def get_terrace(size):
    square = [[0 for j in range(2 * size - 1)] for i in range(2 * size - 1)]
    counter = 1
    dj = 0
    for i in range(size):
        di = size - 1
        for j in range(size):
            square[i + di][j + dj] = counter
            counter += 1
            di -= 1
        dj += 1
    for j in range(size // 2):
        for i in range(2 * size - 1):
            square[i][j - (size // 2) * 2] = square[i][j] or square[i][j - (size // 2) * 2]
            square[i][j] = 0
            square[i][j + (size // 2)] = square[i][j - (size // 2)] or square[i][j + (size // 2)]
            square[i][j - (size // 2)] = 0
            square[j - (size // 2) * 2][i] = square[j][i] or square[j - (size // 2) * 2][i]
            square[j][i] = 0
            square[j + (size // 2)][i] = square[j - (size // 2)][i] or square[j + (size // 2)][i]
            square[j - (size // 2)][i] = 0
    square = [square[i][size // 2: 2 * size - 1 - size // 2] for i in range(size // 2, 2 * size - 1 - size // 2)]
    return(square)
def get_quarter_square(size):
    square = [[0 for j in range(size)] for i in range(size)]
    quarter_square = get_terrace(size // 2)         # получаем методом террас
    for n, ij0 in enumerate([(0, 0), (size // 2, size // 2), (0, size // 2), (size // 2, 0)]):
        i0, j0 = ij0
        for i in range(size // 2 -1):
            for j in range(size // 2 -1):
                square[i + i0][j + j0] = quarter_square[i][j] + n * (size // 2) ** 2
    square[0][0],           square[size // 2][0],    square[size // 2 - 1][0],    square[size - 1][0] = \
    square[size // 2][0],    square[0][0],           square[size - 1][0],        square[size // 2 - 1][0]
    for i in range(1, size // 2 - 1):
        square[i][1], square[i + size // 2][1] = square[i + size // 2][1], square[i][1]
    if size >= 6:
        for j in range(size // 2 - (size // 2 - 3) // 2, size // 2 + (size // 2 - 3) // 2):
            for i in range(size // 2):
                square[i][j], square[size // 2 + i][j] = square[size // 2 + i][j], square[i][j]
    return (square)
def get_double_parity(size):
    square = [[0 for j in range(size)] for i in range(size + 2 * (size //2 - 1))]
    counter = 1
    i0 = size //2 - 1
    for k in range(size //4):
        
        for j, i in enumerate([i for i in range(size //2)] + sorted([i for i in range(size //2)], reverse=True)):
            square[i0 - i][j] = counter
            counter += 1
        for j, i in enumerate([i for i in range(size //2)] + sorted([i for i in range(size //2)], reverse=True)):
            square[i0 + 1 + i][size - 1 - j] = counter
            counter += 1
        for j, i in enumerate([i for i in range(size //2)] + sorted([i for i in range(size //2)], reverse=True)):
            square[i0 + 2 - i][size - 1 - j] = counter
            counter += 1
        for j, i in enumerate([i for i in range(size //2)] + sorted([i for i in range(size //2)], reverse=True)):
            square[i0 + 3 + i][j] = counter
            counter += 1
        i0 += 4
    for i in range(size //2 - 1):
        for j in range(size):
            square[i - (size //2) * 2 + 2][j] = square[i][j] or square[i - (size //2) * 2 + 2][j]
            square[i][j] = 0
            square[i + (size //2) - 1][j] = square[i - (size //2) + 1][j] or square[i + (size //2) - 1][j]
            square[i - (size //2) + 1][j] = 0
    square = [square[i] for i in range(size //2 - 1, size + size //2 - 1)]
    return(square)

n = int(input())
if n%2 == 0 and n/2%2==0:
    square =  get_double_parity(n)
    for i in square: print(*i) 
elif n%2 == 0 and n/2%2!=1: 
    square =  get_quarter_square(n)
    for i in square: print(*i) 
elif n%2 == 1 or n/2%2==1 :
    square =  get_terrace(n)
    for i in square: print(*i)

