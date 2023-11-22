import pandas as pd  # Import the pandas library


n = 2000  # Set the number of rows to read


# Read data from Excel
df = pd.read_excel('Medicine_description.xlsx', sheet_name='Sheet1', header=0, nrows=n)


# Get unique values in 'Reason' column
reasons = df["Reason"].unique()


# Create a dictionary for mapping reasons to numerical indices
reasons_dict = {reason: i for i, reason in enumerate(reasons)}


# Format 'Drug_Name' column
df["Drug_Name"] = "Drug: " + df["Drug_Name"] + "\n" + "Malady:"


# Map 'Reason' values to numerical indices
df["Reason"] = " " + df["Reason"].apply(lambda x: "" + str(reasons_dict[x]))


# Drop the 'Description' column
df.drop(["Description"], axis=1, inplace=True)


# Rename columns
df.rename(columns={"Drug_Name": "prompt", "Reason": "completion"}, inplace=True)


# Convert dataframe to jsonl format
jsonl = df.to_json(orient="records", indent=0, lines=True)


# Write jsonl to a file
with open("drug_malady_data.jsonl", "w") as f:
    f.write(jsonl)