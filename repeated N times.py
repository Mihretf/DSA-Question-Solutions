class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        # approach would be to keep count of all the numbers and their values in dictionary, then find n as nums.
        # length /2 then check from the key value pair, the pair, the one that has the same pair as n, we will
        #return the key of that. 
        from collections import Counter
        from typing import List
        counts = Counter(nums)
        n = len(nums) // 2
        for key, value in counts.items():
            if value == n:
                return key
