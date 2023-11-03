import os
import openai
import sys
from flask import Flask, render_template, request
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

# Function to load database from file
def load_db(file, chain_type, k):
    loader = PyPDFLoader(file_path=file)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = DocArrayInMemorySearch.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})

    # Create a ConversationBufferMemory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True  # Return chat history as a list of messages
    )

    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=False,
        return_generated_question=False,
        memory=memory,
        output_key='answer'  # Specify the desired output key
    )

    return qa

chatbot = load_db(file='docs/2023Catalog.pdf', chain_type='stuff', k=3)
app = Flask(__name__)  # Add this line to instantiate the Flask app

@app.route("/")
def home():
    return render_template("index.html")

chat_history = []
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
   

    # Get the response from the chatbot
    response = chatbot({
        'question': userText,
        'chat_history': []  # Provide an empty list as the initial chat history??
    })
    return response['answer']

if __name__ == "__main__":
    app.run(debug=True)
 