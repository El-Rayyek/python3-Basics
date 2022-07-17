#functions
'''
def mysum(x,y):
    print(x+y)

mysum(3,4)
'''

#parameters
'''
    required
    keyword = positional
    default
    variable length
'''
'''
def mysum(x = 0 , y = 0):
    print(x+y)

mysum(10,4)
'''

#function structure
'''
def func_name(parameters):
    func_body : logic
    return target


def mysum(x,y):
    result = x+y
    return result

x = mysum(3,4)
print(f" x = {x}")
'''

# local VS global : Scope
'''
f = 0
print(f)  #0


def do():
    global f
    f = 5   
    print(f)  #5

do()
print(f)  #5
'''

#anonymous function
# mysum = lambda parameters : logic[return]
'''
mysum = lambda x,y : x+y

x = mysum(5,9)
print(x)
'''
# functions examples :
'''

    print()
    type()
    range()
    enumerate()
'''
'''
for index , x in enumerate( range(10,20) ):
    print(index,x)
'''
