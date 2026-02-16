class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result =[] # stack to keep the count of the operations used
        j =0 # our pointer will start from the first element, can increase
        for num in range(1, n+1):# this will act as a stream
            if j == len(target): # means our target and stack are identical, because J has reached to the length of the target
                break # we can stop our operations
            result.append("Push") # everytime we read a number we push, we pop it if it sth we don't want
            if num == target[j]: # if it is the same, then we move on to the next value to compare
                j+=1 # change our pointer too
            else:
                result.append("Pop") # if it is a value that we don't want meaning it is not present in the target, then since our whole process is to make our stack like the target then we can pop out the things that won't make it the same
        return result


        
