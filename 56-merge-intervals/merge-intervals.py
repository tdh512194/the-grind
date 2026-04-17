class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0]) # sort by start index
        result = []
        i = 0
        max_ej = -1
        while i < len(intervals):
            si,ei = intervals[i]
            if si > max_ej:
                overlapped = []
                max_ej = ei
                for j in range(i, len(intervals)):
                    sj,ej = intervals[j]
                    if sj > max_ej:
                        break
                    max_ej = max(max_ej,ej)
                result.append([si,max_ej])
            i += 1
        return result
            


