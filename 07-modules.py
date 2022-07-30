
#map
'''
names = ['mohamed','ahmed','ayman']

def len_name(x):
    return len(x)

my_len_name = map(len_name,names)

print(list(my_len_name))



my_len_name = map(lambda x : len(x),names)
print(list(my_len_name))
'''
#------------------------
#filter
'''
numbers = [2,55,67,2545,100,455,3000,34,556]

def my_filter(x):
    if x > 500:
        return True
    else:
        return False

filter_numbers = filter(my_filter,numbers)
print(list(filter_numbers))
'''
#---------------------------
#reduce
'''
import functools
numbers = [2,55,67,2545,100,455,3000,34,556]

def mysum(x,y):
    return (x+y)*2

print(sum(numbers))
ms = functools.reduce(mysum,numbers)
print(ms)
'''
#str join
'''
names = ['mohamed','ahmed','ayman']

names = ' '.join(names)
print(names)
'''
'''
name = ',,,,,,,,,   mohamed ,,,,,,,,,,,,         ayman ,,,,      sherrif     ,,, '
name = name.replace(',','').split()
print(name)
'''

#exception handling
'''
from distutils.log import error
from logging import exception


try:
    age = int(input('Enter Your Age :'))
    age = 10/age
    print(f"your age is {age}")

except Exception as ex :
    print('please Enter number and > 0')
    print(ex)
else :     # at no exception
    print('try play')

finally :  # at every case
    print('at finally')
'''