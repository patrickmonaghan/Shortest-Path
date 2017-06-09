# Intro
This is a code challenge I undertook in 2015 for an assessment centre

# Building and Running

To run this, execute 'python2.7 hierarchy.py [INPUT_FILENAME] [START] [END]'
For example, to find the path between Batman and Super Ted in the superheroes.txt 
file, execute 'python2.7 hierarchy.py superheroes.txt "Batman" "Super Ted"'

# Testing

There are 12 unit tests. To execute the unit tests, run 'python unit_tests.py'

The tests are as follows:
* SolutionCheck.testSolutionExampleWorks: Check that the example given in the PDF works
* SolutionCheck.testSolutionWorks: Checks that another example works
* SanityCheck.testCaseCheck: Check that given employee names are not case sensitive.
* SanityCheck.testTrailingLeadingSpace: Check that trailing and leading spaces in specified names are ignored
* SanityCheck.testMultipleSpaces: Check that multiple spaces in specified names are ignored. For example, "Black     Widow" would be treatd as "Black Widow"
* SanityCheck.testMultipleNames: Check that multiple names (but with unique IDs) can be used in finding a path. For example, Minion (1) -> Minion (2)
 
* StabilityCheck.testNoPathFound: Checks that the program gracefully handles when no path is found
* StabilityCheck.testExtendedGraph: Checks that the program works with a bigger dataset
* testInverseSearch: Checks that the graph can search in any direction. For example, if the start node is on the right and the end node is on the left, a path can still be found
* testInvalidManagerFile: Check that providing a file with an invalid employee ID is handled properly

# Documentation

Doxygen documentation is available for access under doxygen/index.html