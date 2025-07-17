from collections import defaultdict
from functools import lru_cache

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10**9 + 7
        count = defaultdict(int)

        # Step 1: Count frequency of each character at each column position
        for word in words:
            for i, c in enumerate(word):
                count[(i, c)] += 1

        # Step 2: Recursive DFS with memoization
        @lru_cache(maxsize=None)
        def dfs(i, k):
            # If we've formed the entire target
            if i == len(target):
                return 1
            # If we've reached the end of word length but target is incomplete
            if k == len(words[0]):
                return 0

            # Option 1: Skip current column
            res = dfs(i, k + 1)

            # Option 2: Use current column if it has the needed character
            c = target[i]
            if count[(k, c)] > 0:
                res += count[(k, c)] * dfs(i + 1, k + 1)
                res %= MOD

            return res

        return dfs(0, 0)
words = ["acca","bbbb","caca"]
target = "aba"
sol = Solution()
print(sol.numWays(words, target))  # Output: 6
