class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        // 1. we first need to find the midpoint of the given sorted array, meaning the index= we need to know the length of the array 
        // 2. we then go to the element where the midpoint index gives us. 
        // 3. then we compare it with the target value
        // 4. if the target value is equal to the selected numbr, we return that index
        // 5. if the target value is less than our selected number, then we move our pointers to the left side meaning we discard using the right side of the values to compare for the target number, 
        // 6. if the target value is greater than our selected number, then we move our index pointer one move to the right and then compare the values again. 
        // 7. if we do all of those yet we don't find them.... meaning for the moving to the left ones, if we find that our target variable is less than the current one but becomes greater when we move one step to the left then we return the index of the current one, similarly if the target variable is greater the next one, then when there is no more next, then we retrun the index of the current plus 1.
         int size = nums.size(); // when cpp calculates the size of nums it gives us in byte, so then we divide it by the individual byte value to get the number of elements found in that array
         int left = 0; // left is initated to the first element in the array
         int right = size - 1; // right is initiated to the last element in the array which is found by subtracting the size minus 1 because we are calculating the index. 


         while(left<=right){
            int mid = (left + right ) / 2;

            if(nums[mid] == target){
                return mid;
            }
            else if(nums[mid] < target){
                left = mid + 1;
            
            }
            else if(nums[mid] > target){
                right = mid -1;
            }


         }
         return left;

        
    }
};