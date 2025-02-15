def generate(numRows):
    answer_list = []

    # Create empty lists for each row
    for _ in range(numRows):
        answer_list.append([])

    # First row is always [1]
    answer_list[0] = [1]

    # Build each subsequent row
    for i in range(1, numRows):
        temp_list = [1]  # Every row starts with 1

        # Calculate the values between the first and last 1
        for j in range(1, i):
            temp_list.append(answer_list[i-1][j-1] + answer_list[i-1][j])

        temp_list.append(1)  # Every row ends with 1

        answer_list[i] = temp_list

    return answer_list

print(generate(8))
#

