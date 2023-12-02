def longest_switch(A):
    n = len(A)

    if n <= 1:
        return n

    max_length = 1
    current_length = 1

    for i in range(1, n):
        if A[i] != A[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)
