#### devide the numbers of range on the input (num2)

num1 = int(input("Enter the last number of range  :"))
num2 = int(input("Enter the number you will devide on it :"))

lst = list()
for x in range(num1+1):
    if x % num2 == 0 :
        lst.append(x)

print(lst)
