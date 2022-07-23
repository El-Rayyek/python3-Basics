# calculate length of words from sentence without repeat


sentence = input("Enter your sentence :")

sentence = sentence.split()

lst = list()

for x in sentence:
    if x not in lst:
        lst.append(x)
        
print("The list of words without Repeat",lst)
print("The number of words without Repeat is : ",len(lst))
    
