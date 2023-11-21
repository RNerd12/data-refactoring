import pandas as pd
import os

# Loop over all files in the input_directory
def getHeaders(input_directory):
    with open(os.path.join(input_directory,"metadata.txt"),'w') as f:
        unique = set()
        for filename in os.listdir(input_directory):
            # Check if the file is an Excel file
            print("processing "+filename)
            if (filename.endswith(".xlsx") or filename.endswith(".xls")):
                # Construct the full file path
                file_path = os.path.join(input_directory, filename)
                # Read the Excel file
                try:
                    # Load only the first row (header) by setting nrows to 0
                    df = pd.read_excel(file_path, nrows=10)
                    # Print the filename and its headers
                    f.write(f"Headers in '{filename}':\n")
                    f.write(str(df.columns.tolist())+"\n")
                    unique.update(df.columns.tolist())
                except Exception as e:
                    # If there was an error reading the Excel file, print the error
                    f.write(f"Error reading {filename}: {e}\n")
                f.write("-" * 40+"\n")
        f.write("unique fields = " + str(unique))
    print("finished processing!")

    print(f"unique fields for {input_directory}= " + str(unique))
    print('-'*40)
