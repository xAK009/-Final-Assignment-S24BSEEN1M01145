def factorial(number):
    # Factorial of 0 is always 1
    if number == 0:
        return 1
    
    # create an empty string to store result
    result = 1
    
    # Loop from 1 to number and multiply the result by each number
    for i in range(1, number + 1):
        result *= i
    
    # Return the calculated factorial
    return result
number=int(input("Enter Any Number To Find The Factorial Of: "))
print("The Factorial Of",number,'=',factorial(number))