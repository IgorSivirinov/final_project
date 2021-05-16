from abc import ABC, abstractmethod


class IModellingElement(ABC):
    mass: float
    electric_charge: float

    x: float
    v_x: float

    y: float
    v_y: float

    z: float
    v_z: float

    @abstractmethod
    def work_with_x(self, not_variable_data: list, variable_data: list, num: int, i: int):
        pass

    @abstractmethod
    def work_with_y(self, not_variable_data: list, variable_data: list, num: int, i: int):
        pass

    @abstractmethod
    def work_with_z(self, not_variable_data: list, variable_data: list, num: int, i: int):
        pass
