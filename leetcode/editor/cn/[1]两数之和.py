# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10956 👎 0

from typing import List


# 1. 暴力枚举
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_len = len(nums)
#         for i in range(nums_len):
#             diff = target - nums[i]
#             for j in range(i+1, nums_len):
#                 if diff == nums[j]:
#                     return [i, j]
#         return []
# leetcode submit region end(Prohibit modification and deletion)

# 2.用哈希表进行查找
'''
哈希表中找不到差值，则把当前数添加进哈希表，那么差值若数组满足条件，则一定能从
哈希表中取出前面已放在哈希表中对值
'''
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[num] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [2, 7 ,11 ,15]
    target = 9
    so = Solution()
    r = so.twoSum(nums, target)
    print(r)