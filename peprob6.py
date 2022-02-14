#Find the difference between square of sum of all hundred natural numbers and sum of squares of hundred numbers

class DiffSquares():
    def __init__(self):
        pass

    def diff(self):
        sum1=0
        sum2=0
        for num in range(1,101):
            sum1 = sum1+num**2
        for num in range(1,101):
            sum2 = sum2+num
    
        if (sum2**2)>sum1:
            print((sum2**2) - sum1)
        else:
            print(sum1 - (sum2**2))

difference = DiffSquares()
print(difference.diff())






        
