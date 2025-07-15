class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        ans= []
        seen = set()
        n = len(grid)
        repeated = 0
        actual_sum = 0
        for i in range(n):
            for j in range(n):
                val=grid[i][j]
                actual_sum += val
                if val in seen:
                    repeated = val
                else:
                    seen.add(val)

        total_elements = n * n
        expected_sum = (total_elements * (total_elements + 1)) // 2
        missing = expected_sum - (actual_sum - repeated)     
        ans.append(repeated)
        ans.append(missing)
        return ans
    
grid = [[1, 2,3 ,4], [5, 4, 6 ,7], [8, 9, 10, 11], [12, 13, 14, 15]]
sol = Solution()
result = sol.findMissingAndRepeatedValues(grid)
print("repeating value is:",result[0]) 
print ("missing value is : ",result[1])
print(sol.findMissingAndRepeatedValues(grid))
