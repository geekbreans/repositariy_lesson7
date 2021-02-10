# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class AnyClothes(ABC):
    @abstractmethod
    def s_calculate(self):
        pass


class AnyCoat(AnyClothes):
    s_value = 0

    def s_calculate(self, ins_value):
        self.s_value = ins_value/6.5 + 0.5

    def __add__(self, other):
        RetAnycoat = AnyCoat()
        RetAnycoat.s_value = self.s_value + other.s_value

        return RetAnycoat

    def __str__(self):
        return str(self.s_value)


class AnySuit(AnyClothes):
    s_value = 0

    # def __init__(self, v_Value):
    #     self.v_Value = v_Value
    #     self.s_value = self.s_calculate()

    def s_calculate(self, ins_value):
        self.s_value = 2 * ins_value + 0.3

    def __add__(self, other):
        RetAnysuit = AnySuit()
        RetAnysuit.s_value = self.s_value + other.s_value
        return RetAnysuit

    def __str__(self):
        return str(self.s_value)


# mCoat = MyClass()
# print(mCoat)
mCoat = AnyCoat()
mCoat.s_calculate(2)
print(mCoat)
print(mCoat + mCoat)

mSuit = AnySuit()
mSuit.s_calculate(5)
print(mSuit)
print(mSuit + mSuit)

print(mSuit + mSuit + mCoat + mCoat)

