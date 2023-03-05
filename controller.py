import roboticstoolbox as rp
import spatialmath as sm
import numpy as np
import time

from view import view_robot
from model import model_robot

class dynamic:
    def robot_static_AL5D(self):
        vista_2 = view_robot()
        vista_2.launch_view()
        vista_2.incluir_robot_AL5D()

    def robot_static_panda(self):
        vista_2 = view_robot()
        vista_2.launch_view()
        vista_2.incluir_robot_panda()

    def robot_static_puma560(self):
        vista_2 = view_robot()
        vista_2.launch_view()
        vista_2.incluir_robot_puma560()

    def movement_robot_panda(self):

        modelo = model_robot()
        vista = view_robot()
        
        modelo.robot_analisis_1.q = modelo.robot_analisis_1.qr
 
        # Forward kinematics
        Tep = modelo.robot_analisis_1.fkine(modelo.robot_analisis_1.q) * sm.SE3.Trans(0.2, 0.2, 0.45)
        vista.launch_view()
        vista.env.add(modelo.robot_analisis_1)

        # variables for simulation
        arrived = False
        dt = 0.05

        while not arrived:
            v, arrived = rp.p_servo(modelo.robot_analisis_1.fkine(modelo.robot_analisis_1.q),Tep, 1)
            modelo.robot_analisis_1.qd = np.linalg.pinv(modelo.robot_analisis_1.jacobe(modelo.robot_analisis_1.q)) @ v   
            vista.env.step(dt)
        vista.env.hold() # from here you can no longer write code scripts

if __name__ == "__main__":

    print("\nSTATIC MODEL OF THE AL5D ROBOT IN PROCESS .................")
    static = dynamic()
    static.robot_static_AL5D()
    time.sleep(2) # seconds delay
    print("\nDENAVIT- HARTENBERG OF THE AL5D ROBOT")
    print("---------------------------------\n")
    time.sleep(2) # seconds delay
    modelo = model_robot()
    modelo.create_model_robot_PR2()
    time.sleep(2) # seconds delay
    print("\nSTATIC MODEL OF THE PUMA560 ROBOT IN PROCESS .................")
    static = dynamic()
    static.robot_static_puma560()
    time.sleep(2) # seconds delay
    print("\nDENAVIT- HARTENBERG OF THE PUMA560 ROBOT")
    print("---------------------------------\n")
    time.sleep(2) # seconds delay
    modelo = model_robot()
    modelo.create_model_robot_puma560()
    time.sleep(2) # seconds delay
    print("\nSTATIC MODEL OF THE PANDA ROBOT IN PROCESS .................")
    time.sleep(2) # seconds delay
    static = dynamic()
    static.robot_static_panda()
    time.sleep(2) # seconds delay
    print("\nDENAVIT- HARTENBERG OF THE PANDA ROBOT - BY FRANKA EMIKA")
    print("---------------------------------------------------------\n")
    time.sleep(2) # seconds delay
    modelo = model_robot()
    modelo.create_model_robot_panda()
    time.sleep(2) # seconds delay
    print("\nDYNAMIC MODEL OF THE PANDA ROBOT IN PROCESS ................")
    time.sleep(2) # seconds delay
    dinamica = dynamic()
    dinamica.movement_robot_panda()