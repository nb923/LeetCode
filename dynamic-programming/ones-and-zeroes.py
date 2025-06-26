class Solution(object):
    def findMaxForm(self, strs, m, n):
        table = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            num_zero = s.count('0')
            num_one = s.count('1')
            
            for row in range(m, num_zero - 1, -1):
                for col in range(n, num_one - 1, -1):
                    table[row][col] = max(table[row][col], 1 + table[row - num_zero][col - num_one])
        
        return table[m][n]
