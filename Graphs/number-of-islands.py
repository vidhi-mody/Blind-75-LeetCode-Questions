"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:       
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j,m,n,grid):
            queue = [(i,j)]
            while(len(queue) > 0):
                i,j = queue.pop()
                grid[i][j] = "0"
                if(i>0 and grid[i-1][j] == "1"):
                    queue.append((i-1,j))
                if(i< m-1 and grid[i+1][j] == "1"):
                    queue.append((i+1,j))
                if(j>0 and grid[i][j-1] == "1"):
                    queue.append((i,j-1))
                if(j<n-1 and grid[i][j+1] == "1"):
                    queue.append((i,j+1))
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == "1"):
                    bfs(i,j,m,n,grid)
                    count += 1
        return count
        