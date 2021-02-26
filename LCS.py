import functools
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        @functools.lru_cache(None)
        def LCS(n,m):
            if n== 0 or m==0:
                return 0
            if text1[n-1]==text2[m-1]:
                return 1+LCS(n-1,m-1)  
            else:
                 return max(LCS(n-1,m),LCS(n,m-1))
        
        return LCS(n,m)

obj = Solution()
print(obj.longestCommonSubsequence('abcde','abce'))
