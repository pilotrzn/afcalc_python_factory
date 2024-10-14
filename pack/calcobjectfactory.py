from pack.calcobject import CalcObject
from pack.calcconfiguration import CalcConfiguration
from pack.cls_af import AFElement


class CalcObjectFactory:
    def create(self, afelement: AFElement,
               config: CalcConfiguration) -> CalcObject:
        calc_object = CalcObject()

        calc_object.name = afelement.name
        afattributes = afelement.af_attributes

        for attr in afattributes:
            calc_object.attributes[attr] = afattributes[attr]
        return calc_object

    def map_child_elements(self):
        pass

    def map_child_attributes(self):
        pass
