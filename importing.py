from datatypes import *


breakers = ['\n', '9']

version_from_module = get_me_info()
splitted_version_info = version_from_module.split()

version = int(splitted_version_info[0][0])


if version < 3:
    print("Not valid python interpreter")
    # print(version)
else:
    pass
# print(breakers[0])

# Access single element in the list
# breaker = breakers[0]

def split_lists():
    for element in splitted_version_info:
        for breaker in breakers:
            print(element.split(breaker))

# print("This python version is: {}".format(sys.version))

# list_test = [12, 234]
# index = 1
# for on, x in enumerate(list_test):
#     print("arg {}: {}".format(on + 1, x))
    # index = index + 1
    # index += 1


# print('arg {}'.format(list_test[0]))
# print('arg {}'.format(list_test[1]))

# for element in splitted_version_info:
    # for splitted_version_info
#     for breaker in breaker:
    # print(type(element))


# print(adding_odd(3212213132, 2))
# version_from_module >

# I don't know whether add arguments annotations
def divison(arg: int):
    pass

breaker = ['\r', '\n']