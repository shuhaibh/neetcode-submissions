class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_num = set(nums)
        n=len(set_num)
        m=len(nums)
        return n!=m