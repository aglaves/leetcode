class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        array_positions = {}
        for num in nums:
            if ((target - num) in array_positions.keys()):
                return [array_positions[target - num], i]
            array_positions[num] = i
            i += 1

        return None
