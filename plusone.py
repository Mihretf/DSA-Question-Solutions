class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # we're making the thing move backward, by giving it the start, the stop and the how to move direction
        for i in range(len(digits)-1, -1, -1):
            # if our last value is less than 9 then we can simply add one and return the value
            if digits[i] <9:
                digits[i]+=1
                return digits
            # else if our last value is 9 then we change that last value to 0, and we will move on to the number next to it in the left side
            digits[i] =0
            # if all the values we get are 0,0,0 since the large integer can never contain any leading 0's we should add one before it
        return [1] + digits
