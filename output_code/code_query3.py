class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = 0
        max_len = 0
        seen = {}
        for end in range(len(s)):
            if s[end] in seen and start <= seen[s[end]]:
                start = seen[s[end]] + 1
            else:
                max_len = max(max_len, end - start + 1)
            seen[s[end]] = end
        return max_len
