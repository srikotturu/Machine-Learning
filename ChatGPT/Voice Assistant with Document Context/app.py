from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import whisper
import queue
import os
import threading
import torch
import numpy as np
import re
from gtts import gTTS
import openai
import click

# Import additional modules required for document processing
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables from .env file
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Function to load database from file for conversational context
def load_db(file, chain_type, k):
    loader = PyPDFLoader(file_path=file)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = DocArrayInMemorySearch.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=False,
        return_generated_question=False,
        memory=memory,
        output_key='answer'
    )

    return qa

# Initialize the conversational chain with the PDF document
conversational_chain = load_db(file='docs/2023Catalog.pdf', chain_type='stuff', k=3)

@click.command()
@click.option("--model", default="base", help="Model to use", type=click.Choice(["tiny", "base", "small", "medium", "large"]))
@click.option("--english", default=False, is_flag=True, help="Whether to use the English model")
@click.option("--energy", default=300, help="Energy level for the mic to detect", type=int)
@click.option("--pause", default=0.8, help="Pause time before entry ends", type=float)
@click.option("--dynamic_energy", default=False, is_flag=True, help="Flag to enable dynamic energy")
@click.option("--wake_word", default="hey computer", help="Wake word to listen for", type=str)
@click.option("--verbose", default=True, is_flag=True, help="Whether to print verbose output")
def main(model, english, energy, pause, dynamic_energy, wake_word, verbose):
    # Load the Whisper model
    if model != "large" and english:
        model = model + ".en"
    audio_model = whisper.load_model(model)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()

    # Start the threads
    threading.Thread(target=record_audio, args=(audio_queue, energy, pause, dynamic_energy, verbose)).start()
    threading.Thread(target=transcribe_forever, args=(audio_queue, result_queue, audio_model, english, wake_word, verbose)).start()
    threading.Thread(target=reply, args=(result_queue, verbose, conversational_chain)).start()

    while True:
        print(result_queue.get())

# Function to record audio from the microphone
def record_audio(audio_queue, energy, pause, dynamic_energy, verbose):
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        while True:
            audio = r.listen(source)
            torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_queue.put_nowait(torch_audio)
            if verbose:
                print("Audio recorded")

# Function to transcribe audio using the Whisper model
def transcribe_forever(audio_queue, result_queue, audio_model, english, wake_word, verbose):
    while True:
        audio_data = audio_queue.get()
        if english:
            result = audio_model.transcribe(audio_data, language='english')
        else:
            result = audio_model.transcribe(audio_data)

        predicted_text = result["text"]
        if verbose:
            print(f"Predicted Text: {predicted_text}")

        if predicted_text.strip().lower().startswith(wake_word.strip().lower()):
            pattern = re.compile(re.escape(wake_word), re.IGNORECASE)
            predicted_text = pattern.sub("", predicted_text).strip()
            predicted_text = re.sub(r'[^a-zA-Z0-9\s]', '', predicted_text)
            if verbose:
                print(f"Detected wake word - '{wake_word}'. Processing: {predicted_text}")

            result_queue.put_nowait(predicted_text)
        else:
            if verbose:
                print("Wake word not detected.")

# Function to reply to the transcribed text using the loaded PDF and OpenAI's model
def reply(result_queue, verbose, conversational_chain):
    while True:
        question = result_queue.get()
        response = conversational_chain({
            'question': question,
            'chat_history': []
        })
        answer = response['answer'] if 'answer' in response else "I'm not sure I can answer that."
        mp3_obj = gTTS(text=answer, lang="en", slow=False)
        mp3_obj.save("reply.mp3")
        reply_audio = AudioSegment.from_mp3("reply.mp3")
        play(reply_audio)

if __name__ == "__main__":
    main()
 