# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        RetCell = Cell(0)
        RetCell.cell = self.cell + other.cell
        return RetCell

    def __sub__(self, other):
        RetCell = Cell(0)
        if self.cell > other.cell:
            RetCell.cell = self.cell - other.cell
        elif self.cell < other.cell:
            RetCell.cell = other.cell - self.cell
        return RetCell

    def __truediv__(self, other):
        RetCell = Cell(1)
        if self.cell > other.cell:
            if other.cell != 0:
                RetCell.cell = self.cell // other.cell
            else:
                RetCell.cell = 0
        elif self.cell < other.cell:
            if self.cell != 0:
                RetCell.cell = other.cell // self.cell
            else:
                RetCell.cell = 0
        return RetCell

    def __mul__(self, other):
        RetCell = Cell(0)
        RetCell.cell = self.cell * other.cell
        return RetCell

    def make_order(self, rows):
        n_value = self.cell//rows
        r_value = n_value * ( rows* "*" + "\n") + (self.cell % rows)*'*'
        return r_value


print("--------------------СЛОЖЕНИЕ--------------------")
cell1 = Cell(9)
print(cell1)
cell2 = Cell(10)
print(cell2)
print(cell2 + cell1)
print("--------------------ВЫЧИТАНИЕ--------------------")
cell1 = Cell(19)
print(cell1)
cell2 = Cell(17)
print(cell2)
print(cell2 - cell1)
print(cell1 - cell2)
print("--------------------ВЫЧИТАНИЕ--------------------")
# __add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
cell1 = Cell(2)
print(cell1)
cell2 = Cell(7)
print(cell2)
print(cell2 * cell1)
print("--------------------ДЕЛЕНИЕ--------------------")
cell1 = Cell(12)
print(cell1)
cell2 = Cell(17)
print(cell2)
print(cell2 / cell1)
print(cell1 / cell2)
print("--------------------ПОСТОРОЕНИЕ--------------------")
cell1 = Cell(27)
cell2 = Cell(17)
print(cell1.make_order(4))
print("--------------------")
print(cell2.make_order(5))

