def problem_521(sentence, k):
    all_rows = []
    for i in range(k):
        new_row = []
        all_rows.append(new_row)

    current_row_index = 0
    increasing = True
    for i in range(len(sentence)):
        current_row = all_rows[current_row_index]
        current_row.append(sentence[i])
        for j in range(k):
            if j != current_row_index:
                all_rows[j].append(" ")

        if current_row_index == k - 1 and increasing:
            increasing = False
        elif current_row_index == 0 and not increasing:
            increasing = True

        if increasing:
            current_row_index += 1
        else:
            current_row_index -= 1

    for i in range(len(all_rows)):
        print("".join(all_rows[i]))

sentence = "thisisazigzag"
k = 4
problem_521(sentence, k)