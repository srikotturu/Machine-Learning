import openai
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI Client
client = openai.Client()

# Uploading a file for Retrieval
with open("SFBUCatalog2023.pdf", "rb") as file:
    uploaded_file = client.files.create(
        file=file,
        purpose='assistants'
    )

# Create an Assistant with Retrieval Enabled
# This assistant uses the uploaded PDF file as a knowledge base to respond to queries about the university
assistant = client.beta.assistants.create(
    instructions="You are a customer support chatbot with access to a PDF file about the university. Use the information from this file to answer user questions about the university.",
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
    file_ids=[uploaded_file.id]
)

thread = client.beta.threads.create()

def send_message_and_get_response(user_message):
    # Send a user message to the thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
    )

    # Create a run to get the assistant's response
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user's question. Use the knowledge base to help you answer the question."
    )

    # Wait for the run to complete with a maximum number of retries
    max_retries = 10
    while max_retries > 0:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if run_status.status in ["completed", "failed"]:
            print(f"Run status: {run_status.status}")
            break
        time.sleep(5)
        max_retries -= 1

    # Retrieve messages and sort them by role
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    if not messages.data:
        print("No messages found in the thread.")
        return

    user_messages = []
    assistant_messages = []

    for message in messages.data:
        content_list = message.content if isinstance(message.content, list) else [message.content]
        for content in content_list:
            if hasattr(content, 'text') and hasattr(content.text, 'value'):
                text = content.text.value
                if message.role == "user":
                    user_messages.append(text)
                else:
                    assistant_messages.append(text)

    # Print user messages followed by assistant messages
    for msg in user_messages:
        print(f"User : {msg}")
    for msg in assistant_messages:
        print(f"Assistant : {msg}")

# Example usage
send_message_and_get_response("What is the scholarship offered?")
