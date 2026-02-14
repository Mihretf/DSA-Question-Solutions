class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        for i in range(len(nums)):
            counter=0
            for j in range(len(nums)):
                if i!=j and nums[j] < nums[i]:
                    counter +=1
            count[nums[i]] = counter
        
        results= [count[num] for num in nums]
        return results
        
