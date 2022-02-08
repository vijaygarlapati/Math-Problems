def upp_letters(text):
    '''Count the number of supper case starting letters in each word of the sentence'''
    c=0
    l=list(text.split())
    for w in l:
        if w[0].isupper()==True:
            c = c+1
        else:
            pass
    return c
            
