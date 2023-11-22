# AI Article Assistant

## Introduction

The AI Article Assistant is a Python-based tool designed to facilitate the process of finding relevant information from a large text corpus and generating concise answers to user queries. This tool leverages advanced natural language processing techniques and is particularly useful for extracting insights from extensive articles or documents.

[Google Slides(AI Article Assitant)]()

## Design

The design of the AI Article Assistant is focused on efficiently parsing and understanding large volumes of text. The system is structured into several key components:

<table border=1>
  <tr>
    <td>1.</td>
    <td><strong>Text Processing</strong></td>
    <td>The initial phase involves cleaning and splitting the provided text into manageable segments. This step is crucial for ensuring accurate analysis in subsequent stages.</td>
  </tr>
  <tr>
    <td>2.</td>
    <td><strong>Embedding Generation</strong></td>
    <td>Using Cohere's powerful AI models, the tool generates embeddings for each text segment. These embeddings are numerical representations that capture the semantic essence of the text.</td>
  </tr>
  <tr>
    <td>3.</td>
    <td><strong>Search Index Creation</strong></td>
    <td>An Annoy Index is created using the embeddings, allowing for efficient nearest-neighbor searches. This index serves as the backbone for retrieving relevant text segments based on user queries.</td>
  </tr>
  <tr>
    <td>4.</td>
    <td><strong>Article Searching and Answer Generation</strong></td>
    <td>The core functionality of the tool involves searching the text corpus for segments most relevant to a given query and then generating a concise answer or summary based on the found content.</td>
  </tr>
</table>


## Implementation

To run the AI Article Assistant, follow these steps:

1. **Set Up a Python Virtual Environment**: This isolates your project dependencies from other Python projects.
   ```bash
   python3 -m venv venv
   . venv/bin/activate
   ```

2. **Install Required Dependencies**: Ensure all necessary libraries are installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**: Execute the main script to start the tool.
   ```bash
   python3 app.py
   ```

*Note: Ensure you have a `.env` file with the necessary API keys (e.g., for Cohere) and any other configuration your script requires.*

## Output

Please find the output of the AI Article Assistant in this [link(output.txt)]().