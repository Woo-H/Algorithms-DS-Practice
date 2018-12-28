# Robot on upper left corner of grid(size = r,c). Movement = (down, right).
# Certain cells are off limits. Design an algorithm to find a path to the bottom right

class Solution:

    def __init__(self, m, n):
        self.rows = m
        self.columns = n
        self.off_limits = []

    def set_off_limits(self, x, y):
        self.off_limits.append([x,y])

    def get_off_limits(self):
        return self.off_limits

    # Dynamic Programming method
    def paths(self):
        m, n = self.rows, self.columns
        off_limits = self.get_off_limits()

 	    # Create grid of size m x n. Fill with 'e'
        grid = [['e' for _ in range(n)] for _ in range(m)]

    	# Mark off limit points as 'x'
        for point in off_limits:
            grid[point[0]][point[1]] = 'x'

        print('Initial Grid: ', grid)

    	# Set Edge conditions
        i,j = n - 1, m - 1
        while grid[-1][i] != 'x' and i >= 0:
            grid[-1][i] = 1
            i -= 1
        while grid[i][-1] != 'x' and j >= 0 :
            grid[j][-1] = 1
            j -= 1

        # Memoization of possible routes from goal to starting point
        for r in reversed(range(m-1)):
            for c in reversed(range(n-1)):
                if grid[r][c] == 'x':
                    grid[r][c] = 'x'
                elif grid[r+1][c] == 'x' and grid[r][c+1] == 'x':
                    grid[r][c] = 'x'
                elif grid[r+1][c] == 'x' and grid[r][c+1] != 'x':
                    grid[r][c] = grid[r][c+1]
                elif grid[r][c+1] == 'x' and grid[r+1][c] != 'x':
                    grid[r][c] = grid[r+1][c]
                else:
                    grid[r][c] = grid[r+1][c] + grid[r][c+1]

        return grid[0][0]

# Test
print("Let's Create the Grid Dimensions")
m = int(input('Number of Rows?: '))
n = int(input('Number of Columns?: '))

test_case = Solution(m,n)

while 1:
    c = str(input('Add off limit points?(y/n): '))
    if c == 'n':
        print('Off_limits are: ', test_case.get_off_limits())
        break
    x = int(input('off limit point row?: '))
    y = int(input('off limit point column?: '))
    test_case.set_off_limits(x,y)

print('Total number of unique paths are ', test_case.paths())
