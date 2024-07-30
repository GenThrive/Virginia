import os
import pathlib
import pandas as pd


# Load the Excel file
data_filepath = pathlib.Path(__file__).parent.absolute()
data_records_filepath = os.path.join(data_filepath,'data_records.xls')

# Define the names of sheets to be processed
sheets_to_process = ['Programs', 'Organization']

# Load the Excel file
xls = pd.ExcelFile(data_records_filepath, engine='openpyxl')



# List of columns to process
# columns_to_process = ['Services_Resources', 'Environmental_Themes', 'Program/Offering_Locations']

# Process each sheet
with pd.ExcelWriter('modified_file.xlsx', engine='openpyxl') as writer:
    # Process each sheet specified in sheets_to_process
    for sheet_name in sheets_to_process:
        if sheet_name in xls.sheet_names:
            # Read the sheet into a DataFrame
            df = pd.read_excel(xls, sheet_name=sheet_name, engine='openpyxl')

            # Apply the transformation to all columns
            for column in df.columns:
                if df[column].dtype == 'object':  # Check if the column is of string type
                    df[column] = df[column].apply(lambda x: x.replace(",", ", ") if isinstance(x, str) else x)

            # Write the modified DataFrame back to a new sheet in the output file
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the modified DataFrame to a new Excel file
        df.to_excel('data/modified_file.xlsx', index=False, engine='openpyxl')
