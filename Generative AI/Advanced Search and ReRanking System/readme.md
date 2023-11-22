# Advanced Search and ReRanking System

## Introduction

This project is focused on implementing an advanced search and reranking system. It leverages the capabilities of Cohere and Weaviate to perform dense retrieval and rerank search results, enhancing the relevance and accuracy of information retrieval. This system can be applied in various domains where precise and context-aware search results are essential.

## Design

The design of this project is centered around integrating two major components: Cohere and Weaviate. The system utilizes Cohere for its natural language understanding capabilities, particularly in reranking responses to align better with the query's context. Weaviate, on the other hand, is used for its efficient and scalable vector search, enabling dense retrieval of documents.

### Process

<table border=1>
  <tr>
    <td>1.</td>
    <td><strong>Setup</strong></td>
    <td>The initial phase involves setting up the necessary environment, including installing dependencies and setting up environment variables for API keys.</td>
  </tr>
  <tr>
    <td>2.</td>
    <td><strong>Dense Retrieval</strong></td>
    <td>This step uses Weaviate's vector search to retrieve a set of documents that are semantically close to the input query.</td>
  </tr>
  <tr>
    <td>3.</td>
    <td><strong>Reranking</strong></td>
    <td>In this step, Cohere's reranking model is applied to the results from dense retrieval, refining them to ensure that the most contextually relevant results are prioritized.</td>
  </tr>
  <tr>
    <td>4.</td>
    <td><strong>Integration</strong></td>
    <td>Both dense retrieval and reranking functionalities are integrated into a single, seamless workflow, providing an end-to-end solution for enhanced search capabilities.</td>
  </tr>
</table>


## Implementation

To get the system up and running, follow these steps:

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