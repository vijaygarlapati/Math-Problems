def mult_three_five(n):
    ''' sum of multiples of 3 or 5 below the given number'''
    l=[]
    sum=0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            l.append(i)
        else:
            pass
    for j in l:
        sum = sum + j
    return sum



  

