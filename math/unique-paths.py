class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        grid = [([0] * (n + 1)) for _ in range(m + 1)]

        grid[m - 1][n] = 1

        for row in range(m - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                grid[row][column] = grid[row + 1][column] + grid[row][column + 1]

        return grid[0][0]

        mem_map = {}

        # def get_total_unique_paths(x, y):
        #     if x >= n or y >= m:
        #         return 0

        #     if x == n - 1 and y == m - 1:
        #         return 1

        #     if (x, y) in mem_map:
        #         return mem_map[(x, y)]

        #     result = get_total_unique_paths(x + 1, y) + get_total_unique_paths(x, y + 1)
        #     mem_map[(x, y)] = result
            
        #     return result

        # return get_total_unique_paths(0, 0)





        