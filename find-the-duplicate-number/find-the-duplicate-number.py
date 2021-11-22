class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = set()
        for c in nums:
            if c in count: return c
            if c  not in count:count.add(c)
        