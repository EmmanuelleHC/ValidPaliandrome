import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert all uppercase letters to lowercase
        s = s.lower()

        # Remove alphanumeric characters and underscores using regular expressions
        s = re.sub(r'[\W_]+', '', s)
        
        # Check if the modified string is a palindrome
        return s[:] == s[::-1]
        
