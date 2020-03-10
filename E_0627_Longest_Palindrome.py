'''
Given a string which consists of lowercase or uppercase letters, find the length
of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
'''

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        ans = 0
        letters = {}
        remaining = 0

        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        for char in letters:
            ans += letters[char] // 2 * 2
            remaining += letters[char] % 2

        if remaining > 0:
            ans += 1

        return ans

'''
思路：数一下每个字母有多少个，2的倍数均可组成回文，外加正中间可以存在一个单个字母
'''
