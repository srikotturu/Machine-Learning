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

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file
openai.api_key = os.environ['API_KEY']

@click.command()
@click.option("--model", default="base", help="Model to use", type=click.Choice(["tiny", "base", "small", "medium", "large"]))
@click.option("--english", default=False, help="Whether to use the English model", is_flag=True, type=bool)
@click.option("--energy", default=300, help="Energy level for the mic to detect", type=int)
@click.option("--pause", default=0.8, help="Pause time before entry ends", type=float)
@click.option("--dynamic_energy", default=False, is_flag=True, help="Flag to enable dynamic energy", type=bool)
@click.option("--wake_word", default="hey computer", help="Wake word to listen for", type=str)
@click.option("--verbose", default=True, help="Whether to print verbose output", is_flag=True, type=bool)
def main(model, english, energy, pause, dynamic_energy, wake_word, verbose):
    if model != "large" and english:
        model = model + ".en"
    audio_model = whisper.load_model(model)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()

    threading.Thread(target=record_audio, args=(audio_queue, energy, pause, dynamic_energy, verbose)).start()
    threading.Thread(target=transcribe_forever, args=(audio_queue, result_queue, audio_model, english, wake_word, verbose)).start()
    threading.Thread(target=reply, args=(result_queue, verbose)).start()

    while True:
        print(result_queue.get())

def record_audio(audio_queue, energy, pause, dynamic_energy, verbose):
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate=16000) as source:
        print("Listening...")
        i = 0
        while True:
            audio = r.listen(source)
            torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
            audio_data = torch_audio
            audio_queue.put_nowait(audio_data)
            i += 1
            if verbose:
                print(f"Audio recorded - {i}")

def transcribe_forever(audio_queue, result_queue, audio_model, english, wake_word, verbose):
    while True:
        audio_data = audio_queue.get()
        if english:
            result = audio_model.transcribe(audio_data, language='english')
        else:
            result = audio_model.transcribe(audio_data)

        predicted_text = result["text"]
        print(f"Predicted Text: {predicted_text}")


        if predicted_text.strip().lower().startswith(wake_word.strip().lower()):
            pattern = re.compile(re.escape(wake_word), re.IGNORECASE)
            predicted_text = pattern.sub("", predicted_text).strip()
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            predicted_text = predicted_text.translate({ord(i): None for i in punc})
            if verbose:
                print(f"Detected wake word - '{wake_word}'. Processing: {predicted_text}")

            result_queue.put_nowait(predicted_text)
        else:
            if verbose:
                print("You did not say the wake word.. Ignoring")

def reply(result_queue, verbose):
    while True:
        question = result_queue.get()
        prompt = f"Q: {question}?\nA:"
        messages = [{"role": "user", "content": prompt}]
        data = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
            max_tokens=100,
            n=1,
            stop=["\n"]
        )
        print("Received data: ", data)

        try:
            # Extract the answer from the data
            answer = data["choices"][0]["message"]["content"]
            # print("Answer extracted: ", answer)
            
            # Convert the answer to speech
            mp3_obj = gTTS(text=answer, lang="en", slow=False)
        except KeyError as ke:
            print(f"KeyError: {ke}. Response structure might have changed.")
        except Exception as e:
            # Predefined responses for when an error occurs
            choices = [
                "I'm sorry, I don't know the answer to that",
                "I'm not sure I understand",
                "I'm not sure I can answer that",
                "Please repeat the question in a different way"
            ]
            # Select a random response
            mp3_obj = gTTS(text=choices[np.random.randint(0, len(choices))], lang="en", slow=False)
            if verbose:
                print(f"Error generating reply: {type(e).__name__}: {e}")

        # In both cases, we play the audio
        # print("Saving reply as mp3...")
        mp3_obj.save("reply.mp3")
        reply_audio = AudioSegment.from_mp3("reply.mp3")
        # print("Playing reply...")
        play(reply_audio)

main()