def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    print(divisible_by_ten(20))
    print(divisible_by_ten(25))  