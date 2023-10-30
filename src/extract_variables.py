import re
import json

class StringManipulations():
    def tokenize(formula: str):
        #remove whitespace
        formula.replace(" ", "")
        delimiters = ["/", "+", "-", "*",]
        for delimiter in delimiters:
            for delimiter in delimiters:
                string = " ".join(formula.split(delimiter))
        return string.split()
    
    def remove_math(tokenized: list):
        return [i for i in tokenized if i not in ("+", "-", "*", "/", "=")]
    
    def write_json(new_data: dict, filename: str, field: str):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data[field].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)

# print(StringManipulations.tokenize("E = M C^2"))
# print(StringManipulations.remove_math(StringManipulations.tokenize("E = M C^2")))
