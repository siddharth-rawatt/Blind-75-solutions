class Solution(object):
    def productExceptSelf(self, nums):
        prefix = []
        postfix = []
        output = []
        pre = 1
        po = 1
        for i in nums:
            pre = i * pre
            prefix.append(pre)

        for i in nums[::-1]:
            po = i * po
            postfix.append(po)

        postfix = postfix[::-1]
        postfix.append(1)

        for i, num in enumerate(nums):
            if i == 0:
                output.append(postfix[i + 1])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])

        return output

        """
        :type nums: List[int]
        :rtype: List[int]
        """
