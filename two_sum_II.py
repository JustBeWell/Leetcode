class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        last_i = len(numbers) - 1

        while i < last_i:
            n1 = numbers[i]
            n2 = numbers[last_i]

            posible_sol = n1 + n2

            if posible_sol == target:
                return [i + 1, last_i + 1]

            elif posible_sol < target:
                i += 1

            else:
                last_i -= 1

        return []