# Generate fibonacci sequence of length N using recursion and dynamic programming

class Solution:

    def __init__(self,N):
        self.length = N

    # Recursive Solution
    def recursion(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        return self.recursion(x-1) + self.recursion(x-2)

    # Dynamic Programming solution to the fibonacci sequence
    def dp_method(self, x, memo = [0,1]):
        if len(memo) <= x:
            memo.append(self.dp_method(x-1, memo) + self.dp_method(x-2, memo))
        return memo[x]

    def test(self, method = 'recursion'):
        output = []
        if method == 'recursion':
            for i in range(self.length):
                output.append(self.recursion(i))
        if method == 'dp_method':
            for i in range(self.length):
                output.append(self.dp_method(i))
        return output

# Test
n = int(input('How long is your fibonacci sequence?: '))
test_case = Solution(n)

print('Output of Recursive method')
print(test_case.test('recursion'))

print('Output of Dynamic Programming')
print(test_case.test('dp_method'))
