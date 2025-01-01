# Recursive Worksheet Creator - Creates a python file with random recursive 
# Algorithms to practice along with tests via pytest

import argparse
from datetime import datetime
import os
from pathlib import Path
import pytest
import random
import shutil


TEMPLATES_PATH = Path((os.path.dirname(__file__)), "templates", "algorithms")
POSSIBLE_ALGORITHMS_PER_PAGE = len(os.listdir(TEMPLATES_PATH))
WORKSHEETS_PATH = Path((os.path.dirname(__file__)), "worksheets")


def _pick_random_algorithms(number: int):
    algorithms = os.listdir(TEMPLATES_PATH)
    random_set = set()
    while len(random_set) < number:
        random_set.add(random.choice(algorithms))
    return random_set


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


def _write_worksheet(worksheet_path, algorithms, no_instructions):
    # Write Heading of worksheet and clear worksheet if it already exists. 
    with open(worksheet_path, 'w') as fout:
        fout.write(f'# Recursion Worksheet: {datetime.now().strftime("%m-%d")}\n\n')
    
    while len(algorithms) > 0:
        current_algorithm = algorithms.pop()

        # Read and store algo from template
        if no_instructions == False:
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


def make_new_worksheet(date, number, no_instructions):
    # Creates a path to a directory with today's date 
    if date is None:
        date = datetime.now().strftime('%m-%d')
    path = Path((os.path.dirname(__file__)), "worksheets", date)
    if path.exists() is False:
        os.makedirs(path)

    # Picks Random algorithms based on argument number
    algos_set = _pick_random_algorithms(number)
    test_algos = list(algos_set)

    # Paths to the new worksheet and test files
    worksheet_path = Path(path, "worksheet.py")
    test_path = Path(path, "test_worksheet.py")

    # Write the worksheet and pytest file in same directory
    _write_worksheet(worksheet_path, algos_set, no_instructions)
    _write_tests(test_path, test_algos)

    return 


def remove_worksheet(date, number, no_instructions) -> None:
    folder_to_remove = Path(WORKSHEETS_PATH, date)

    if os.path.isdir(folder_to_remove):
        while True:
            user_input = input(f'Are you sure you want to remove the directory{date}? y/n  ')
            if user_input.lower() == 'y' or user_input.lower() == 'yes':
                print(f'.....Removing {folder_to_remove}...\n')
                shutil.rmtree(folder_to_remove)
                print(f'Successfully removed the {date} folder')
                break
            elif user_input.lower() == 'n' or user_input.lower == 'no':
                print('Process aborted........ exiting program. ')
    return


def clean(*args) -> None:
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


def run_tests(date, number, no_instructions):
    """Runs pytest on the file for the specific date"""

    test_path = Path(WORKSHEETS_PATH, date)
    
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


def _parse_args() -> dict:

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

    parser.add_argument('command', choices=['make', 'remove', 'clean', 'test'], default='make', help=command_help)

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

    args = parser.parse_args()
    # reformats dates incase user puts '/' or '\' which would return an error
    if '/' in args.date or '\\' in args.date:
        args.date = args.date.replace('/', '-').replace('\\', '-')
    
    return args


def main() -> None:
    function_dictionary = {
                            'make': make_new_worksheet,
                            'test': run_tests,
                            'clean': clean,
                            'remove': remove_worksheet 
                            }
    args = _parse_args()
    
    command = function_dictionary[args.command]
    command(args.date, args.number, args.no_instructions)


if __name__ == "__main__":
    main()