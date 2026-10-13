import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        k_numbers = []

        for n in nums:
            if len(k_numbers) < k:
                heapq.heappush(k_numbers, n)

            elif n > k_numbers[0]:
                heapq.heapreplace(k_numbers, n)

        return k_numbers[0]