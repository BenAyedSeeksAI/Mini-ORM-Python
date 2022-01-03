

class BaseManager:

    def __init__(self, model_class):
        self.model_class = model_class

    def select(self, *field_names):
        pass

    def bulk_insert(self, rows: list):
        pass

    def update(self, new_data: dict):
        pass

    def delete(self):
        pass


# ----------------------- Model ----------------------- #
class MetaModel(type):
    manager_class = BaseManager

    def _get_manager(self):
        return self.manager_class(model_class=self)

    @property
    def objects(self):
        return self._get_manager()


class BaseModel(metaclass=MetaModel):
    table_name = ""


# ----------------------- Usage ----------------------- #
class Employee(BaseModel):
    manager_class = BaseManager
    table_name = "employees"
