class Money:

    def __init__(self, money: int) -> None:
        """money - (целочисленная) для хранения количества денег (своя для каждого объекта класса Money);"""
        if self.check_money(money):
            self.set_money(money)

    @classmethod
    def check_money(cls, money: int) -> bool:
        """для проверки корректности объема средств в параметре money
        (возвращает True, если значение корректно и False - в противном случае)."""
        return type(money) is int and money >= 0

    def set_money(self, money: int) -> None:
        """для передачи нового значения приватной локальной переменной money (изменение выполняется
                только если метод check_money(money) возвращает значение True);"""
        if self.check_money(money):
            self.__money = money

    def add_money(self, money: int) -> None:
        """для прибавления средств из объекта mn класса Money к средствам текущего объекта;"""
        if isinstance(money, Money):
            if self.check_money(money):
                self.__money += money

    def get_money(self) -> int:
        """для получения текущего объема средств (денег);"""
        return self.__money


mn_1 = Money(10)
mn_2 = Money(20)
assert mn_1._Money__money == 10 and mn_2._Money__money == 20, "неверные значения в локальном приватном атрибуте __money"

mn_1.set_money(100)
mn_2.add_money(mn_1)
assert mn_1.get_money() == 100 and mn_2.get_money() == 120, "неверное количество средств: возможно некорректая работа методов set_money и/или add_money"

mn_1.set_money(-1)
assert mn_1.get_money() == 100, "неверное количество средств: некорректная работа метода set_money"
