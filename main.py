from pack.calculator import Calculator
from pack.calcobjectfactory import CalcObjectFactory
from pack.calcinstanse import CalcInstance
from datetime import datetime


# Аналог класса АСЕ расчета
# ModuleDependentInitialization()
class Calc:
    def __init__(self) -> None:
        self.main_calculator = Calculator()
        self.calc_object_factory = CalcObjectFactory()
        self.calc_instance = CalcInstance(
            calc_object_factory=self.calc_object_factory,
            calculator=self.main_calculator)
        self.calc_instance.initialize()

# ACECalculations()
    def ace_calculation(self):
        current_datetime = datetime.now()
        self.calc_instance.calculation(current_datetime)


# блок программы, запускаемой службой
def initialize() -> Calc:
    calc_instance = Calc()
    return calc_instance


# запусается по расписанию
def calculate(instance: Calc):
    instance.ace_calculation()


if __name__ == '__main__':
    instance = initialize()
    calculate(instance)
