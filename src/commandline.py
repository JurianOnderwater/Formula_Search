import argparse
import sys
from FormulaSearch import FormulaSearch

fs = FormulaSearch()
func_dict = {'search': fs.search(mode='field')}
parser = argparse.ArgumentParser()
parser.add_argument('function', type=str)
subparsers = parser.add_subparsers()

# Create a search subcommand    
parser_search = subparsers.add_parser("search", help='search for a function')
parser_search.add_argument("mode")

# parser_search.set_defaults(func=fs.search())

# Create a save subcommand       
parser_save = subparsers.add_parser('save', help='save a function')
# parser_save.set_defaults(func=fs.save())

# Print usage message if no args are supplied.


if len(sys.argv) <= 1:
    sys.argv.append('--help')
# parser.add_argument('--mode', type=str, required=True)
options = parser.parse_args()
vars = parser_search.parse_args()
print(options)
# Run the appropriate function (in this case showtop20 or listapps)
func = func_dict[options.function]
func(mode='field')

# If you add command-line options, consider passing them to the function,
# e.g. `options.func(options)`