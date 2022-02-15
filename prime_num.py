#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
 
num = 3
prime_numbers = [2]

prime_num = True

while prime_num:
    for n in range(2,num):
        if num%n==0:
            num+=2
            continue
        elif num%n!=0:
            if n == num-1:
                prime_numbers.append(num)
                num+=2
                continue
            else:
                pass
    if len(prime_numbers)>10001:
        print(prime_numbers[10000])
        break
