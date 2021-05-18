def integerBreak(x):
    """
    Returns the maximum product from the total added value of a positive integer.
    Example: 2+2+3 = 7 -> 2*2*3 = 12

    >>> integerBreak(7)

    12
    """

    if(x == 1 or x == 2):
        return 1
    elif (x == 3):
        return 2
    else:
        remainder = x % 3
        exponent = x // 3

        # Remainder can only be 0, 1 or 2
        if(remainder == 1):
            exponent -= 1
            res = 3 ** exponent
            # Subtraction of res and x is always 4
            res *= 4
        else:
            res = 3 ** exponent
            # If remainder is 0, then the exponent is the total added value
            # We only need to multiply the remaining value when remainder exist
            if(remainder == 2):
                res *= remainder
    return res
