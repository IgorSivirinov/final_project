from IModellingElement import IModellingElement
from constant import G, k

class ElectricField(IModellingElement):

    Ex: float
    Ey: float
    Ez: float

    Bx: float
    By: float
    Bz: float

    def __init__(self, mass, Ex, Ey, Ez, Bx, By, Bz, x, v_x, y, v_y, z, v_z):

        self.Ex = Ex
        self.Ey = Ey
        self.Ez = Ez

        self.Bx = Bx
        self.By = By
        self.Bz = Bz

        self.x = x
        self.v_x = v_x
        self.y = y
        self.v_y = v_y
        self.z = z
        self.v_z = v_z

        self.mass = mass
        self.electric_charge = 0

    def work_with_x(self, not_variable_data: list, variable_data: list, num: int, i: int):
        """
        :param i:
        :param variable_data - все объекты моделирования
        :param num - номер объекта на который дейсвуют другие тела
        :return out: взаимодействие variable_data элементов на num-ый элемент по x
        """

        it_x = variable_data[i * 6 + 0]
        it_y = variable_data[i * 6 + 2]
        it_z = variable_data[i * 6 + 4]

        m = not_variable_data[num * 2 + 0]
        q = not_variable_data[num * 2 + 1]
        x = variable_data[num * 6 + 0]
        y = variable_data[num * 6 + 2]
        z = variable_data[num * 6 + 4]
        v_x = variable_data[num * 6 + 1]
        v_y = variable_data[num * 6 + 3]
        v_z = variable_data[num * 6 + 5]

        out = 0.0

        if i != num:
            # Вычисляем гравитационное взаимодействие variable_data элементов на num-ый элемент
            if ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5 != 0:
                out += (-G * self.mass * (x - it_x) / ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5)

            if (self.Ex + v_y * self.Bz - self.By * v_z) != 0:
                out += q / m * (self.Ex + v_y * self.Bz - self.By * v_z)

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

        m = not_variable_data[num * 2 + 0]
        q = not_variable_data[num * 2 + 1]
        x = variable_data[num * 6 + 0]
        y = variable_data[num * 6 + 2]
        z = variable_data[num * 6 + 4]
        v_x = variable_data[num * 6 + 1]
        v_y = variable_data[num * 6 + 3]
        v_z = variable_data[num * 6 + 5]

        out = 0.0

        if i != num:
            # Вычисляем гравитационное взаимодействие variable_data элементов на num-ый элемент
            if ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5 != 0:
                out += (-G * self.mass * (y - it_y) / ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5)

            if (self.Ey + v_x * self.Bx - self.Bz * v_x) != 0:
                out += q / m * (self.Ey + v_x * self.Bx - self.Bz * v_x)

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

        m = not_variable_data[num * 2 + 0]
        q = not_variable_data[num * 2 + 1]
        x = variable_data[num * 6 + 0]
        y = variable_data[num * 6 + 2]
        z = variable_data[num * 6 + 4]
        v_x = variable_data[num * 6 + 1]
        v_y = variable_data[num * 6 + 3]
        v_z = variable_data[num * 6 + 5]

        out = 0.0

        if i != num:
            # Вычисляем гравитационное взаимодействие variable_data элементов на num-ый элемент
            if ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5 != 0:
                out += (-G * self.mass * (z - it_z) / ((x - it_x) ** 2 + (y - it_y) ** 2 + (z - it_z) ** 2) ** 1.5)

            if (self.Ez + v_x * self.By - self.Bx * v_y) != 0:
                out += q / m * (self.Ez + v_x * self.By - self.Bx * v_y)

        return out

