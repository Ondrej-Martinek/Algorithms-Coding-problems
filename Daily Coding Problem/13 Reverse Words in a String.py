'''Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "The cat in the hat"
Output: "ehT tac ni eht tah"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.'''

class Solution:
    def reverseWords(self, string):
        return ' '.join(''.join(letter for letter in reversed(word)) for word in string.split())

string = "The cat in the hat"

print(Solution().reverseWords(string))
