# TODO return examples
import sys


def get_me_info():
    # print("This python version is: {}".format(sys.version))
    return sys.version

def adding_odd(a, b):
    assert type(a) is int and type(b) is int, 'Not an integer'
    return a + b


def copy():
    print('asdsad')


def paste():
    a = 1 +12


if __name__ == '__main__':
    print(adding_odd(1, 2))
