'''
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return ""

        longest = 0
        center = 0
        for i in range(len(s)):
            length = max(self.getLongestLen(s, i, i), self.getLongestLen(s, i, i+1))
            if length > longest:
                longest = length
                center = i
        if longest % 2 == 0:
            return s[(center - longest//2 + 1):(center + longest//2 + 1)]
        else:
            return s[(center - longest//2):(center + longest//2 + 1)]


    def getLongestLen(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return end - start - 1

'''
遍历字符串，以每个位置为中心向两侧扩展，寻找以该位置为中心的最长回文串
注意回文串长度可以是奇数（一个中心）也可以是偶数（两个中心）
注意getLongestLen返回的值应为end - start - 1
'''
