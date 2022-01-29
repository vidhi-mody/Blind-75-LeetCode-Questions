"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(i,j,m,n,heights):
            atlantic = False
            pacific = False
            queue = [(i,j)]
            visited = set()
            while(queue):
                i, j = queue.pop()
                if(i == m-1 or j == n-1):
                    atlantic = True
                if(i == 0 or j == 0):
                    pacific = True
                if(atlantic == True and pacific == True):
                    return (atlantic, pacific)
                if(i>0 and heights[i][j] >= heights[i-1][j]):
                    if((i-1,j) not in visited):
                        queue.append((i-1,j))
                        visited.add((i-1,j))
                if(j>0 and heights[i][j] >= heights[i][j-1]):
                    if((i,j-1) not in visited):
                        queue.append((i,j-1))
                        visited.add((i,j-1))          
                if(i<m-1 and heights[i][j] >= heights[i+1][j]):
                    if((i+1,j) not in visited):
                        queue.append((i+1,j))
                        visited.add((i+1,j))
                if(j<n-1 and heights[i][j] >= heights[i][j+1]):
                    if((i,j+1) not in visited):
                        queue.append((i,j+1))
                        visited.add((i,j+1))   
            return (atlantic, pacific)
            
        m = len(heights)
        n = len(heights[0])
        result = []
        for i in range(m):
            for j in range(n): 
                atlantic, pacific = bfs(i,j,m,n,heights) 
                if(atlantic == True and pacific == True):
                    result.append([i,j])
        return result
                    
                
                
                    
                
        