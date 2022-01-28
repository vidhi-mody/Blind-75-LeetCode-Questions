"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        total = m*n
        answer = []
        start_row = 0
        end_row = m - 1
        start_col = 0
        end_col = n - 1
        right = True
        down = True
        while(len(answer) != total):
            if(right):
                for j in range(start_col,end_col):
                    if(matrix[start_row][j] != "#"):
                        answer.append(matrix[start_row][j])
                        matrix[start_row][j] = "#"      
                right = False
            if(down):
                for i in range(start_row, end_row):
                    if(matrix[i][end_col] != "#"):
                        answer.append(matrix[i][end_col])
                        matrix[i][end_col] = "#"     
                down = False
            if not right:
                for j in range(end_col, start_col-1, -1):
                    if(matrix[end_row][j] != "#"):
                        answer.append(matrix[end_row][j])
                        matrix[end_row][j] = "#"         
                right = True
            if not down:
                for i in range(end_row, start_row-1, -1):
                    if(matrix[i][start_col] != "#"):
                        answer.append(matrix[i][start_col])
                        matrix[i][start_col] = "#"    
                down = True
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
                
        return answer
                    
                
                    
            
            
            
            