# Voice-Activated Conversational AI with Document Context Integration

## Introduction
This project integrates advanced technologies in audio processing, speech recognition, conversational AI, and document context processing to create a sophisticated voice-activated conversational system. The system listens for a wake word, processes spoken queries or commands, and generates contextually relevant responses using information from a loaded document. This solution is ideal for interactive voice assistants, automated customer support, or educational tools where voice-activated access to document-based information is beneficial.

[Google Slides (Voice Assistant with Document Context)](https://docs.google.com/presentation/d/1B7-iEMma-eNnnmATr1CIj2yjVvAwRjKVU8Y3CM6GHRA/edit?usp=sharing)

## Design

## Implementation

To set up and run the project, follow these steps:

1. **Create a Python Virtual Environment:**
   ```bash
   python3 -m venv venv
   . venv/bin/activate

2. **Install Dependencies:**
    ```bash
    sudo apt update && sudo apt install ffmpeg
    pip install -r requirements.txt
    ```

3. **Run the Script:**
    ```bash
    python3 app.py
    ```

    - The script will prompt you to enter a wake word. The default wake word is "hey computer".
    - Once the wake word is set, the script will begin listening for your voice commands.
    - To stop the script, press `Ctrl + C`.

## Output

<img src= "img/output.png">
To hear the assistant's audio response, please see the google slides. 