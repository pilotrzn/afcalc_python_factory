from afsdk.af_attribute import AFAttribute
from afsdk.af_element import AFElement
from afsdk.af_time import AFTime
# from datetime import datetime


class CalcObject:
    def __init__(self) -> None:
        self._name: str = 'Name'
        self.attributes: dict[str, AFAttribute] = {}
        self.result_attributes: dict[str, AFAttribute] = {}
        self.gas_fuel_elements: dict[str, AFElement] = {}
        self.liquid_fuel_elements: dict[str, AFElement] = {}
        self.smoke_gas_elements: dict[str, AFElement] = {}
        self.row_components: dict[str, AFElement] = {}
        self.fact_variables: dict[str, float] = {}
        self.plan_variables: dict[str, float] = {}
        self.regular_variables: dict[str, float] = {}
        self.result_variables: dict[str, float] = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, thename: str):
        self._name = thename

    def get_value(self, attribute: AFAttribute, date_time: AFTime) -> float:
        return 0
