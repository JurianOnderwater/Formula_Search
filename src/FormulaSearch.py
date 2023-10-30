import re
import json
from extract_variables import StringManipulations as sm
import argparse
from helptext import HelpText



class FormulaSearch:
    def __init__(self) -> None:
        pass

    def search(self, mode: str, 
               fields:list[str] = ['physics',
                                    'computer science',
                                    'engineering',
                                    'chemistry',
                                    'biology',], 
                inputs_variables: list = [None]):
        """
        Match all formulas that exactly match the variables provided

        Args:
            mode (str): search mode used
            inputs_variables (list[str]): list of variables in the formula
        """

        file = open("../formulas/formulas.json")
        data = json.load(file)
        match mode:
            case "name":
                for field in fields:
                    for entry in data[str(field)]:
                        if entry['name'] == inputs_variables[0]:
                            print(f"{entry['name']}: {entry['equation']}")
            case "field":
                fields = (
                    input(
                        """Please choose what field's formulas you want to search in.\n
If you want to look through multiple fields, please type them out with a space in between:\n"""
                    )
                    .lower()
                    .split(" ")
                )
                for field in fields:
                    print(f"\n{field} equations:\n______________________")
                    for entry in data[field]:
                        print(f"{entry['name']}: {entry['equation']}")
            case "variables":
                pass
        return

    def save(self, fields: list[str]):
        """
        Save a formula to the database

        Args:
            field (list[str]): The field(s) of science where the formula is used
        """
        formula = {}
        formula["name"] = input("Please enter the name of the formula: ").lower()
        formula["equation"] = input(
            "Type out the formula, please use spaces between every component.\nEx.: 'E = M C^2'\nType here: "
        )
        formula["variables"] = sm.remove_math(sm.tokenize(formula=formula["equation"]))
        # print(formula['variables'])
        for field in fields:
            sm.write_json(
                new_data=formula, filename=f"formulas/formulas.json", field=field
            )

    def edit_function(self):
        print("Not implemented yet, sorry :(")

def main():
    helptext = HelpText()
    parser = argparse.ArgumentParser()
    
    parser.add_argument('function', type=str, choices=['search', 'save'], help=helptext.functionhelp)
    parser.add_argument('--mode', type=str, choices=['name', 'field', 'variables'], help=helptext.modehelp)
    parser.add_argument('--variables', nargs='*', help=helptext.variableshelp)
    parser.add_argument('--field', nargs='*', help=helptext.fieldhelp)

    args = parser.parse_args()
    print(f"mode: {args.mode}")
    fs = FormulaSearch()
    if args.function == 'search':
        fs.search(mode=args.mode, inputs_variables=args.variables )
    elif args.function == 'save':
        fs.save(args.field)
    else:
        print('Choose an existing function dickhead')



if __name__ == "__main__":
    main()