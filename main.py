def sort_matrix(matrix):
    old_matrix = matrix
    new_matrix = []

    old_size = len(old_matrix)
    new_size = old_size

    for x in range(old_size):
        y_max = 0
        for y in range(new_size):
            if abs(old_matrix[y][x]) > abs(old_matrix[y_max][x]):
                y_max = y
        new_matrix.append(old_matrix.pop(y_max))
        new_size = len(old_matrix)

    return new_matrix


def first_triag(matrix):
    new_matrix = matrix
    size = len(new_matrix)
    for c in range(size):

        new_matrix[c] = normilize_row(new_matrix[c], new_matrix[c][c])
        for y in range(c + 1, size):
            new_matrix[y] = add_row_to_row(new_matrix[y], new_matrix[c], -new_matrix[y][c])

    return new_matrix


def second_triag(matrix):
    new_matrix = matrix
    size = len(new_matrix)
    for c in range(size - 1, -1, -1):
        for y in range(c - 1, -1, -1):
            new_matrix[y] = add_row_to_row(new_matrix[y], new_matrix[c], -new_matrix[y][c])

    return new_matrix


def add_row_to_row(f_l, s_l, coef):
    if len(f_l) != len(s_l):
        pass
    size = len(f_l)
    new_l = []

    for i in range(size):
        new_l.append(f_l[i] + s_l[i] * coef)

    return new_l


def normilize_row(row, el):
    if el == 0:
        return row
    new_row = []
    for i in range(len(row)):
        new_row.append(row[i] / el)
    return new_row


def calculate_trig_determinant(matrix):
    det = 1
    for c in range(len(matrix)):
        det*=matrix[c][c]


def print_matrix(matrix):
    for i in matrix:
        print(*i)


matrix = []
f = open("./input.txt", 'r')

raw = f.readlines()

for line in raw:
    if line[-1] == "n":
        matrix.append([int(j) for j in line[0:-2].split()])
    else:
        matrix.append([int(j) for j in line.split()])
f.close()

print("Исходная матрица: ")
print_matrix(matrix)
print("\n")

print("Отсортированная матрица: ")
sorted_matrix = sort_matrix(matrix)
print_matrix(sorted_matrix)
print("\n")

print("Треугольная матрица: ")
triag_matrix = first_triag(sorted_matrix)
print_matrix(triag_matrix)
print("\n")

if calculate_trig_determinant(triag_matrix) == 0:
    print("Бесконечное количество решений")
else:
    print("Корни: ")
    roots = [round(i[len(triag_matrix)], 3) for i in second_triag(triag_matrix)]
    print(*roots)
    print("\n")

    print("Невязки: ")
    deviations = []
    size = len(sorted_matrix)
    for y in range(size):
        row_sum = 0
        for x in range(size):
            row_sum += sorted_matrix[y][x] * roots[x]
        deviations.append(sorted_matrix[y][size] - row_sum)

    print(*deviations)

