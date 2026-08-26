class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = 0
        ones = 0
        ans = ""
        for r in range(n):
            if s[r] == '1':
                ones += 1
            while ones == k:
                while s[l] == '0':
                    l += 1
                curr = s[l:r + 1]
                if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                    ans = curr
                ones -= 1
                l += 1
        return ans