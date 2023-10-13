def count_vowels_consonants(input_string):
    vowel_count = 0
    consonant_count = 0
    vowels = "AEIOU aeiou"

    for char in input_string:
       if char.isalpha():
           if char in vowels:
               vowel_count += 1

           else:
               consonant_count += 1
    return vowel_count, consonant_count

def reverse_string(input_string):
    return input_string[::-1]

def remove_space(input_string):
    return input_string.replace(" ", " ")


while True:
    user_input = input("Enter string (or 'quit' to exit): ").strip()
    if user_input.lower() == "quit":
        break

    print("\nMenu:")
    print("1. Count characters")
    print("2. Reverse String")
    print("3. Remove spaces")
    print("4. Quit")

    choice = input("Enter your choices from 1-4 :")

    if choice == "1":
        result = count_vowels_consonants(user_input)
        print(f"vowels: {result[0]} consonants: {result[1]}")
    elif choice == "2":
        reversed_str = reverse_string (user_input)
        print(f"reversed string: {reversed_str}")
    elif choice == "3":
        no_space_str = remove_space(user_input)
        print(f"String without spaces: {no_space_str}")
    elif choice == "4":
        break
    else:
        print("Please try again. Enter from  choices 1-4.")





















