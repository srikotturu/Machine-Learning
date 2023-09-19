# Customer Support System using Web page

## Introduction
This project is a Customer Support System that uses web crawling, text embedding, and the OpenAI API to answer questions about webpages' content. It includes two implementations: `Command Line Based` and `Web Based`.

[Customer Support System (Google Slides)](https://docs.google.com/presentation/d/12nCGc0cTLNANdy5E32ED5QG6uSdT6HaiYG5wjZ0hu1w/edit?usp=sharing)

## Design
The system is designed to perform the following steps:

**1. Web Crawling:** It crawls webpages, extracts their text content, and stores it for further processing.

**2. Text Embedding:** The extracted text is tokenized and embedded into numerical representations using OpenAI's embedding models.

**3. Question Answering:** Users can ask questions about the crawled webpages, and the system generates responses using the embeddings and OpenAI's API.

### Command Line Based
In the command line-based implementation, users interact with the system through the Ubuntu terminal. They can ask questions about the webpages crawled by the system, and the system generates responses based on the embedded text data. This implementation provides a straightforward and text-based interface for users to query web content.

### Web-Based (Flask)
The web-based implementation utilizes the Flask framework to provide a user-friendly interface for interacting with the system. Users can access the system through a web browser, making it accessible and convenient. This web interface allows users to input questions and receive responses, enhancing the user experience and accessibility of the system.

## Implementation (Command Line Based & Web Based)

### Ubuntu Terminal Setup
To run this project on an Ubuntu system, follow these steps:

* (**Optional**) Execute the complete code on Jupyter Notebook (`command_code.ipynb`) or Google Colab.

* Export the Jupyter notebook to .py and separate it into different parts (`crawl.py`, `embed.py`, `app.py`).

*  Install Python 3.10's virtual environment package, if not installed already
```bash
$ sudo apt install python3.10-venv
```
* Create a Python virtual environment named 'venv'
```bash
$ python3 -m venv venv
```
* Activate the virtual environment
```bash
$ . venv/bin/activate
```
* Install the required Python packages listed in 'requirements.txt'
```bash
$ pip install -r requirements.txt
```
* To crawl data from webpages, run:
```bash
$ python3 crawl.py
```
* To embed the crawled data, run:
```bash
$ python3 embed.py
```
* To run the system, run:
```bash
$ python3 app.py
```
* To deactivate the virtual environment, run:
```bash
$ deactivate
```

## Output (Command Line based)
Note: I crawled the website www.x.ai

<img src="Command Line Based/img/output.png">

## Output (Web Flask based)
<img src="Web Based/img/ask.png" width="400px">
<img src="Web Based/img/reply1.png" width="400px">
<img src="Web Based/img/reply2.png" width="400px">