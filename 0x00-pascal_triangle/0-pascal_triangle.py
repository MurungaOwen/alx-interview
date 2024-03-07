def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1] #initialise a row with 1 as first value for each row
        print(f"i is {i}")
        for j in range(1, i):#loop for values inside the row
            print(f"j is at {triangle[i - 1]}")
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle