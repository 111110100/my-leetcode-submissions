class Solution:
    def countNegatives(self, grid) -> int:
        return sum([y < 0 for x in grid for y in x])

answer = Solution()
print(answer.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(answer.countNegatives([[3,2],[1,0]]))
print(answer.countNegatives([[1,-1],[-1,-1]]))
print(answer.countNegatives([[-1]]))

'''
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return str(grid).count('-')
'''