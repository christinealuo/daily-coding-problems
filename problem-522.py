# abracadabra
# 012345678910
# Return: [0, 7]

def problem_522(string, pattern):
    result = list() # []
    match_starting_index = 0 # 0
    current_match_index = 0 # Start looking for the first letter
    for index, letter in enumerate(string):
        if letter == pattern[current_match_index]:
            # Keep track of starting index
            if current_match_index == 0:
                match_starting_index = index
            # Found match, look for next letter in the string
            current_match_index += 1
            # Found perfect match
            if current_match_index == len(pattern):
                result.append(match_starting_index)
                current_match_index = 0 # Reset
                match_starting_index = 0 # Reset
        elif letter != pattern[current_match_index] and current_match_index != 0:
            current_match_index = 0
            match_starting_index = 0
    return result

string = "abracadabra"
pattern = "abr"
print(problem_522(string, pattern))
