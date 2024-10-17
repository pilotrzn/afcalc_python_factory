from pack.calcobject import CalcObject


class GasFuelComponentCalc:
    def __init__(self) -> None:
        self.u1: dict[str, float] = {}
        self.u2: dict[str, float] = {}
        self.dict_m: dict[str, float] = {}
        self.dict_vars: dict[str, float] = {}
        self.dict_c1: dict[str, float] = {}
        self.dict_c2: dict[str, float] = {}
        self.dict_w1: dict[str, float] = {}
        self.dict_w2: dict[str, float] = {}
        self.dict_vur: dict[str, float] = {}

    def calc(self, calc_object: CalcObject):
        for element in calc_object.gas_fuel_elements:
            print(type(element))

    def calc_vars(self):
        pass

    def cleaner(self):
        pass
