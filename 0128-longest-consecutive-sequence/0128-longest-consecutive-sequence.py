class Solution(object):
    def longestConsecutive(self, nums):
        numbers = set(nums)
        max_count = 0

        for num in numbers:
            if num - 1 not in numbers:
                current = num
                count = 1

                while current + 1 in numbers:
                    current += 1
                    count += 1

                max_count = max(max_count, count)

        return max_count