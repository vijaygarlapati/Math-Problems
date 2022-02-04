#if we list all the natural numbers below 10 which are multilples of 3 or 5, we get 3,5,6,9. 
#The sume of these multiples is 23. Find the sume of all the multiples of 3 or 5, below 1000.

n=int(input("Enter the number"))
l=[]
sum=0
for i in range(1,n):
    if i%3==0 or i%5==0:
        l.append(i)
    else:
        continue
for j in range(0,len(l)):
    sum = sum+l[j]
print(sum)

  

