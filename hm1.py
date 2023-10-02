import sys

def gcd(a, b):
    pass

def __test_gcd():
    value = gcd(12, 32)
    print("check")

    pass

def __test_qwerty2():
    print('qwerty2')
    pass

def __test_aaaaaaaa():
    print('aaaaaa')
    pass

def __test_bbbbbbb():
    print('aaaaaa')
    pass

global_dir = dir()
def find_test_functions():

    name_prefix = '__test_'
    test_functions = []
    for function in global_dir:
        if function.startswith(name_prefix):
            test_functions.append(function)
            
    return test_functions

for test_function_name in find_test_functions():
    globals()[test_function_name]()
