# Determine if a string has all unique characters

class Solution:

    def is_unique(self, string_input):
        hash = {}
        for char in string_input:
            hash[char] = 1
        if len(hash) == len(string_input):
            return True
        else:
            return False

# Test method
test = Solution()
test_string = str(input('Input string to test for is_unique: '))
print('The string [{}] has distinct characters: {}'.format(test_string, test.is_unique(test_string)))
