from afsdk.af_time import AFTime


class AFAttribute:
    def __init__(self, name: str, attr_type: object, value: object,
                 date_time: AFTime) -> None:
        self.name: str = name
        self.type: object = attr_type
        self.value: object = value
        self.datetime: AFTime = date_time
