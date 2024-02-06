'''
# palindrome_lab_template
Palindrome Lab  
This is an independent lab. Code and solutions must not be shared among classmates. You may ask me questions.

A palindrome is a word with the same letters forward as backwards. 

Examples of palindromes:  
kayak  
Hannah  
racecar

In this lab:
1. Ask the user for input text
2. Complete the function palindrome() to determine if the text is a palindrome.
3. If the text is a palindrome, return True else return False.

Notes
1. An empty string is not a palindrome
2. Case does not matter
3. White spaces should not be taken into consideration
'''

#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    
    if word.isspace():
        return False

    word = word.upper()
    word = word.replace(' ', '')
    
    for i in range(len(word)//2):
        if not(word[i] == word[((i+1) * (-1))]):
            return False
    
    return True

#YOUR CODE GOES HERE

imp = input()
print(palindrome(imp))