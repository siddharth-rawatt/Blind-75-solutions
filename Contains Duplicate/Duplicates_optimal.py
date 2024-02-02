class Solution(object):
    def containsDuplicate(self, nums):
        lst = []
        for i in nums:
            if i in lst:
                return True
            else:
                lst.append(i)
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """


# ponint to note - why does the abpove algo works fine if we use a set or a dictionary but it fails to perform with a list/array.
# this approach turned out to be slow in the leetcode, although it had a time complexity of O(n), but had to use some exra space


class Solution(object):
    def containsDuplicate(self, nums):
        lst = {}
        for i in nums:
            if i in lst:
                return True
            else:
                lst[i] = "presemt"
        return False
