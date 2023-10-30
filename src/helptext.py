class HelpText:
    def __init__(self) -> None:
        self.functionhelp =  """
                        Choose between 'search' and 'save'\n
                        For search there is suboption `--mode`. Mode lets you specify \n
                        which search mode you want to use.
                        For save you need to use `--field` to specify under which field(s)\n
                        you want to store the formula.
                        """
        self.modehelp =  """
                    Choose which search mode to use. Options are:\n
                    - name: search by function name\n
                    - field: list all functions saved to specific field
                    - variables: list all functions containing provided variables
                    """
        self.variableshelp =  """
                        Additional values needed for search. When combined with mode\n
                        - name: enter the name of the function you're looking for
                        - variables: enter the variables you want to look for
                        """
        self.fieldhelp = """
                    Chose the field under which you want to save the formula
                    """