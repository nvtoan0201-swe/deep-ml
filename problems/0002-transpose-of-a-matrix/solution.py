def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a:
        return []

    return [
        [a[j][i] for j in range(len(a))]
        for i in range(len(a[0]))
    ]