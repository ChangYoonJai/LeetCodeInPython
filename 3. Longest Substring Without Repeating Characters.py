'''
Given a string s, find the length of the longest substring without repeating characters.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = [0, ]
        hash_c = set()
        for i, c in enumerate(s, 1):
            if c in hash_c:
                hash_c.clear()
                length.append(1)
            else:
                length.append(length[i-1] + 1)
            hash_c.add(c)
        return max(length)

def test(input:str, output:int):
    sol = Solution().lengthOfLongestSubstring(input)
    if sol != output:
        print(input, sol, output)
    else:
        print(input)

test("dvdf", 3)
test("abcabcbb", 3)
test("bbbbb", 1)
test("pwwkew", 3)
test("", 0)