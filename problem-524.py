def problem_524(numbers):
    sumSoFar = 0  # 42
    startingIndex = 0
    for index, number in enumerate(numbers):
        if sumSoFar == 0 and number > 0:
            sumSoFar = number
            startingIndex = 0
        elif sumSoFar != 0 and sumSoFar + number > 0:
            sumSoFar += number
        elif sumSoFar != 0 and sumSoFar + number < 0:
            sumSoFar = 0
            startingIndex = 0
    return sumSoFar


numbers = [34, -50, 42, 14, -5, 86]
print(problem_524(numbers))
numbers2 = [-5, -1, -8, -9]
print(problem_524(numbers2))
~