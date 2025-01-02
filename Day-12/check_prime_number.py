def is_prime():
    number = int(input("enter any number: "))
    if number > 1:
        for i in range(2,number):
            # Check if the number can be divided by the potential prime number
            if number%i==0:
                return False
            # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
        return True
    else:
        return "not prime number"
print(is_prime())