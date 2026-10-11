class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxwater=float('-inf')
        n=len(height)
        mh=max(height)
        l,r=0,n-1
        while l<r:
            maxwater=max(maxwater,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            if mh*(r-l)<maxwater:
                break
        return maxwater