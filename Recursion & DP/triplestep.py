# Give total possiblity of climbing N steps, when you can take either 1, 2,
# or 3 steps at a time. Consider recursion and dynamic programming

import timeit

class Solution:

    def __init__(self,N):
        self.steps = N

    # simple recursion
    def recursive_method(self, N):
        if N < 0:
            return 0
        elif N ==0:
            return 1
        else:
            return self.recursive_method(N-1) + self.recursive_method(N-2) + self.recursive_method(N-3)

    # memoization
    def dp_method(self, N, memo = [1,2,4]):
        if N <= 0:
            return 0
        if N > len(memo):
            memo.append(self.dp_method(N-1,memo) + self.dp_method(N-2,memo) + self.dp_method(N-3,memo))
        return memo[N-1]

    # Test method
    def test(self, method):
        if method == 'recursion':
            for i in range(self.steps):
                print(self.recursive_method(i))
        if method == 'dp':
            for i in range(self.steps):
                print(self.dp_method(i))

# Test
steps = int(input('Total number of steps to test?: '))
test_case = Solution(steps)

print('Simple recursion')
start1 = timeit.default_timer()
test_case.test('recursion')
finish1 = timeit.default_timer()
print('Total compute time: ', finish1 - start1)

print('Dynamic programming')
start2 = timeit.default_timer()
test_case.test('dp')
finish2 = timeit.default_timer()
print('Total compute time: ', finish2 - start2)

print('dp_method was {} times faster than simple recursion'.format((finish1-start1)/(finish2-start2)))
