from pack.cls_af import AFElement, AFAttribute
from datetime import datetime
import random


def create_struct() -> AFElement:
    root_element: AFElement = AFElement()
    for i in range(1, 10):
        new_element = AFElement()
        new_element.name = f'element_{i}'
        for j in range(1, 5):
            afatribute = AFAttribute(f'attr{i}', int,
                                     random.randint(1, 100),
                                     datetime.now())
            new_element.af_attributes[f'attribute_{j}'] = afatribute
        root_element.child_elements[new_element.name] = new_element
    return root_element
