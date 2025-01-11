# Recursive Worksheet Creator - Creates a python file with random recursive 
# Algorithms to practice along with tests via pytest

import argparse
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path
import pytest
import random
import shutil




TEMPLATES_PATH = Path((os.path.dirname(__file__)), "templates", "algorithms")
TEMPLATES_WITH_INSTRUCTIONS = Path((os.path.dirname(__file__)), \
                                    "templates", "algorithms_with_instructions")
POSSIBLE_ALGORITHMS_PER_PAGE = len(os.listdir(TEMPLATES_PATH))
WORKSHEETS_PATH = Path((os.path.dirname(__file__)), "worksheets")


@dataclass
class Arguments():
    command: str
    date: str
    number: int
    no_instructions: bool
    function: str


def _pick_random_algorithms(number: int) -> list:
    algorithms = os.listdir(TEMPLATES_PATH)
    random_set = set()
    while len(random_set) < number:
        random_set.add(random.choice(algorithms))
    return list(random_set)


def _write_tests(test_path, tests):
    # Heading
    with open(test_path, "w") as fout:
        fout.write('import pytest\n')
        fout.write('import worksheet\n')
        fout.write('from collections import Counter\n\n\n') 

    while len(tests) > 0:
        current_test = tests.pop()

        # Read and store test template
        template_path = Path((os.path.dirname(__file__)), "templates", "tests", current_test)
        with open(template_path, 'r') as t:
            lines = t.readlines()

        # Write test to the test file
        with open(test_path, 'a') as fout:
            for line in lines:
                fout.write(line)
            fout.write('\n\n\n')


