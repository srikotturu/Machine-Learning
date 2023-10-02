# Customer Support System: An email to the customer

## Introduction

The Customer Support System is a web application that utilizes the OpenAI GPT-3.5 Turbo model to provide customer support for an electronic product company. This system generates customer comments, email subjects, comment summaries, and email responses based on user interactions. It offers support in multiple languages, including English, Spanish, and Portuguese.

## Design

The system is designed as a Flask web application with a straightforward user interface. Users can select the language in which they want to generate email responses and view the generated customer comment and email response. The application follows these key design components:

- **Flask Web Application**: The application is built using Flask, a lightweight web framework in Python, to handle user interactions.

- **OpenAI Integration**: It integrates with the OpenAI GPT-3.5 Turbo model to generate text-based responses for customer support tasks.

- **HTML Template**: The user interface is designed using an HTML template (`index.html`) with a language dropdown menu, question, and answer containers.

We will test the following:
<img src="img/table.png">

## Implementation

To run this application, follow these implementation steps:

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   . venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install flask openai python-dotenv
   ```

4. Start the Flask application:
   ```bash
   python3 app.py
   ```

## Test (Output)

Once the application is running, open a web browser and navigate to `http://localhost:5000`. You can then interact with the system as follows:

<img src="img/english comment.png">

- Choose the desired language from the dropdown menu.
- View the generated customer comment in the "Question" container.
- Observe the corresponding email response in the "Answer" container.
- Click the "Process" button to initiate the processing of the customer comment.

The application will display the generated email response based on the selected language and customer comment.

<b>English Email generated from English Comment:</b>
<img src="img/eng to eng.png">

<b> Portugese Email generated from English Comment: </b>
<img src="img/eng to port.png">