def integerBreak(self):
    if(self == 1 or self == 2):
        return 1
    elif (self == 3):
        return 2
    else:
        remainder = self % 3
        exponent = self // 3
        if(remainder == 1):
            exponent -= 1
            res = 3 ** exponent
            res *= 4
        else:
            res = 3 ** exponent
            if(remainder != 0):
                res *= remainder
    return res
