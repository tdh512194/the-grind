class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = ""
        curr = ""
        br = False
        while not br:
            prefix = prefix + curr
            # if len(strs[0]) == 0:
            #     return ""
            # just a tedious problem, need to check this twice
            if i > len(strs[0])-1:
                return prefix
            curr = strs[0][i]
            for c in strs:
                if i > len(c)-1:
                    br = True
                    return prefix
                if c[i]!=curr:
                    br = True
                    break
            i += 1
        return prefix