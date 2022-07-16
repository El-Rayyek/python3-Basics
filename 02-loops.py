'''
#nested loop

x = 0
while x < 5 :
    y = 0

    while y < 3 :
        print(x,y)
        y += 1

    x += 1
    
'''


'''
#Multiplication Table

#1 x 1 = 1
#2 x 2 = 4
#3 x 10 = 30

multi = 1
while multi <= 10 :
    x = 1

    while x <= 10 :
        print(f"{multi} X {x} = {multi*x}")
        x += 1
    multi += 1
'''
'''
#for loop

for x in "mohamed":
    print(x)


#Range

range(4) #0 1 2 3
range(1,5) #1 2 3 4
range(1,11,3) #1 4 7 10

for multi in range(1,4):  #1 2 3
    for x in range(1,11): #1 2 3 4 5 6 7 8 9 10
        print(f"{multi} X {x} = {multi*x}")

'''
'''
#input

x  = input("Enter your input")
print(x)


my_number  = int(input("Enter the scale range :"))

for x in range(1 ,my_number+1 ):
    print(x)

'''

'''
#Control Statment
#break
#continue

for x in range(1,11):
    if x == 6 :
        break
    print(x)
'''

'''
for x in range(1,11):
    if x == 6 :
        continue
    print(x)
    
print("welcome")
'''














