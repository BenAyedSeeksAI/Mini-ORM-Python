class base:
    def __init__(self,model):
        self.Model = model

class MetaModel(type):
    base_model = base

class baseModel(metaclass=MetaModel):
    tablename = ""


class Person(baseModel):
    base_model = base
    tablename = "Person"
    fields = ("name", "address")

    def __init__(self):
        pass

class Vehicle(baseModel):
    base_model = base
    tablename = "Vehicle"
    fields = ("name", "speed")

    def __init__(self):
        pass


model_list = [Person,
              Vehicle,
              ]
