class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        longest_by_end =  []
        for i in range(len(nums))
            longest_by_end.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_by_end[i] = max(longest_by_end[i], longest_by_end[j] + 1)
        return max(longest_by_end[i])


assert s.lengthOfLIS(nums=[1,1]) == 1