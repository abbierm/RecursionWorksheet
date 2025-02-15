
# Recursion Worksheet Generator


## Description

 Creates a python file with empty recursive functions (with instructions) and tests them via pytest.

 Inside of the RecursionWorksheet folder in the terminal you can run the command:

        python main.py make -n 3

This will create files "worksheet.py" and "test_worksheet.py" inside of the "worksheets\MM-DD\" directory. The worksheet will have 3 empty functions with instructions on what they are expected to do. 

 ![blank example worksheet](static/example_blank_worksheet.jpg)


Once the user is done writing the algorithms, they can test their answers by running the following command:

        python main.py test
 
The terminal will print the pytest results

![example command line results](static/example_test_results.jpg)

 ## Requirements

- python 
- pytest 

 ## Basic Usage

- Download or clone repository on your computer via the green <> Code dropdown menu. 


- pip install pytest inside of virtual environment  


        pip install pytest

- Inside of the RecursionWorksheet directory in the terminal or command line run the following code to create a new worksheet with 10 different algorithms. 

        python main.py make -n 10 

- Inside of the worksheet/mm-dd folder there should be two new files:
    1. worksheet.py
    2. test_worksheet.py

- The worksheet.py file will have the the functions defined with a short description detailing what algorithm the function should complete. 

     
- Once you are done writing out the answers you can test your worksheet by running the following command  

        python main.py test


## Details

#### The program has four different basic commands. If you run the main.py script without one of these four command line arguments then the program will return with an error message.

1. "make" - Creates a new worksheet.py file inside of the worksheet/MM-DD directory along with a test_worksheet.py file used to test. 

2. "test" - Runs pytest and prints results to the terminal. 

3. "clean" - Removes all of the tests inside of the worksheets/ directory

4. "remove" - Removes one worksheet


#### There are three optional command line arguments. If you don't include these the program will assume the default values. 

1. "-n" : Specify the number of worksheets to create.  The default is set at 5. "make" is the only command that uses the -n command.

2. "-d" : Specify the date (or what you want to name the folder). The default is set at the current date.

3. "--no-i" : Tells the program to generate a worksheet without the docstring instructions. Without including this argument the worksheet will have instructions.


## Examples commands :


#### Create a worksheet with 7 different recursive algorithms.


        python main.py make -n 7


#### Test a worksheet you created on 12-11.


        python main.py test -d 12-11


#### Create a worksheet with 3 different algorithms in a folder named "i_love_corgis"

        python main.py make -n 3 -d i_love_corgis

#### Test worksheet from previous example 

        python main.py test -d i_love_corgis

#### Remove the worksheet from the i_hate_recursion folder

        python main.py remove -d i_love_corgis

#### Permanently delete all of the files and worksheets in the worksheets folder

        python main.py clean


#### Create a worksheet with 12 different algorithms without the docstring instructions.

       python main.py -make -n 12 --no-i
