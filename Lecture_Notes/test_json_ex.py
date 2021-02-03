''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 2: JSON, Unit Testing, Version Control 

           Unit Tests in Python  
           
In this script, the Python "unittest" library will be used to write unit tests
for simple functions.

Definition: "Unit Tests" are designed to test small components (ex: individual
functions) of your code. They should demonstrate that things that are expected
to work actually do work, and things that are expected to break raise appropriate
errors. The Python "unittest" unit testing framework supports test automation, 
set up and shut down code for tests, and aggregation of tests into collections. 
It is built into the Python Standard Library (PSL) and can be imported directly. 


Let's use the functions defined in "json_ex.py" to understand how the 
"unittest" library can be used for unit testing in Python. 

NOTE: IT IS COMMON PYTHON CONVENTION TO NAME A TEST FILE THE SAME NAME AS
THE SCRIPT YOU ARE TESTING, BUT WITH THE "test_" PREFIX ADDED AT THE BEGINNING'''
           
         
import unittest # Import the "unittest" framework
from json_ex import check_char_count,check_char_type,compare_first_char # Import the function we want to test

class TestJsonEx(unittest.TestCase): # Create class and subclass for testing our application
    
    # Define "test_check_char_count()" method for testing a specific function:

    def test_check_char_count(self):
        
        '''Write tests to check that certain calls to our function return expected results
        Note that the test will only pass if the two parameters passed to 
        that method are equal. The script can be executed to run the tests: '''
        
        self.assertEqual(check_char_count('AA'),'AA count passes')
        self.assertEqual(check_char_count('AAA'), 'AAA count FAILS')
        
        ''' WE can also look at edge cases. Previously, we sent an "int" to 
        this function, and it raised a "TypeError". This is good and expected
        behavior. We can use the "assertRaises()" method to make sure that 
        errors are properly generated '''
        
        self.assertRaises(AssertionError,check_char_count, 1)
        self.assertRaises(AssertionError,check_char_count, 2.5)
        self.assertRaises(AssertionError, check_char_count, True)
        self.assertRaises(AssertionError, check_char_count, ['AA', 'BB'])


        ''' Now, each of the tests run ok, however, we can still modify our function
        in "json_ex.py" to handle edge cases better. We don't want to pass anything sent
        to this function other than a two-character string. So, an "assert" statement
        will be added inside the function definition to make sure that the argument is 
        always a string. Namely, the statement "assert isinstance(mystr,str), 
        'Input to this function should be a string"'''  


    ''' The check_char_type()" method is already pretty failsafe because it
    is using built-in string methods "isupper()" and "isalpha()" to do the 
    checking. These already have internal error handling, so we can probably 
    get away with a few simple tests and no changes to our original function. '''
    
    # Define "test_check_char_type()" method for testing a specific function:

    def test_check_char_type(self):
         self.assertEqual(check_char_type('AA'), 'AA type passes')
         self.assertEqual(check_char_type('Aa'), 'Aa type FAILS')
         self.assertEqual(check_char_type('aa'), 'aa type FAILS')
         self.assertEqual(check_char_type('A1'), 'A1 type FAILS')
         self.assertEqual(check_char_type('a1'), 'a1 type FAILS')
         
         ''' The "isupper()" and "isalpha()" methods only work on strings. If 
         they are tried on any other datatype, they will automatically return 
         an "AttributeError". '''
         
         self.assertRaises(AttributeError, check_char_type, 1)
         self.assertRaises(AttributeError, check_char_type, True)
         self.assertRaises(AttributeError, check_char_type, ['AA', 'BB'])
         
    # Define "test_compare_first_char()" method for testing a specific function:

    def test_compare_first_char(self):
         self.assertEqual(compare_first_char('AK','Alaska'), \
                          'AK first character agrees with the state name')
         self.assertEqual(compare_first_char('LL','Illinois'),\
                          'LL first character does not agree with the state name')
         self.assertEqual(compare_first_char('C0','Colorado'), \
                          'C0 first character agrees with the state name')
         self.assertEqual(compare_first_char('KAN','Kansas'), \
                          'KAN first character agrees with the state name')
         self.assertEqual(compare_first_char('Ms','Mississippi'), \
                          'Ms first character agrees with the state name')
         
         ''' The "isupper()" and "isalpha()" methods only work on strings. If 
         they are tried on any other datatype, they will automatically return 
         an "AttributeError". '''
         
         
         self.assertRaises(IndexError, compare_first_char,'AA', '')
         self.assertRaises(IndexError, compare_first_char,'', 'AA')
         self.assertRaises(IndexError, compare_first_char,'', '')
         self.assertRaises(TypeError, compare_first_char,[1,2])
         self.assertRaises(TypeError, compare_first_char, (True,False))
         self.assertRaises(TypeError, compare_first_char, [['AA', 'BB'],['BB','AA']])

 # Wrap the "unittest.main()" function at the bottom so the script can be called: 
     
if (__name__ == '__main__'):
    unittest.main()