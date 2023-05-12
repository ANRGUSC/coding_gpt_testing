class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
        
        reversed_num = 0
        while x > 0:
            reversed_num = (reversed_num * 10) + (x % 10)
            x //= 10
        
        reversed_num *= sign
        if reversed_num < -2147483648 or reversed_num > 2147483647:
            return 0
        else:
            return reversed_num