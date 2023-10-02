import sys

def gcd(a, b):
    pass

#Создаем тестовые функции
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

#Обращаемся к глобальному окружению
global_dir = dir()

#Создаем функцию, которые ищет все тестовые функции
def find_test_functions():

    name_prefix = '__test_'
    test_functions = []
    for function in global_dir:
        if function.startswith(name_prefix):
            test_functions.append(function)
            
    return test_functions

#Проверяем работоспособность 
for test_function_name in find_test_functions():
    globals()[test_function_name]()
