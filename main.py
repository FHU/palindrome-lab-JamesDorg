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
I. Ask the user for input text
II. Complete the function palindrome() to determine if the text is a palindrome.
III. If the text is a palindrome, return True else return False.


Notes
i. An empty string is not a palindrome
ii. Case does not matter
iii. White spaces should not be taken into consideration
yay
'''

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

if __name__ == '__main__':
    
    imp = input()
    print(palindrome(imp))
