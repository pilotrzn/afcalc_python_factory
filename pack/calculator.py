from pack.gasfuelcomponentcalc import GasFuelComponentCalc
from pack.calcobject import CalcObject
from datetime import datetime
from pack.calcconfiguration import CalcConfiguration


class Calculator:
    def __init__(self) -> None:
        self.gas_fuel_calc = GasFuelComponentCalc()
        self.liquid_calc = None
        self.raw_calc = None

    def calculate(self, calc_object: CalcObject,
                  date_time: datetime, config: CalcConfiguration):
        pass

    def __main_calc(self, calc_object: CalcObject):
        pass

    def __clear_collection(self, calc_object: CalcObject):
        pass
