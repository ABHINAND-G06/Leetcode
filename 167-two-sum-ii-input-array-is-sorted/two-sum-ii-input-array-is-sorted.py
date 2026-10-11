class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n=len(numbers)
        # l,r=0,n-1
        # while l<r:
        #     if numbers[l]+numbers[r]>target:
        #         r-=1
        #     elif numbers[l]+numbers[r]<target:
        #         l+=1
        #     else:
        #         return[l+1,r+1]
        hmap={}
        for i in range(n):
            c=target-numbers[i]
            if c in hmap:
                return[hmap[c]+1,i+1]
            hmap[numbers[i]]=i
        return[-1,-1]        