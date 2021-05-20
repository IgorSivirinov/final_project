import numpy as np
from scipy.integrate import odeint
from typing import List
from code.models.IModellingElement import IModellingElement
from code.models.ProgressBar import ProgressBar

def calculation_coordinate(frames: int, start_time: float, stop_time: float,
                           modelling_elements: List[IModellingElement]):
    bar = ProgressBar(" Calculation", max=stop_time*1000)

    def get_dv_xdt(variable_data: list, num: int):
        """
        :param variable_data - все объекты моделирования
        :param num - номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_data элементов на num-ый элемент по x
        """
        out = 0.0

        for i in range(len(modelling_elements)):
            if num != i:
                out += modelling_elements[i].work_with_x(not_variable_data, variable_data, num, i)
        return out

    def get_dv_ydt(variable_data: list, num: int):
        """
        :param variable_data: все объекты моделирования
        :param num: номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_data элементов на num-ый элемент по y
        """

        out = 0.0

        for i in range(len(modelling_elements)):
            if num != i:
                out += modelling_elements[i].work_with_y(not_variable_data, variable_data, num, i)
        return out

    def get_dv_zdt(variable_data: list, num: int):
        """
        :param variable_data: все объекты моделирования
        :param num: номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_data элементов на num-ый элемент по z
        """

        out = 0.0

        for i in range(len(modelling_elements)):
            if num != i:
                out += modelling_elements[i].work_with_z(not_variable_data, variable_data, num, i)
        return out

    def move_func(variable, t):
        """
        :param variable: все изменияемые данные объектов моделирования
        :param t: linspace переода времяни
        :return: outs: решение диференциального уравнения
        """
        # Лист возвращяемых данных
        # Переод = 6
        # Элементы объекта: 0 = dxdt, 1 = dv_xdt, 2 = dydt, 3 = dv_ydt, 4 = dzdt, 5 = dv_zdt
        outs = []

        bar.index = t*1000
        bar.update()

        # Для каждего моделируемого объекта вычислем возвращяемые даннные
        for j in range(len(modelling_elements)):
            # Вычисляем dxdt
            outs.append(variable[j * 6 + 1])
            # Вычисляем dv_xdt
            outs.append(get_dv_xdt(variable, j))
            # Вычисляем dydt
            outs.append(variable[j * 6 + 3])
            # Вычисляем dv_ydt
            outs.append(get_dv_ydt(variable, j))
            # Вычисляем dzdt
            outs.append(variable[j * 6 + 5])
            # Вычисляем dv_zdt
            outs.append(get_dv_zdt(variable, j))

        return outs

    def add_mas_data():
        for i in modelling_elements:
            not_variable_data.append(i.mass)
            not_variable_data.append(i.electric_charge)

            variable_data.append(i.x)
            variable_data.append(i.v_x)
            variable_data.append(i.y)
            variable_data.append(i.v_y)
            variable_data.append(i.z)
            variable_data.append(i.v_z)

    t = np.linspace(start_time, stop_time, frames)

    # Лист не изменяемых данных моделируемых объектов
    # Период = 2
    # Данные одного моделируемого объекта: 0 = масса, 1 = зарят
    not_variable_data = []

    # Лист изменяемых данных моделируемых объектов
    # Период = 6
    # Данные одного моделируемого объекта: 0 = x, 1 = вектор x, 2 = y, 3 = вектор y, 4 = z, 5 = вектрор z
    variable_data = []

    add_mas_data()

    # Моделируем
    sol = odeint(move_func, variable_data, t)
    bar.finish()

    return sol
