from IModellingElement import IModellingElement
from constant import G, k, mu
from enum import Enum


class Magnet(IModellingElement):
    class Orientation(Enum):
        BY_X = 1
        BY_Y = 2
        BY_Z = 3

    orientation: Orientation

    mu_d: float

    def __init__(self, orientation: Orientation, mu_d: float, mass: float, x, v_x, y, v_y, z, v_z):

        self.orientation = orientation
        self.mu_d = mu_d

        self.electric_charge = 0
        self.mass = mass

        self.x = x
        self.v_x = v_x

        self.y = y
        self.v_y = v_y

        self.z = z
        self.v_z = v_z

    def work_with_x(self, not_variable_data: list, variable_data: list, num: int, i: int):
        """
        :param variable_data - все объекты моделирования
        :param num - номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_data элементов на num-ый элемент по x
        """



        it_x = variable_data[i * 6 + 0]
        it_y = variable_data[i * 6 + 2]
        it_z = variable_data[i * 6 + 4]

        if self.orientation == self.Orientation.BY_Y:
            it_z, it_y = it_y, it_z
        elif self.orientation == self.Orientation.BY_X:
            it_z, it_x = it_x, it_z

        m = not_variable_data[num * 2 + 0]
        q = not_variable_data[num * 2 + 1]
        x = variable_data[num * 6 + 0]
        y = variable_data[num * 6 + 2]
        z = variable_data[num * 6 + 4]
        v_y = variable_data[num * 6 + 3]
        v_z = variable_data[num * 6 + 5]

        out = 0.0

        if i != num:
            # Вычисляем гравитационное взаимодействие variable_data элементов на num-ый элемент
            if ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5 != 0:
                out += (-G * self.mass * (x - it_x) / ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5)

            if (((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2)) != 0:
                By = ((3 * (y - it_y) * (z - it_z) * self.mu_d) * mu) / (
                            ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2))
                Bz = ((2 * (z - it_z) ** 2 - (x - it_x) ** 2 - (y - it_y) ** 2) * self.mu_d * mu) / (
                            ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2))

                if (v_y * Bz - By * v_z) != 0:
                    out += q / m * (v_y * Bz - By * v_z)
        return out

    def work_with_y(self, not_variable_data: list, variable_data: list, num: int, i: int):
        """
        :param variable_balls: все объекты моделирования
        :param num: номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_balls элементов на num-ый элемент по y
        """

        it_x = variable_data[i * 6 + 0]
        it_y = variable_data[i * 6 + 2]
        it_z = variable_data[i * 6 + 4]

        if self.orientation == self.Orientation.BY_Y:
            it_z, it_y = it_y, it_z
        elif self.orientation == self.Orientation.BY_X:
            it_z, it_x = it_x, it_z

        m = not_variable_data[num * 2 + 0]
        q = not_variable_data[num * 2 + 1]
        x = variable_data[num * 6 + 0]
        y = variable_data[num * 6 + 2]
        z = variable_data[num * 6 + 4]
        v_x = variable_data[num * 6 + 1]
        v_z = variable_data[num * 6 + 5]

        out = 0.0

        if i != num:
            # Вычисляем гравитационное взаимодействие variable_data элементов на num-ый элемент
            if ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5 != 0:
                out += (-G * self.mass * (y - it_y) / ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5)

            if (((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2)) != 0:
                Bx = (3 * (x - it_x) * (z - it_z) * self.mu_d * mu) / (
                            ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2))
                Bz = ((2 * (z - it_z) ** 2 - (x - it_x) ** 2 - (y - it_y) ** 2) * self.mu_d * mu) / (
                        ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2))
                if (v_z * Bx - Bz * v_x) != 0:
                    out += q / m * (v_z * Bx - Bz * v_x)
        return out

    def work_with_z(self, not_variable_data: list, variable_data: list, num: int, i: int):
        """
        :param variable_balls: все объекты моделирования
        :param num: номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_balls элементов на num-ый элемент по z
        """

        it_x = variable_data[i * 6 + 0]
        it_y = variable_data[i * 6 + 2]
        it_z = variable_data[i * 6 + 4]

        if self.orientation == self.Orientation.BY_Y:
            it_z, it_y = it_y, it_z
        elif self.orientation == self.Orientation.BY_X:
            it_z, it_x = it_x, it_z

        m = not_variable_data[num * 2 + 0]
        q = not_variable_data[num * 2 + 1]
        x = variable_data[num * 6 + 0]
        y = variable_data[num * 6 + 2]
        z = variable_data[num * 6 + 4]
        v_x = variable_data[num * 6 + 1]
        v_y = variable_data[num * 6 + 3]

        out = 0.0

        if i != num:
            # Вычисляем гравитационное взаимодействие variable_data элементов на num-ый элемент
            if ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5 != 0:
                out += (-G * self.mass * (z - it_z) / ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5)

            if (((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2)) != 0:
                Bx = (3 * (x - it_x) * (z - it_z) * self.mu_d * mu) / (
                            ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2))
                By = ((3 * (y - it_y) * (z - it_z) * self.mu_d) * mu) / (
                            ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** (5 / 2))
                if (v_x * By - Bx * v_y) != 0:
                    out += q / m * (v_x * By - Bx * v_y)
        return out
