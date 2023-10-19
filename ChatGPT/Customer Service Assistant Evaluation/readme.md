# Customer Service Assistant Evaluation

## Introduction

This repository contains a set of Python scripts that demonstrate the use of the OpenAI GPT-3.5 Turbo model to assist with customer queries. The scripts provide functionality to classify customer queries, evaluate responses, and generate relevant information based on product-related queries. 

[Customer Service Assistant Evaluation](https://docs.google.com/presentation/d/1m4wZ_SDiu-8WZKSV1A87coMGksTiWyfUJ6iN-Sr8H0A/edit?usp=sharing)

## Design

The repository includes the following Python scripts:

<table border="1">
    <tr>
        <th>File Name</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>chain_of_thoughts.py</td>
        <td>This script performs chain-of-thought processing to generate meaningful results from a series of connected thoughts.</td>
    </tr>
    <tr>
        <td>check_output.py</td>
        <td>This script checks the output of a particular process or operation to ensure it meets the desired criteria.</td>
    </tr>
    <tr>
        <td>classification.py</td>
        <td>This script is used for classifying data into different categories or groups based on specific criteria.</td>
    </tr>
    <tr>
        <td>evaluation1.py</td>
        <td>These scripts are used for evaluating different aspects of a dataset or process. They provide insight into the effectiveness or accuracy of the operation.</td>
    </tr>
    <tr>
        <td>evaluation2.py</td>
        <td>These scripts are used for evaluating different aspects of a dataset or process. They provide insight into the effectiveness or accuracy of the operation.</td>
    </tr>
    <tr>
        <td>moderation.py</td>
        <td>This script performs moderation by filtering out unwanted or inappropriate content from a dataset.</td>
    </tr>
    <tr>
        <td>products_data.py</td>
        <td>This script processes and analyzes the data from products.json to extract meaningful information.</td>
    </tr>
    <tr>
        <td>utils.py</td>
        <td>This script contains utility functions that can be used across different scripts to perform common operations.</td>
    </tr>
</table>

   The data file products.json contains a dataset that can be used in conjunction with the Python scripts for data analysis and processing.

## Implementation

To run these scripts, follow these steps:

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   . venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install python-dotenv openai utils
   ```

4. Run the Python scripts with the following commands, replacing `<filename.py>` with the actual filename of the script you want to execute:

   ```bash
   python3 <filename.py>
   ```
**Note:** Ensure that you have set up your OpenAI API key and environment variables as needed for the scripts to function correctly.

## Output

Each script provides specific output as described in the comments and documentation within the code. Please refer to this [Google slides](https://docs.google.com/presentation/d/1m4wZ_SDiu-8WZKSV1A87coMGksTiWyfUJ6iN-Sr8H0A/edit?usp=sharing) tp see the output they generate.

