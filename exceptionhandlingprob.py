def ask():
'''Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.'''
    
    while True:
        try: 
            n = int(input("Enter the number: "))
            sqr = n**2
            print("The square of the given number is: {}".format(sqr))
            break
        except:
            print("An error occured and pl try again")
            continue
            
