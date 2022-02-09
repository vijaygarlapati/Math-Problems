def palindrome(s):
    #Check the given word or phrase is palindrom or not
    
    #Remove Spaces if any in a phrase
    
    s.replace(' ','')
    return s == s[::-1]
