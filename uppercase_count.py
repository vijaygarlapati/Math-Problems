def case_letter(text):
    '''Count the number of upper and lowercase letters in a given string'''
    uppercase = 0
    lowercase = 0
    for char in text:
        if char.isupper():
            uppercase +=1
            
        elif char.islower():
            lowercase +=1

        else:
            pass
    print(f'The given string is: {text}')
    print(f'The number of uppercase letters in the above stirng is {uppercase}')
    print(f'The number of lowercase letters in the above stirng is {lowercase}')
