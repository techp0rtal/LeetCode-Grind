

"""
Option 1: Less efficient. Easy method
This is my first attempt. It's not efficient since it tries to compare positive to negative numbers, which is a waste
since the negative sign - will obviously make them not match. Better to eliminate negative numbers immediately by
doing an immediate return false.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_number = str(x)
        reversed_number = reversed_number[::-1]


        if str(x) == reversed_number:
            return True

        else:
            return False
"""
# Now time for chatgpt one line of code....
"""
Option 1 (improved): one line of code. Still relies on converting to string though which is kind of cheating.

class Solution:
    return str(x) == str(x)[::-1]

Why have if statements if you don't need them?

"""
# Now time for option 2, the math method.

#class Solution:

# This was my method. A little different from the AI's approach, but same logic. Only caveat/risky thing is
# I compare an int to a float, which could be tricky in other languages (easy to remedy through a simply conversion though)

def isPalindrome(x) -> bool:
    if x < 0:
        return False
    changing_num = x
    last_digit = x % 10
    reversed_number = 0
    reversed_number += last_digit

    while changing_num > 0:
        changing_num //= 10
        last_digit = changing_num % 10
        reversed_number = reversed_number * 10 + last_digit
    reversed_number = reversed_number / 10
    print(reversed_number)
    return reversed_number == x

isPalindrome(121)

# Chat GPT's version:
"""

def isPalindrome(self, x: int) -> bool:
    if x < 0:  # Negative numbers are never palindromes
        return False
    
    original = x
    reversed_number = 0

    while x > 0:
        digit = x % 10  # Get the last digit
        reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
        x //= 10  # Remove the last digit from x

    return original == reversed_number  # Compare original number with reversed number




"""