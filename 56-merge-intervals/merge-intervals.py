class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        i=0
        j=0
        n=len(intervals)
        while i<n:
            if  not res:
                res.append(intervals[i])
                i+=1
                continue
            if intervals[i][0] <= res[j][1]:
                res[j][0]=min(intervals[i][0],res[j][0])
                res[j][1]=max(intervals[i][1],res[j][1])
                i+=1
            else:
                res.append(intervals[i])
                i+=1
                j+=1
        return res
            