def _write_worksheet(
    worksheet_path: Path, 
    algorithms: list[str], 
    no_instructions: bool
):

    # Write Heading of worksheet and clear worksheet if it already exists. 
    with open(worksheet_path, 'w') as fout:
        fout.write(f'# Recursion Worksheet: {datetime.now().strftime("%m-%d")}\n\n')
    
    for i in range(len(algorithms)):
    # while len(algorithms) > 0:
        current_algorithm = algorithms[i]

        # Read and store algo from template
        if no_instructions is False:
            template_path = Path((os.path.dirname(__file__)), 
                        "templates", 
                        "algorithms_with_instructions", 
                        current_algorithm)
        else:
            template_path = Path((os.path.dirname(__file__)), "templates", "algorithms", current_algorithm)

        with open(template_path, 'r') as w:
            lines = w.readlines()

        with open(worksheet_path, 'a') as fout:
            for i in range(len(lines)):
                if i == 0:
                    # Creating a hash header 
                    white_space = ((80 - len(lines[i])) // 2) - 3
                    title = '#' + white_space * '=' + ' ' + lines[i].rstrip('\n') + ' ' + white_space * '='
                    fout.write(title)

                else:
                    fout.write(lines[i])
            fout.write('\n\n\n')
    return None


def make_new_worksheet(args):
    # Creates a path to a directory with today's date 
    if args.date is None:
        args.date = datetime.now().strftime('%m-%d')
    path = Path((os.path.dirname(__file__)), "worksheets", args.date)
    if path.exists() is False:
        os.makedirs(path)

    # Picks Random algorithms based on argument number
    algos = _pick_random_algorithms(args.number)
    
    # Paths to the new worksheet and test files
    worksheet_path = Path(path, "worksheet.py")
    test_path = Path(path, "test_worksheet.py")

    # Write the worksheet and pytest file in same directory
    _write_worksheet(worksheet_path, algos, args.no_instructions)
    _write_tests(test_path, algos)
    return 


def remove_worksheet(args) -> None:
    """Removes a specific worksheet."""
    folder_to_remove = Path(WORKSHEETS_PATH, args.date)
    if os.path.isdir(folder_to_remove):
        while True:
            user_input = input(f'Are you sure you want to remove the directory{args.date}? y/n: ')
            if user_input.lower() == 'y' or user_input.lower() == 'yes':
                print(f'.....Removing {folder_to_remove}...\n')
                shutil.rmtree(folder_to_remove)
                print(f'Successfully removed the {args.date} folder')
                break
            elif user_input.lower() == 'n' or user_input.lower == 'no':
                print('Process aborted........ exiting program. ')
    return


def clean(args) -> None:
    """ Removes all files from the worksheet folder. """

    worksheet_folders = os.listdir(WORKSHEETS_PATH)
    print('Are you sure you want to permanently delete all of the worksheet folders below?  ')
    for folder in worksheet_folders:
        print(folder)

    while True:
        user_input = input('y/n ')
        if user_input.lower() == 'y' or user_input.lower() == 'yes':
            for folder in worksheet_folders:
                print(f'...removing {folder}')
                worksheet_folder_path = Path(WORKSHEETS_PATH, folder)
                shutil.rmtree(worksheet_folder_path)
            break
        elif user_input.lower() == 'n' or user_input.lower*() == 'no':
            print('Process aborted...........exiting program.')
            break
    return None


def testf(args) -> None:
    """
    Creates a worksheet with one specific function specified in the command line arguments.
    """
    if not args.date:
        args.date = datetime.now().strftime('%m-%d')
    worksheet_path = Path(WORKSHEETS_PATH, args.date, "worksheet.py")
    test_path = Path(WORKSHEETS_PATH, args.date, "test_worksheet.py")


    func = "{}.txt".format(args.function)
    if func not in os.listdir(TEMPLATES_PATH):
        print(f"Unable to find function: {args.function}")
        return
    
    algos = [func]
    _write_worksheet(worksheet_path, algos, args.no_instructions)
    _write_tests(test_path, algos)
    return



def run_tests(args):
    """Runs pytest on the file for the specific date"""

    test_path = Path(WORKSHEETS_PATH, args.date)
    
    if os.path.isdir(test_path):
        # Clears the cache
        pycache_file = Path(test_path, '__pycache__')
        if os.path.isdir(pycache_file):
            shutil.rmtree(pycache_file)
        pytest.main([test_path, "-v"])
    else:
        print('There is no worksheet file for the selected date.')
        print('If you are trying to run pytest on a worksheet that isn\'t today\'s date, run the command: ')
        print('"python main.py test -d <date or folder name you want to test>"')

    return


def _parse_args():

    """ 
    Setup and parse command-line arguments.
    
    Returns:
        args: Dict of parsed args
        keys: ['command', 'date', 'number']

    """

    parser = argparse.ArgumentParser(description='Creates recursion worksheets in python')

    command_help = "'make' creates new worksheet, 'remove' removes all the \
        files inside of the selected dates folder, 'clean' deletes all the \
        worksheets inside of the worksheet folder, 'test' runs the pytest test \
        to check the worksheet."

    parser.add_argument('command', choices=['make', 'remove', 'clean', 'test', 'testf'], default='make', help=command_help)

    date_help = "Date argument for file removal or testing. Takes the date in 'mm-dd' year argument. "
    parser.add_argument('-date', '-d', help=date_help, default=datetime.now().strftime("%m-%d"))

    number_help = "Specifies number of algorithms you want to make on the worksheet.  Defaults to 5 algorithms if not specified.  "
    parser.add_argument('-number', '-n', type=int, default=5, help=number_help)

    no_instructions_help = "If you don't want the commented/doc-string \
        instructions on your worksheet, use the --no-i modifier to create the \
        worksheets with just the functions. \nGenerally this option is for \
        people who already know what the function is asking for and don't want \
            the extra visual clutter."
    parser.add_argument(
            '--no-i',
            '-no-i',
            '--no-instructions', 
            '-no-instructions',
            dest="no_instructions", 
            action="store_true", 
            help=no_instructions_help
        )

    function_help = "If you want to create a worksheet with one specific function, you can use the -f or -function argument and specify the name of the function. The function name should be its stem inside the templates/algorithm folder.\nFor example if you wanted to make a worksheet for the multiply() function, you would use the following command:\n'python make -f karatsuba_multiplication'\n"
    parser.add_argument(
        '-f',
        '-function',
        dest='function',
        help=function_help,
        default=None)

    nsp = Arguments(**vars(parser.parse_args()))

    if '/' in nsp.date or '\\' in nsp.date:
        nsp.date = nsp.date.replace('/', '-').replace('\\', '-')
    
    return nsp


def main() -> None:
    function_dictionary = {
                            'make': make_new_worksheet,
                            'test': run_tests,
                            'clean': clean,
                            'remove': remove_worksheet,
                            'testf': testf 
                            }
    args = _parse_args()
    command = function_dictionary[args.command]
    command(args)


if __name__ == "__main__":
    main()