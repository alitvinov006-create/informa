from tkinter import *
# pygame у меня намертво не устанавливается :(
# пришлось делать по своему

from random import *
from heapq import *
from enum import *

# размер сетки и окна
gridsize, cellsize = 10, 50
windowsize = gridsize * cellsize

# диапазон весов клеток (стоимость прохождения)
vmin, vmax = 1, 10

class CellType(Enum):
    EMPTY = 0     # пустая клетка
    OBSTACLE = 1  # стена
    START = 2     # старт (A)
    END = 3       # финиш (B)
    PATH = 4      # найденный путь

class Cell:
    def __init__(self):
        self.type = CellType.EMPTY  # по умолчанию пустая клетка
        self.weight = 1             # стоимость прохождения


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


class Node:
    def __init__(self, x, y, g=0, h=0):
        self.x, self.y, self.g, self.h = x, y, g, h  # координаты + стоимость пути

    def f(self):
        return self.g + self.h  # f = g + h (оценка узла)

    def __lt__(self, other):
        return self.f() < other.f()  # приоритет в куче

def a_star(grid, start, goal):

    # очередь с приоритетом (open set)
    open_set = []

    # откуда пришли в каждую клетку (для восстановления пути)
    came_from = {}

    # стоимость пути от старта до клетки
    g_score = {}

    # добавляем стартовый узел
    heappush(open_set, Node(*start, 0, manhattan_distance(*start, *goal)))

    # старт имеет стоимость 0
    g_score[start] = 0

    # возможные направления движения (4 стороны)
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    # основной цикл A*
    while open_set:

        # берём узел с минимальным f
        cur = heappop(open_set)

        # если дошли до цели — восстанавливаем путь
        if (cur.x, cur.y) == goal:
            path = []
            p = goal

            # откат назад по came_from
            while p in came_from:
                path.append(p)
                p = came_from[p]

            # добавляем старт
            path.append(start)

            # разворачиваем путь
            path.reverse()

            # возвращаем путь и стоимость
            return path, g_score[goal]

        # проверяем соседей
        for dx, dy in dirs:

            nx, ny = cur.x + dx, cur.y + dy

            # проверка границ и стен
            if not (0 <= nx < gridsize and 0 <= ny < gridsize) or grid[nx][ny].type == CellType.OBSTACLE:
                continue

            neigh = (nx, ny)

            # новая стоимость пути до соседа
            new_g = g_score[(cur.x, cur.y)] + grid[nx][ny].weight

            # если нашли лучший путь
            if neigh not in g_score or new_g < g_score[neigh]:

                # запоминаем откуда пришли
                came_from[neigh] = (cur.x, cur.y)

                # обновляем стоимость
                g_score[neigh] = new_g

                # добавляем в очередь с приоритетом
                heappush(
                    open_set,
                    Node(nx, ny, new_g, manhattan_distance(nx, ny, *goal))
                )

    # если путь не найден
    return []


# генерация поля
def generate(grid):

    for x in range(gridsize):
        for y in range(gridsize):

            # делаем клетку пустой
            grid[x][y].type = CellType.EMPTY

            # задаём случайный вес
            grid[x][y].weight = randint(vmin, vmax)

            # случайно добавляем препятствия (25%)
            if random() < 1/4:
                grid[x][y].type = CellType.OBSTACLE


# само приложение
class App:
    def __init__(self, root):

        self.root = root

        # холст для рисования сетки
        self.canvas = Canvas(root, width=windowsize, height=windowsize, bg="white")
        self.canvas.pack()

        # создание сетки клеток
        self.grid = [[Cell() for _ in range(gridsize)] for _ in range(gridsize)]

        # координаты старта и финиша
        self.start = None
        self.end = None

        # генерация карты
        generate(self.grid)

        # управление клавишами
        root.bind("<space>", self.solve)  # запуск A*
        root.bind("r", self.reset)        # новая карта

        # обработка клика мыши
        self.canvas.bind("<Button-1>", self.click)

        # первая отрисовка
        self.draw()


    # ивент-хэндлер кликов
    def click(self, event):

        # перевод координат пикселей в координаты сетки
        x, y = event.x // cellsize, event.y // cellsize

        # проверка границ
        if not (0 <= x < gridsize and 0 <= y < gridsize):
            return

        cell = self.grid[x][y]

        # если клик по стене — убрать её
        if cell.type == CellType.OBSTACLE:
            cell.type = CellType.EMPTY
            self.draw()
            return

        # установка старта
        if self.start is None:
            self.clear_paths()
            self.start = (x, y)
            cell.type = CellType.START

        # установка финиша
        elif self.end is None and (x, y) != self.start:
            self.clear_paths()
            self.end = (x, y)
            cell.type = CellType.END

        # иначе ставим стену
        elif (x, y) != self.start and (x, y) != self.end:
            cell.type = CellType.OBSTACLE

        self.draw()

    def clear_paths(self):
        for row in self.grid:
            for c in row:
                if c.type == CellType.PATH:
                    c.type = CellType.EMPTY

    # цвета клеток
    def color(self, cell):

        if cell.type == CellType.EMPTY:
            v = int(50 + (cell.weight / vmax) * 180)
            return "grey"  # обычная клетка

        if cell.type == CellType.OBSTACLE:
            return "black"  # стена

        if cell.type == CellType.START:
            return "green"  # старт A

        if cell.type == CellType.END:
            return "red"  # финиш B

        if cell.type == CellType.PATH:
            return "yellow"  # путь

        return "brown"

    # рендер поля
    def draw(self):

        self.canvas.delete("all")

        for x in range(gridsize):
            for y in range(gridsize):

                c = self.grid[x][y]

                x0, y0 = x * cellsize, y * cellsize

                self.canvas.create_rectangle(
                    x0, y0,
                    x0 + cellsize,
                    y0 + cellsize,
                    fill=self.color(c),
                    outline="gray"
                )

    # запуск алгоритма
    def solve(self, event=None):

        self.clear_paths()

        path, cost = a_star(self.grid, self.start, self.end)

        if path:
            for x, y in path:
                if self.grid[x][y].type not in (CellType.START, CellType.END):
                    self.grid[x][y].type = CellType.PATH

            print("Стоимость пути:", cost)

        self.draw()

    # ресет
    def reset(self):

        generate(self.grid)

        self.start = None
        self.end = None

        self.draw()

g = Tk()
g.title("а-виакомпания норд-стар")

App(g)
g.mainloop()