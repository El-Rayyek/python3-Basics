#OOP Calculate
'''
class calculate:

    def sum(self,x,y):   #method
        return x+y
    
    def mul(self,x,y):   #method
        return x*y
    
    def __init__(self , name,x,y):  #constructor
        print(f"welcome {name}")
        print(self.sum(x,y))
        


c1 = calculate('mohamed',4,5)




s = c1.sum(3,4)
l = c1.mul(3,4)

print(f"sum = {s} , multi = {l}")
'''


# OOP Student

'''
    - add student : name , welcome message
    - add mark of student
    - get avg marks
'''    
'''
class Student:
    def __init__(self,name):
        print(f"Welcome {name}")
        self.marks = []

    def get_mark(self,mark):
        self.marks.append(mark)

    def get_avg(self):
        return sum(self.marks)/len(self.marks)


s1 = Student('mohamed')

s1.get_mark(90)
s1.get_mark(40)
s1.get_mark(80)
s1.get_mark(30)
s1.get_mark(70)

print(s1.marks)
print(s1.get_avg())

s2 = Student('ahmed')

s2.get_mark(60)
s2.get_mark(40)
s2.get_mark(80)
s2.get_mark(20)
s2.get_mark(10)

print(s2.marks)
print(s2.get_avg())
'''
