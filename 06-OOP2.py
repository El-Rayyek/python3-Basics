# Encapsulation : self
# Inheritance
'''
class Calc:
    def __init__(self,name):
        print(f"welcome {name}")

    def sum(self,x,y):
        return x+y

    def mul(self,x,y):
        return x*y

class SciCalc(Calc):
    def power(self,x,y):
        return x**y


C1 = SciCalc('mohamed')
print(C1.sum(5,9))
print(C1.mul(5,9))
print(C1.power(5,9))
'''
#----------------------------------------------
# Multi Inheritance
'''
class A:                # <== Polymorphism
    def do(self):
        print("In A")

class B(A):
        pass

class C():              # <== Polymorphism
    def do(self):
        print("In C")

class D(B,C):
        pass
    
        
dv = D()
dv.do()
print(D.mro())
'''


# Parent class = Super class = Main class     : class Calc
# Child class  = Sub class   = Derived class  : class SciCalc





