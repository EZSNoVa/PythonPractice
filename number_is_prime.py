#determine is number is prime 
print("CHECK IF NUMBER IS PRIME")
number = int(input("Enter a number: "))

def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
