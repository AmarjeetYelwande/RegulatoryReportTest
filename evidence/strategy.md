### High level overview:

* Instead of writing multiple tests, I have created one representative test which covers testing duplicate columns and data types of values in report
* Instead of having two tests for testing each of the scenario I have combined them in one as 90 percent of the code
* written for each test is same. Technically we can split the code in two functions but wont make much difference as far as readability is 
* Another advantage of having them in one function in the same file for column names and data type at same time.

### How to extend this test to other scenarios:

* We can test other scenarios by adding respective template and report files in respective folder / make folder hierarchy
* This can be done by either product owner or tester working on this project
* From product point of view I would recommend creating multiple templates instead of all of them in one spreadsheet
* I have renamed column names which match with the columns names from report which are easy to read and helps to map from templates
concerned

### Choice of Language and description of code:

* I have chosen Python as Pandas package in python offers better handling of csv files.
* This solution offers easy maintenance as user simply needs to add template and report files to folders
* For any new type add respective class in CustomTypes.py, and it is ready to use in tests.
* I have used regex pattern matching for validating data types as we can find regex for all types
* There is scope for refactoring the CustomTypes.py class as for some classes code is common ( except regex pattern)
* But I have not done it as separate classes for each type offer good readability

### Continuous integration

* All tests are run as part of Github actions CI workflow. All of them pass
