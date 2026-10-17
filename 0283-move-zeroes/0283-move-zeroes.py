class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        temp=[]
        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])
        
        n2=len(temp)
        for i in range(0, n2):
            nums[i]=temp[i]
        for i in range(n2, n):
            nums[i]=0
        return nums
