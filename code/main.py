from model.Electron import Electron
from model.ElectricField import ElectricField
from services import animation_3d_service, calculation_3d_service

frames = 1500
start = 0
stop = 0.0000001

elements = [
            Electron(0.001, 10**7, 0.001, 10**6, 0, 0),
            # Electron.Electron(5, 0, -10, 0, 9, -7),
            Electron(-0.001, -10**7, -0.001, -10**6, 0, 0),
            ElectricField(1,
                          0.01, 0, 0,
                          0, 0.02, 0,
                          0, 0, 0, 0, 0, 0),
            # Electron.Electron(10, 56, -10, 0, 10, 20),
            # Magnet(Magnet.Orientation.BY_Y, 5000000000000, 2, -20, 0, 3, 0, 0, 0),
            # Magnet(Magnet.Orientation.BY_Z, 1000000000000, 10, 0, 0, 0, 0, 0, 0)
            ]

sol = calculation_3d_service.calculation_coordinate(frames, start, stop, elements)
animation_3d_service.animation(frames, start, stop, sol, elements)