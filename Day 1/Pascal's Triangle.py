def printPascal(n):
    triangle = []
    for row in range(1, n+1):
        rCe = 1
        add = []
        for i in range(1, row+1):
            add.append(rCe)
            rCe = rCe * (row - i) // i
        triangle.append(add)
    return triangle
