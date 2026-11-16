class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        return sum(stone in jewels for stone in stones)
        