def recursion_sum(number):
    if number == 1:
        return 1
    else:
        return number + recursion_sum(number-1)
number=int(input("Enter Any Number To Find The Recursion Sum Of: "))
print(recursion_sum(number))