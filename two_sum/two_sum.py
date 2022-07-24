class Solution:
    # This notation essentially says that the list will be an integer, the input will be an integer
    # and that the result will also be an integer.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creates an empty dictionary/hashtable and assigns the values of nums list to seen 
        seen = {}
        # this for loop will take the target value, subtract a given value from the list
        # This subtracts a value from target then tries to find a match to the remainder as those will add up to the target
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            
            
            # attempts to find the remainder in the seen list.
            if remaining in seen:
                return [i, seen[remaining]]
            
            # This moves values in the list that have been used as a key to the dictionary.
            seen[value] = i
        