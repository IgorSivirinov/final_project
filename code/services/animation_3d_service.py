import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import FuncAnimation
from typing import List
from code.models.IModellingElement import IModellingElement
from code.models.ProgressBar import ProgressBar

def animation(frames:  int, start_time: float, stop_time: float, sol: list, modelling_elements: List[IModellingElement]):
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    bar = ProgressBar(" Animation", max=frames)

    # Лист графических элементов моделируемых объектов
    # Переод = 2
    # Данные одного моделируемого объекта: 0 = шар, 1 = путь
    plots = []

    def solve_func(i: float, n: int):
        """
        :param i: время в которое мы берём координаты
        :param n: номер моделируемого объекта для которого мы получаем координаты
        :return x, y, z: n-го моделируемого элемента в i-е время
        """
        x = sol[i, n * 6 + 0]
        y = sol[i, n * 6 + 2]
        z = sol[i, n * 6 + 4]

        return x, y, z

    def solve_func_line(i: float, n: int):
        """
        :param i: время в которое мы берём координаты
        :param n: номер моделируемого объекта для которого мы получаем координаты
        :return x, y, z: n-го моделируемого элемента в i-е время
        """
        x = sol[:i, n * 6 + 0]
        y = sol[:i, n * 6 + 2]
        z = sol[:i, n * 6 + 4]

        return x, y, z

    # Создаём для каждего моделируемого объекта графические элементы
    for i in modelling_elements:
        # создаём рандомный цвет
        if i.electric_charge < 0:
            color = 'b'
        elif i.electric_charge > 0:
            color = 'r'
        else:
            color = 'k'

        # создаём графический элемент "шар"
        plot, = ax.plot([], [], [], 'o', color=color, ms=5)
        plots.append(plot)

        # создаём графический элемент "лия"
        plot2, = ax.plot([], [], [], '-', color=color)
        plots.append(plot2)


    def animation_func(i):
        """
        Моделируем для каждего моделируемого объека графические элементы

        :param i: время в которое мы берём координаты
        """
        bar.next()
        for j in range(len(modelling_elements)):

            solve = solve_func(i, j)
            plots[j * 2 + 0].set_data(solve[0], solve[1])
            plots[j * 2 + 0].set_3d_properties(solve[2])

            solve_line = solve_func_line(i, j)
            plots[j * 2 + 1].set_data(solve_line[0], solve_line[1])
            plots[j * 2 + 1].set_3d_properties(solve_line[2])

    qu = 15

    ax.set_xlim3d([-qu, qu])
    ax.set_xlabel('X')

    ax.set_ylim3d([-qu, qu])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-qu, qu])
    ax.set_zlabel('Z')

    ani = FuncAnimation(fig, animation_func, frames, interval=50)

    # ani.save("tipo.gif")

    plt.show()
    ani.save("tipo4.gif")
    bar.finish()

