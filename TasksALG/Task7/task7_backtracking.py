n = int(input())
square = [[0] * 3 for _ in range(3)] # создаем квадрат 3x3
square[0][0] = n # сразу фиксируем первую клетку

used = [False] * 10
used[n] = True # если число n уже стоит в квадрате

def valid(): # проверяем весь квадрат
    for i in range(3): # проверяем заполненные строки
        if all(square[i][j] != 0 for j in range(3)):
            if sum(square[i]) != 15:
                return False
    for j in range(3): # проверяем заполненные столбцы
        col = [square[i][j] for i in range(3)]
        if all(x != 0 for x in col):
            if sum(col) != 15:
                return False
    diag1 = [square[i][i] for i in range(3)] # главная диагональ
    if all(x != 0 for x in diag1):
        if sum(diag1) != 15:
            return False
    diag2 = [square[i][2 - i] for i in range(3)] # побочная диагональ
    if all(x != 0 for x in diag2):
        if sum(diag2) != 15:
            return False
    return True

def backtrack(pos):
    if pos == 9: # если все 9 клеток заполнены - решение найдено
        return True

    row, col = pos // 3, pos % 3

    if row == 0 and col == 0: # первая клетка уже занята числом N
        return backtrack(pos + 1)
    for num in range(1, 10): # пробуем поставить каждое еще не использованное число
        if not used[num]:
            # делаем шаг
            square[row][col], used[num] = num, True
            if valid() and backtrack(pos + 1): # продолжаем заполнять квадрат если условия не нарушены
                return True
            used[num], square[row][col] = False, 0 # сам возврат
    return False # если не нашли подходящее число для текущей клетки

if backtrack(False):
    for row in square:
        print(*row) # квадрат
else:
    print(-1) # если он отсутствует