class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        seen_substrings = set()
        max_length = len(s) - 1
        
        while max_length > 0:
            seen_substrings.clear()
            for start in range(len(s) - max_length + 1):
                end = start
                current_substring = s[end : end + max_length]
                if current_substring in seen_substrings:
                    return max_length
                seen_substrings.add(current_substring)
            max_length -= 1
        return 0