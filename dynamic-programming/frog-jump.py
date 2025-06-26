class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        
        stone_positions = {stone: set() for stone in stones}
        stone_positions[0].add(0)  
        
        for stone in stones:
            for k in stone_positions[stone]:
                for step in range(k - 1, k + 2):
                    if step > 0 and stone + step in stone_positions:
                        stone_positions[stone + step].add(step)
        
        return bool(stone_positions[stones[-1]])
