class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            if target-nums[i] in num_map:
                sol_list = []
                sol_list.append(num_map[target-nums[i]])
                sol_list.append(i)
                return sol_list
            num_map[nums[i]] = i
        