class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen_idx={}
        result = 0
        i = j = 0
        for j,c in enumerate(s):
            if c in last_seen_idx:
                i = max(i,last_seen_idx[c]+1) # we dont go backward, last_seen_idx[c]+1 could be from an earlier index (than i), we are sure that the current window is non-repeating, so we jump here to the max of i or next of last seen.
            result = max(result, j - i + 1)
            last_seen_idx[c] = j
        return result
