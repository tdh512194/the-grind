class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        j = 0
        result = 0
        tmp = 0
        while j < len(s):
            cur = s[j]
            if j + 1 == len(s):
                result += symbol[cur]
                break
            nex = s[j+1]
            if ( symbol[cur] < symbol[nex]):
            #     ((cur == 'I') and (nex in ('V', 'X')))
            #     or ((cur == 'X') and (nex in ('L', 'C')))
            #     or ((cur == 'C') and (nex in ('D', 'M')))
            # ):
                result += symbol[nex] - symbol[cur]
                j = j + 2
            else:
                result += symbol[cur]
                j = j + 1
        return result




