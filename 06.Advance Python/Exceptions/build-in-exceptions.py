# https://docs.python.org/3/library/exceptions.html


# AttributeError
class MyClass:
    def __init__(self):
        self.my_property = 5

x = MyClass()
print(x.missing_variable)
print(x.my_property)


# ImportError
import my_awesome_module

# KeyError
my_dict = {'x': 5, 'y': 10}
print(my_dict['z'])


# RunTimeError

# TypeError
int([])

# ValueError
int('a')


# IOError
open('my_file.txt', 'r')
