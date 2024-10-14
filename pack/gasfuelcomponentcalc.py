from pack.typed_dict import DictStrFloat
from pack.calcobject import CalcObject


class GasFuelComponentCalc:
    u1: DictStrFloat
    u2: DictStrFloat
    dict_m: DictStrFloat
    dict_vars: DictStrFloat

    def __init__(self) -> None:
        pass

    def calc(self, calc_object: CalcObject):
        for element in calc_object.gas_fuel_elements:
            print(element)

    def calc_vars(self):
        pass

    def cleaner(self):
        pass
