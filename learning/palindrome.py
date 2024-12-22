def is_palindrome(sequence):
    return sequence == sequence[::-1]


def check():
    string_palin = input("Enter a String to check if thats a palindrome or not:")
    if((is_palindrome(string_palin)) == True):
        print("Its a palindrome !!!")
    else:
        print("No sorry its not a palindrome !!!")

check()