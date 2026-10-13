class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0
        j = len(nums) - 1

        def binary_search(i, j, target, nums):
            if i > j:
                return -1

            mid = (i + j) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return binary_search(mid + 1, j, target, nums)

            else:
                return binary_search(i, mid - 1, target, nums)

        output = binary_search(i,j,target,nums)

        return output
    
        

        
        