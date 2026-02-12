class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n= len(nums)
        seen= set()
        duplicate = -1 #simple placeholder
        total_count = 0 # initial count

        expected_count = n * (n+1) // 2

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            total_count+=num
        
        missing= expected_count - (total_count - duplicate)
        return[duplicate, missing]

        


        
