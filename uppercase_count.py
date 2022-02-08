def upp_letters(text):
    '''Count the number of uppercase starting letters and lowercase letters in each word of the sentence'''
    u=0
    l=0
    word_list=list(text.split())
    for w in word_list:
        if w[0].isupper()==True:
            u = u+1
        else:
            pass
    for w in word_list:
        for i in range(0,len(w)):
            if w[i].islower()==True:
                l=l+1
            else:
                pass
    print('No of uppercase letters: ',u)
    print('No of uppercase letters: ',l)
            
