class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1]))
        c=0
        last=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<last[1]:
                c+=1
            else:
                last=intervals[i]
        return c