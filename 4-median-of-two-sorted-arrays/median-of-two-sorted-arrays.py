class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergel=nums1+nums2
        mergel.sort()
        n=len(mergel)
        if n%2!=0:
            return(mergel[(n+1)//2-1])
        else:
            return((mergel[n//2-1]+mergel[n//2])/2)