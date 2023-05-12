class Solution:
    def myAtoi(self, s: str) -> int:
        # step 1: ignore leading whitespace
        s = s.lstrip()

        # step 2: check for sign
        sign = 1
        if s and (s[0] == '+' or s[0] == '-'):
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # step 3: read digits
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            else:
                break

        # step 4: apply sign
        num *= sign

        # step 5: clamp to range
        num = max(min(num, 2**31-1), -2**31)

        return num