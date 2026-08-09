class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "#".join("^" + s + "$")
        n = len(t)
        p = [0] * n  # array to store palindrome radius
        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

        # Try to expand palindrome centered at i
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

        # If palindrome expands past right, adjust center and right
            if i + p[i] > right:
                center, right = i, i + p[i]

    # Step 2: Find the max length and center
        max_len = max(p)
        center_index = p.index(max_len)
        start = (center_index - max_len) // 2  # convert back to original index
        return s[start:start + max_len]