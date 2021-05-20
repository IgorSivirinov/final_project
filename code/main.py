from code.models.Electron import Electron
from code.models.Magnet import Magnet
from code.models.Body import Body
from code.models.ElectricField import ElectricField
from services import animation_3d_service, calculation_3d_service

frames = 750
start = 0
stop = 10

elements = [
            Electron( 5, 20, -5, 0, 5, -10),
            # Electron( -10, 0, 10, 0, 10, -50),
            # Electron(0.001, 10**7, 0.001, 10**6, 0, 0),
            # # Electron.Electron(5, 0, -10, 0, 9, -7),
            # Electron(-0.001, -10**7, -0.001, -10**6, 0, 0),
            # ElectricField(1,
            #               0.00000000001, 0, 0,
            #               0, 0.0000000002, 0,
            #               0, 0, 0, 0, 0, 0),
            # Electron.Electron(10, 56, -10, 0, 10, 20),
            Magnet(Magnet.Orientation.BY_Z, 5, 1000, -10, 0, -3, 0, 0, 0),
            Magnet(Magnet.Orientation.BY_Z, 1, 200, 0, 0, 0, 0, 0, 0)
            ]

sol = calculation_3d_service.calculation_coordinate(frames, start, stop, elements)
animation_3d_service.animation(frames, start, stop, sol, elements)