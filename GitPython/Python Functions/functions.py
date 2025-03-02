import csv
import json

class Reader:
    def __init__(self, file_path, row_sep='\n', col_sep=','):
        #Initializes the FileReader with a file path and optional separators
        self.file_path = file_path
        self.row_sep = row_sep
        self.col_sep = col_sep
        self.data = self._read_file()  # Store the table upon initialization

    def _read_file(self):
        # Reads the file and stores it as a list of lists (table format)
        try:
            with open(self.file_path, 'r') as file:
                return [line.strip().split(self.col_sep) for line in file if line.strip()]
        except FileNotFoundError:
            return "Error: File not found."
        except IOError:
            return "Error: Could not read the file."

    def read(self):
        # Returns the entire table as a list of lists
        return self.data

    def __getitem__(self, index):
        # Allows indexing to get specific rows.
        return self.data[index]



class Transformer():
    def __init__(self, data, header_index=0):
        self.data = data
        self.header_index = header_index
        self.headers = data[header_index]
        self.rows = data[:header_index] + data[header_index + 1:]  # Exclude header row
        self.transformed_data = self.dictify()

    def dictify(self):
        # Convert the list of lists into a dictionary using the specified header row
        return [dict(zip(self.headers, row)) for row in self.rows]

    def drop_columns(self, columns):
        # Drop specified columns from the transformed dictionary
        if not isinstance(columns, list):
            columns = [columns]
        self.transformed_data = [
            {key: value for key, value in row.items() if key not in columns}
            for row in self.transformed_data
        ]

    def get_data(self):
        # Return the transformed data
        return self.transformed_data


class Loader():
    def __init__(self, data):
        self.data = data  # transformed data from the Transformer class


    def load(self, format="csv", delimiter=",", file_name="output"):
        # Load the transformed data to a specified format. keeping it bound to csv and json. DB loads would lengthen the class
        if format == "csv":
            self._write_csv(delimiter, file_name)
        elif format == "json":
            self._write_json(file_name)
        else:
            raise ValueError("Unsupported format. Supported formats: 'csv', 'json'.")


    def _write_csv(self, delimiter, file_name):
        # Write the transformed data to a CSV file with the specified delimiter
        with open(f"{file_name}.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.data[0].keys(), delimiter=delimiter)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"Data has been written to {file_name}.csv")


    def _write_json(self, file_name):
        # Write the transformed data to a JSON file
        with open(f"{file_name}.json", mode="w") as file:
            json.dump(self.data, file, indent=4)
        print(f"Data has been written to {file_name}.json")


