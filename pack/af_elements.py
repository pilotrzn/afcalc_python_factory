from afsdk.af_attribute import AFAttribute
from afsdk.af_element import AFElement
from afsdk.af_time import AFTime
from datetime import datetime
import random


def create_struct() -> AFElement:
    root_element = create_element('root')
    for i in range(1, 10):
        new_element = create_element(f'element_{i}')
        sub_element = create_element('sub_element')
        for j in range(1, 5):
            new_element.af_attributes[f'attribute_{j}'] = create_attribute(
                f'attr{i}', int, random.randint(1, 100), datetime.now())
        new_element.af_attributes['sub_element'] = create_attribute(
            'sub_element', AFElement, sub_element, datetime.now())
        root_element.child_elements[new_element.name] = new_element
    return root_element


def create_attribute(attr_name: str, attr_type: object,
                     attr_value: object, dt: datetime) -> AFAttribute:
    return AFAttribute(name=attr_name,
                       attr_type=attr_type,
                       value=attr_value,
                       date_time=AFTime(dt))


def create_element(name: str) -> AFElement:
    element = AFElement(name)
    return element
