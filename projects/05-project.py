'''A program that takes two numbers from the user
and prints all the numbers that are divisible by
My number is from 0 to 100
'''

while True :
    
    num1 = int(input("Enter frist number :"))
    num2 = int(input("Enter second number :"))

    lst = list()
    for x in range(101):
        if x % num1 == 0 and x % num2 == 0 :
            lst.append(x)

    print(lst)

    complete = input("press x to EXIT or else to complete :")
    if complete == 'x':break
