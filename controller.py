import roboticstoolbox as rp
import spatialmath as sm
import numpy as np
import time

from view import view_robot
from model import model_robot

class dynamic:

    def robot_static(self):
        vista_2 = view_robot()
        vista_2.launch_view()
        vista_2.incluir_robot()

    def movement(self):

        modelo = model_robot()
        vista = view_robot()
        
        modelo.robot_analisis_1.q = modelo.robot_analisis_1.qr
 
        # Forward kinematics
        Tep = modelo.robot_analisis_1.fkine(modelo.robot_analisis_1.q) * sm.SE3.Trans(0.2, 0.2, 0.45)
        vista.launch_view()
        vista.env.add(modelo.robot_analisis_1)
    
        arrived = False
        dt = 0.05

        while not arrived:
            v, arrived = rp.p_servo(modelo.robot_analisis_1.fkine(modelo.robot_analisis_1.q),Tep, 1)
            modelo.robot_analisis_1.qd = np.linalg.pinv(modelo.robot_analisis_1.jacobe(modelo.robot_analisis_1.q)) @ v   
            vista.env.step(dt)
        vista.env.hold() # from here you can no longer write code scripts

if __name__ == "__main__":
    print("\nDENAVIT-HARTENBERG OF THE ROBOT")
    print("---------------------------------\n")
    modelo = model_robot()
    modelo.create_model()
    time.sleep(2) # seconds delay
    print("\nSTATIC MODEL IN PROCESS .................")
    # print("---------------------------------\n")
    static = dynamic()
    static.robot_static()
    time.sleep(4) # seconds delay
    print("\nDYNAMIC MODEL IN PROCESS ................")
    # print("---------------------------------\n")
    dinamica = dynamic()
    dinamica.movement()