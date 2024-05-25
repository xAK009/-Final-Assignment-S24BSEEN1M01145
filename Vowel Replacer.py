def vowels_replacer():
    vowels=['a','e','i','o','u']
    input_string=input("Enter Your Sentence: ")
    lower_string=input_string.lower()
    replacement=input("Enter Anything You Want To Change The Vowels With: ")
    result=''
    for char in input_string.lower():
        if char in vowels:
            result += replacement
        else:
            result += char
    print("Changed Sentence is : ",result)
vowels_replacer()