# Chatbot

## Introduction

The Chatbot is a web-based chat application powered by the OpenAI GPT-3.5 model. It allows users to interact with a conversational AI to obtain information from a set of documents.

[Chatbot google slides](https://docs.google.com/presentation/d/122UOc-MyBLZMrOebGAFi9fH4J8Y88xkDHY39ekSPvpo/edit?usp=sharing)

## Design

The design of the Chatbot project can be summarized as follows:

<table border=2>
  <tr>
    <th colspan="2">Design</th>
  </tr>
  <tr>
    <td>Load Documents and Create VectorDB</td>
    <td>
      <ol>
        <li><strong>Document Loading:</strong> Documents are loaded from a specified source, typically a PDF file.</li>
        <li><strong>Document Splitting:</strong> Documents are divided into smaller chunks for efficient retrieval.</li>
        <li><strong>VectorDB Creation:</strong> The documents and chunks are embedded into vector representations for retrieval.</li>
      </ol>
    </td>
  </tr>
  <tr>
    <td>Splitting the Documents into Chunks</td>
    <td>
      <ol>
        <li><strong>Text Splitting:</strong> A Text Splitter (Recursive Character Text Splitter) is used to break down documents into sections.</li>
      </ol>
    </td>
  </tr>
  <tr>
    <td>Using a Conversational Retrieval Chain</td>
    <td>
      <ol>
        <li><strong>Conversational Retrieval Chain Components:</strong>
          <ul>
            <li><strong>GPT-3.5 Chat Model:</strong> Responsible for generating responses.</li>
            <li><strong>Retriever Component:</strong> Retrieves relevant information from documents using the VectorDB.</li>
            <li><strong>Conversation Memory:</strong> Stores chat history for context-aware responses.</li>
            <li><strong>Output Configuration:</strong> Configured to return the answer generated by the chatbot.</li>
          </ul>
        </li>
      </ol>
    </td>
  </tr>
</table>

## Implementation

To run the Chatbot project on Ubuntu, follow these steps:

1. Create a Python virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   . venv/bin/activate
   ```

3. Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the application by running `app.py`:
   ```bash
   python3 app.py
   ```
5. Open you web browser and navigate to http://127.0.0.1:5000 to access the Chatbot web application.

## Output

<img src="img/output.png">