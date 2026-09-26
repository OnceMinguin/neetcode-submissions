class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        result = []
        for num in nums:
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1
        sorted_nums = sorted(nums_map.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sorted_nums[i][0])
        return result