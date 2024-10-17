from pack.calcobject import CalcObject
from pack.calcconfiguration import CalcConfiguration
from afsdk.af_attribute import AFAttribute
from afsdk.af_element import AFElement


class CalcObjectFactory:
    def create(self, afelement: AFElement,
               config: CalcConfiguration) -> CalcObject:
        calc_object = CalcObject()
        calc_object.name = afelement.name
        afattributes = afelement.af_attributes
        for attr in afattributes:
            calc_object.attributes[attr] = afattributes[attr]
        return calc_object

    def map_child_elements(self, calc_object: CalcObject,
                           attribute: AFAttribute,
                           config: CalcConfiguration):
        for element in calc_object.attributes:
            pass

    def map_child_attributes(self):
        pass
