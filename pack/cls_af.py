from datetime import datetime


class AFTime:
    pass


class AFAttribute:
    def __init__(self, name: str, attr_type: object, value: object,
                 date_time: datetime) -> None:
        self.name: str = name
        self.type: object = attr_type
        self.value: object = value
        self.datetime: datetime = date_time


class AFElement:
    def __init__(self) -> None:
        self.name: str
        self.child_elements: dict[str, AFElement] = {}
        self.af_attributes: dict[str, AFAttribute] = {}
