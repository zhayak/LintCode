'''
For a given source string and a target string, you should output the first
index(from 0) of target string in source string.
If target does not exist in source, just return -1.
'''

class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: an index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        ls = len(source)
        lt = len(target)

        for i in range(ls - lt + 1):
            match = True
            for j in range(lt):
                if source[i + j] != target[j]:
                    match = False
                    break
            if match:
                return i

        return -1

'''
注意i的取值范围是range(ls - lt + 1)
'''
