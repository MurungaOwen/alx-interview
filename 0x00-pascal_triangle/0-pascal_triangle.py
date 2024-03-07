def pascal_triangle(n):
    try:
        n = int(n)
        if n <= 0:
            return []

        triangle = [[1]]
        for i in range(1, n):
            row = [1] #initialise a row with 1 as first value for each row
            for j in range(1, i):#loop for values inside the row
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
            row.append(1)
            triangle.append(row)
        return triangle
    except ValueError :
        print("Invalid input: n must be an integer.")
        return []