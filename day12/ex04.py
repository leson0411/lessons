def identify_palindrome(word):
    return word == word[:: -1]


word = input("Enter a string: ").strip().lower()
print(identify_palindrome(word))
