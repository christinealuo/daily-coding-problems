# With division
def problem_two(numbers):
    product = 1
    for number in numbers:
        product *= number
    result = []
    for number in numbers:
        result.append(int(product / number))
    return result

# Without division
def without_division(numbers):
    # Prefix products: [1, 2, 6, 24, 120]
    # Suffix products: [120, 120, 60, 20, 5]    
    return []

# Test
numbers_one = [1, 2, 3, 4, 5]
result_one = [120, 60, 40, 30, 24]
numbers_two = [3, 2, 1]
result_two = [2, 3, 6]
print(problem_two(numbers_one))
print(problem_two(numbers_two))

# Solution: https://www.dailycodingproblem.com/solution/2?token=8fa585c144e4af96610a0ca7a5229f05db3a722216fde4d7551669ea075d7e49b1bd1760