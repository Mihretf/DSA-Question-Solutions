class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack =[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    stack.append(prices[i]-prices[j])
                    break
            else:
                stack.append(prices[i])
        return stack
            


        
