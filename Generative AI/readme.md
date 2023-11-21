# AI-Driven Drug-Malady Classification System

## Introduction
This project focuses on the classification of drugs based on their maladies using a machine learning model fine-tuned with OpenAI's GPT-3. It involves processing a dataset of drug names and their associated maladies, converting this data into a format suitable for training a model, and then using the model to classify or predict the malady based on a given drug name.

[Google Slides (Drug Classification)](https://docs.google.com/presentation/d/1xgWroPRc4vvq0_cQVQqlUZOHJVq3kYewXkDDMGBVk6U/edit?usp=sharing)

## Design
<table border="1">
    <tr>
        <th>Step</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Data Preparation</td>
        <td>
            The project begins with a dataset contained in an Excel file, listing drugs and their associated maladies.
            Using Python and Pandas, this data is processed to format specific columns and map categorical data into a numerical format, making it suitable for machine learning applications.
        </td>
    </tr>
    <tr>
        <td>Data Conversion</td>
        <td>
            The processed data is then converted into JSON Lines (JSONL) format. This conversion is crucial as it aligns the data format with what is required by the OpenAI API for model training.
        </td>
    </tr>
    <tr>
        <td>Environment Setup</td>
        <td>
            A Python virtual environment is established to manage dependencies, ensuring that the required libraries are installed and isolated from the global Python environment.
        </td>
    </tr>
    <tr>
        <td>Model Training with OpenAI</td>
        <td>
            The core of the project involves using OpenAI's API to fine-tune a GPT-3 model.
            The JSONL data is first prepared using OpenAI's CLI tools, dividing it into training and validation sets.
            A fine-tuning process is initiated with the OpenAI API, specifying the model type, number of classes, and other parameters relevant to the classification task.
        </td>
    </tr>
    <tr>
        <td>Classification and Prediction</td>
        <td>
            Post-training, the fine-tuned model is used to classify drugs based on the input drug names.
            This classification task involves feeding drug names into the model and receiving predictions about their associated maladies.
        </td>
    </tr>
</table>

## Implementation
To implement this project, follow these steps:

1. **Set up the Python Environment**:
   ```bash
   python3 -m venv venv
   . venv/bin/activate
   pip install pandas openpyxl openai==0.28
   ```

2. **Process the Dataset**:
   - Run the `app.py` script to process the Excel dataset and to create a jsonl file.
     ```bash
     python3 app.py
     ```

3. **Prepare Data for Fine-Tuning**:
   - Use the OpenAI CLI to prepare the data for fine-tuning.
     ```bash
     openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl
     ```

4. **Set Up OpenAI API Key**:
   - Export your OpenAI API key.
     ```bash
     export OPENAI_API_KEY="your_api_key_here"
     ```

5. **Fine-Tune the Model**:
   - Create a fine-tuning job using the OpenAI API.
     ```bash
     openai api fine_tunes.create \
        -t "drug_malady_data_prepared_train.jsonl" \
        -v "drug_malady_data_prepared_valid.jsonl" \
        --compute_classification_metrics \
        --classification_n_classes 7 \
        -m ada \
        --suffix "drug_malady_data"
     ```

6. **Follow the Fine-Tuning Job**:
   - Monitor the fine-tuning job using the job ID.
     ```bash
     openai api fine_tunes.follow -i <JOB ID>
     ```

7. **Run the Test Script**:
   - Execute `test.py` to classify drugs using the fine-tuned model.
     ```bash
     python3 test.py
     ```

     Note: Update this code with your fine-tuned model ID.

By following these steps, you should be able to fine-tune a model to classify drugs based on their maladies and then test the model's performance on new drug names.