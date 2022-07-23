### Game (Collect The Last Projects in One Game) by OOP programming 



class Game:
    def __init__(self):
        while True:
            print('''

Welcome in our Game
Please Choose one of five Games :
            Press 1 ==> devision the list of numbers to (even numbers list) and (odd numbers list).
            press 2 ==> calculate length of words from sentence without repeat .
            press 3 ==> make a range from 0 to input of user number.
            press 4 ==> devide the numbers of range on the input (number2).
            press 5 ==> takes two numbers from the user
                        and prints all the numbers that are divisible by
                        My number is from 0 to 100 .
            press 'x' ==> EXIT
''')
            choose_user = input("Enter The Number of Game :")
            if choose_user == 'x':
                print("Good Bye ^_^")
                break
            if int(choose_user) == 1:
                self.dev_list()
                complete = input('''
Do You Want To Continue Playing ?
        Enter Y for (yes) / X for (No)
''')
                if complete.lower() == 'x' :
                    print("Good Bye ^_^")
                    break
                else : continue
            if int(choose_user) == 2:
                self.calc_len_words()
                complete = input('''
Do You Want To Continue Playing ?
        Enter Y for (yes) / X for (No)
''')
                if complete.lower() == 'x' :
                    print("Good Bye ^_^")
                    break
                else : continue
            if int(choose_user) == 3:
                self.rng_frm_0_input()
                complete = input('''
Do You Want To Continue Playing ?
        Enter Y for (yes) / X for (No)
''')
                if complete.lower() == 'x' :
                    print("Good Bye ^_^")
                    break
                else : continue
            if int(choose_user) == 4:
                self.dev_nums_on_input()
                complete = input('''
Do You Want To Continue Playing ?
        Enter Y for (yes) / X for (No)
''')
                if complete.lower() == 'x' :
                    print("Good Bye ^_^")
                    break
                else : continue
            if int(choose_user) == 5:
                self.nums_dev_0to100()
                complete = input('''
Do You Want To Continue Playing ?
        Enter Y for (yes) / X for (No)
''')
                if complete.lower() == 'x' :
                    print("Good Bye ^_^")
                    break
                else : continue
            
    def dev_list(self):
        numbers_lst = list()
        even_lst    = list()
        odd_lst     = list()

        print("Press 'x' to show the lists")
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
        


    def calc_len_words(self):
        sentence = input("Enter your sentence :")

        sentence = sentence.split()

        lst = list()

        for x in sentence:
            if x not in lst:
                lst.append(x)
                        
        print("The list of words without Repeat",lst)
        print("The number of words without Repeat is : ",len(lst))
        

    def rng_frm_0_input(self):
        number = int(input("enter the numper to do the range : "))

        for x in range(number +1):
            print(x)
        
        
    def dev_nums_on_input(self):
        num1 = int(input("Enter the last number of range  :"))
        num2 = int(input("Enter the number you will devide on it :"))

        lst = list()
        for x in range(num1+1):
            if x % num2 == 0 :
                lst.append(x)

        print(lst)
        
    def nums_dev_0to100(self):
        num1 = int(input("Enter frist number :"))
        num2 = int(input("Enter second number :"))

        lst = list()
        for x in range(101):
            if x % num1 == 0 and x % num2 == 0 :
                lst.append(x)

        print(lst)

                                            
g = Game()












