# Two-sum problem   
def problem_one(numbers, k):
    # numbers = [10, 15, 3, 7]
    # k = 17
    bucket = set()
    for number in numbers:
        if k - number in bucket:
            return True
        else:
            bucket.add(number)
    return False

numbers = [10, 15, 3, 7]
k = 17
print(problem_one(numbers, k))