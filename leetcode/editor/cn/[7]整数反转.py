# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。 
# 
#  如果反转后整数超过 32 位的有符号整数的范围 [−231, 231 − 1] ，就返回 0。 
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 123
# 输出：321
#  
# 
#  示例 2： 
# 
#  
# 输入：x = -123
# 输出：-321
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 120
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：x = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  -231 <= x <= 231 - 1 
#  
#  Related Topics 数学 
#  👍 2792 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def reverse(self, x: int) -> int:
#         x_str = str(x)
#         sign = '' # 符号
#         num = x_str # 数字
#         if not x_str.isdigit():
#             sign = x_str[0]
#             num = x_str[1:]
#         x_reverse = sign + ''.join(list(reversed(num)))
#         x_reverse =  int(x_reverse)
#         if -2**31 <= x_reverse <= 2**31 -1:
#             return x_reverse
#         return 0
# leetcode submit region end(Prohibit modification and deletion)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        x_reverse = []
        for char in str(x)[::-1]:
            if char.isdigit():
                x_reverse.append(char)
            else:
                x_reverse.insert(0, char)
        x_reverse = ''.join(x_reverse)
        x_reverse =  int(x_reverse)
        if -2**31 <= x_reverse <= 2**31 -1:
            return x_reverse
        return 0
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    x = -2**31
    s = Solution()
    r = s.reverse(x)
    print(r)