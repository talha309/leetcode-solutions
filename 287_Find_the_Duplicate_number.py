nums = [1,3,4,2,2]

# time complexity: O(n)
# space complexity: O(n)

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

sol = Solution()
result = sol.findDuplicate(nums)
print("Duplicate number is O(n):", result)

# time complexity: O(n)
# space complexity: O(1) constant space solution
# using Floyd's Tortoise and Hare (Cycle Detection) also called the slow and fast pointer technique

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

sol = Solution()
result = sol.findDuplicate(nums)
print("Duplicate number is O(1):", result)

