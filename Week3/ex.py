"""
Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False
"""
def large_power(base, exponent):
    """
    Check if base raised to the exponent is greater than 5000.
    
    :param base: The base number.
    :param exponent: The exponent to raise the base to.
    :return: True if base^exponent > 5000, otherwise False.
    """
    if base ** exponent > 5000:
        return True
    else:
        return False
if __name__ == "__main__":
    # Example usage
    print(large_power(5, 5))  # True, since 5^5 = 3125
    print(large_power(6, 4))  # True, since 6^4 = 1296
    print(large_power(3, 7))  # False, since 3^7 = 2187
    print(large_power(10, 10)) # True, since 10^3 = 1000
