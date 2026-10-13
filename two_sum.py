class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        solution = {}

        for i, num in enumerate(nums):
          target_in_map = target-num

          if target_in_map in solution:
            return [solution[target_in_map],i]
        
          solution[num] = i

        return []

 