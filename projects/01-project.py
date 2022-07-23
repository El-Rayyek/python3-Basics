## devision the list of numbers to (even numbers list) and (odd numbers list)

numbers_lst = list()
even_lst    = list()
odd_lst     = list()

print("Press 'x' to EXIT and show the list")
print("Enter your numbers:")
while True:
    
    inn = input("")
    if inn == 'x': break
    numbers_lst.append(int(inn))

    
for x in numbers_lst:
    if x % 2 == 0:
        even_lst.append(x)
    else:
        odd_lst.append(x)

print("The Even List is :",even_lst)
print("The Odd List is  :",odd_lst)
print("Good bye ^_^")
