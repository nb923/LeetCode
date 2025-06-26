class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_set_array = [set() for _ in range(9)]
        col_set_array = [set() for _ in range(9)]
        box_set_array = [[set() for _ in range(3)] for _ in range(3)]

        for row_num in range(9):
            for col_num in range(9):
                value = board[row_num][col_num]

                if value == '.':
                    continue
                elif (value in row_set_array[row_num]) or (value in col_set_array[col_num]) or (value in box_set_array[row_num // 3][col_num // 3]):
                    return False
                
                row_set_array[row_num].add(value)
                col_set_array[col_num].add(value)
                box_set_array[row_num // 3][col_num // 3].add(value)
        
        return True
        