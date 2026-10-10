
def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    if not a:
        return []

    if any(len(row) != len(b) for row in a):
        return -1

    result = []

    for row in a:
        total = 0
        for i in range(len(b)):
            total += row[i] * b[i]
        result.append(total)

    return result
