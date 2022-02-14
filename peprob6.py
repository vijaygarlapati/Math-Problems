#Find the difference between square of sum of all hundred natural numbers and sum of squares of hundred numbers

class DiffSquares():
    def __init__(self):
        pass

    def diff(self):
        n = int(input("Enter the number: "))
        sum1=0
        sum2=0
        for num in range(1,n+1):
            sum1 = sum1+num**2
        for num in range(1,n+1):
            sum2 = sum2+num
    
        if (sum2**2)>sum1:
            return ((sum2**2) - sum1)
        else:
            return (sum1 - (sum2**2))

difference = DiffSquares()
print(difference.diff())






        
