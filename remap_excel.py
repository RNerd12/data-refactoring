import os
import pandas as pd
from configs1 import header_mappings
# Function to merge duplicate columns
def merge_duplicate_columns(df, column_name):
    temp = 'temp_column_name'
    if column_name == "":
        return df
    columns = [col for col in df if col.startswith(column_name)]
    if len(columns) > 1:
        # Combine and drop duplicates
        df[temp] = df[columns].apply(lambda x: ', '.join(x.dropna().astype(str)), axis=1)
        df.drop(columns=columns, inplace=True)
        df.rename(columns={temp:column_name},inplace=True)
    return df


# Process each file in the directory
def remapExcel(input_directory,header_mappings = header_mappings):
    output_directory = input_directory +' csv'
    metadata_file_path = input_directory + '/metadata.csv'
    os.makedirs(output_directory, exist_ok=True)
    metadata = []
    for filename in os.listdir(input_directory):
        if filename.endswith((".xlsx", ".xls")):
            print(f"Processing {filename}")
            file_path = os.path.join(input_directory, filename)
            # Read the Excel file
            df = pd.read_excel(file_path)
            df = df.astype(str)
            # Standardize header names
            df.columns = [header_mappings.get(str(col).strip(), str(col).strip()) for col in df.columns]

            # Merge duplicate columns
            for col in set(df.columns):
                df = merge_duplicate_columns(df, col)

            # Save the transformed dataframe to a new CSV file
            csv_filename = os.path.splitext(filename)[0] + '.csv'
            output_file_path = os.path.join(output_directory, csv_filename)
            df.to_csv(output_file_path, index=False)

            # Add information to metadata
            metadata.append({
                'FileName': csv_filename,
                'Headers': ', '.join(df.columns)
            })

    # Convert metadata to a DataFrame and save as a CSV
    metadata_df = pd.DataFrame(metadata)
    metadata_df.to_csv(metadata_file_path, index=False)

    print(f"All files in {input_directory} have been processed. Metadata file has been saved.")
