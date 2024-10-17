from .calcobjectfactory import CalcObjectFactory
from pack.calculator import Calculator
from pack.calcconfiguration import CalcConfiguration
from pack.calcobject import CalcObject
from datetime import datetime
from pack.af_elements import create_struct


CHECK = False


class CalcInstance():
    def __init__(self, calc_object_factory: CalcObjectFactory,
                 calculator: Calculator) -> None:
        self.af_struct = create_struct()
        self.config = CalcConfiguration().initialize()
        self.calc_object_factory = calc_object_factory
        self.calculator = calculator
        self.calc_objects: list[CalcObject] = []
        self.pisystems = None
        self.pisystem = None
        self.afdatabase = None

    def initialize(self):
        self.__connect()
        self.calc_objects = self.__get_collection()

    def calculation(self, date_time: datetime):
        # проверка на изменение конфигурации
        if CHECK:
            self.__get_collection()
        for calc_object in self.calc_objects:
            self.calculator.calculate(calc_object, date_time, self.config)

    def __get_collection(self) -> list[CalcObject]:
        list_objects: list[CalcObject] = []
        for element in self.af_struct.child_elements:
            # заглушка
            obj = self.calc_object_factory.create(
                self.af_struct.child_elements[element],
                self.config)
            list_objects.append(obj)
        return list_objects

    def __connect(self): pass
    def __upd_state(seld): pass
