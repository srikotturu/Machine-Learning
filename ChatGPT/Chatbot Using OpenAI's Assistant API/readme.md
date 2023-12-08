# Chatbot using OpenAI's Assistant API

## Introduction

This document provides an overview of a customer support chatbot designed to answer queries  using a specific PDF file as a knowledge base. The chatbot is developed using OpenAI's GPT-3.5 model and leverages the latest advancements in natural language processing to provide accurate and contextually relevant responses.

## Design

<img src="img/design.png">

The chatbot system is designed using Python and involves integration with OpenAI's API. The process is outlined below in a tabular format and compares it with chat completion API:

<table border="1">
  <tr>
    <th>Step</th>
    <th>Assistant API</th>
    <th>Chat Completion API</th>
  </tr>
  <tr>
    <td>1. Initial Setup</td>
    <td>Obtain API keys, set up authorization.</td>
    <td>Obtain API keys, set up authorization.</td>
  </tr>
  <tr>
    <td>2. Document Upload</td>
    <td>Uses Retrieval tool for accessing and processing information from documents.</td>
    <td>Focused more on chat inputs than on document upload.</td>
  </tr>
  <tr>
    <td>3. Define Prompt/Start Conversation</td>
    <td>Create a text prompt or start a conversation in a new Thread.</td>
    <td>Initiate with a conversational message.</td>
  </tr>
  <tr>
    <td>4. Choose Model</td>
    <td>Select an appropriate model (e.g., GPT-3, Codex).</td>
    <td>Uses a model optimized for chat interactions.</td>
  </tr>
  <tr>
    <td>5. API Request/Send Message</td>
    <td>Send a request to Run the Assistant on a Thread with Messages.</td>
    <td>Send a message maintaining conversation context.</td>
  </tr>
  <tr>
    <td>6. Processing</td>
    <td>Assistant uses configuration and Messages in Thread to perform tasks.</td>
    <td>Generates a reply considering the ongoing conversation.</td>
  </tr>
  <tr>
    <td>7. Receive Response</td>
    <td>Assistant appends new Messages to the Thread as output.</td>
    <td>Receive a conversational response relevant to the chat.</td>
  </tr>
  <tr>
    <td>8. Post-Processing/Maintain Context</td>
    <td>Interpret and integrate responses; review Run Steps for insights.</td>
    <td>Use the response in the conversational interface, keeping context.</td>
  </tr>
</table>


## Implementation

To set up and run the chatbot, follow these steps:

1. Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

2. Install necessary packages:
   ```bash
   pip install openai python-dotenv
   ```

3. Run the application:
   ```bash
   python3 app.py
   ```

## Testing

Here's the result:

<img src="img/output.png">

The assistant created here can also be tested on the OpenAI web interface.
<img src="img/web.png">

Note:
- <b><i> We can also create and test the assistant using the OpenAI Playground web interface. Here's a [tutorial document.](https://github.com/srikotturu/Machine-Learning/blob/8fe369a3f5974b14f6b00da0bcb97ba487f0ac45/ChatGPT/Chatbot%20Using%20OpenAI's%20Assistant%20API/OpenAI_Assistant_API_Web.pdf) </i></b>

- An assistant created in the web interface can be used in our project with the assistant ID, eliminating the need to recreate the assistant and upload the file using Python.

- In the current implementation, it's important to note that the assistant API is in beta mode. As a result, there are occasions(as shown) when the assistant may respond indicating that it does not have access to the uploaded document for answering queries. This is a known issue and is expected to be resolved as the API matures and is further developed by OpenAI.

<img src="img/error.png">

## Enhancement Ideas

Future enhancements can include:
- Improved error handling and logging for more robust operation.
- Integration with a user interface for easier interaction.
- Expansion of the knowledge base to cover a broader range of topics.

## References

For more information, visit:
- OpenAI Assistants Overview: [OpenAI Assistants Documentation](https://platform.openai.com/docs/assistants/overview)