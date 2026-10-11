def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if not a:
        return []
    
    n = len(a)
    m = len(a[0])

    res = []

    for i in range(m):
        arr = []
        for j in range(n):
            arr.append(a[j][i])
        res.append(arr)

    return res
