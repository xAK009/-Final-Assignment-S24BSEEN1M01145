def vowels_count():
    vowels=['a','e','i','o','u']
    vowels_counter=0
    input_string=input("Enter your sentence to count Vowels: ")
    lower_string=input_string.lower()
    for vow in lower_string:
        if vow in vowels:
            vowels_counter+=1
    print(vowels_counter)
vowels_count()