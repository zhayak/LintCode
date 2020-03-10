'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        if s is None:
            return False

        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True

'''
使用两个指针分别指向头尾，往中间移动
注意内层while的条件里也要加start < end。end初始值为len(s)-1，不要忘记-1
'''
