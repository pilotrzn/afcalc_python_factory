from afsdk.af_attribute import AFAttribute
import uuid


class AFElement:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.child_elements: dict[str, AFElement] = {}
        self.af_attributes: dict[str, AFAttribute] = {}
        self.id = self.__generate_id()

    def __generate_id(self):
        return uuid.uuid4()
