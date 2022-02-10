def smallest_multiple():
  '''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
    
    l=[]
    for i in range(1,21):
      l.append(i)
    
    num = len(l)
    while num>=len(l):
        for n in l:
            if num%n!=0:
                num+=1
                break
            elif num%n==0 and n==l[-1]:
                return num
                break
            else:
                pass
