__author__ = "Adam Jarzebak"
__copyright__ = "Copyright 2018, Adam Jarzebak"
__credits__ = []
__license__ = "MIT"
__maintainer__ = "Adam Jarzebak"
__email__ = "adam@jarzebak.eu"
"""
This file consist of examples or set of comments and descriptions related to the topic of python's annotation
for variables data types. In order to see examples fully working, please update you PyCharm editor.
"""


# At IDE level. Syntax for Variable Annotations. Specifying data type for an input.
# Version < 3.6 does not accept a variable annotation.
def multiply(factor: int):
    """
    Example where input argument has specified variable annotation.
    This example is showing how to cast variable. And assert in order to check for any error at the early stage.
    :param factor:
    :return: results: int
    """
    # This will print a data type of this variable e.g. int, float, string.
    print(type(factor))
    # Casting variable into another data type (Casting is when you convert a variable value from one type to another.)
    factor_var = int(factor)
    # Check if data type is what we expect to be.
    assert type(factor_var) == int

    # Return function can return a single variable as well as execute function.
    # Return causes the function to stop executing and hand a value back to whatever called it.return causes the
    # function to stop executing and hand a value back to whatever called it."
    return int(factor_var * 23.233223)


# This example present lack of variable annotations. At this stage variable will not be highlighted in case of
# other data type of variable was provided. However, this examples has extended usage of assert function in python.
def multiply_1(factor):
    """
    Example without using annotations. Better example of how to use assert.
    :param factor:
    :return: results: int
    """
    assert type(factor) is not int or type(factor) is not float, "MAMMA MIA!"
    # Above example shows that we need that type of variable factor has to either int or float.
    # Otherwise will print out an extra annotation.

    results = factor * factor * factor

    return results
