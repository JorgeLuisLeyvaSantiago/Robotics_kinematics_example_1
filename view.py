import swift
from model import model_robot

# from main import panda, Tep

class view_robot:

    # def __init__(self):
    #     self.env = swift.Swift()

    def launch_view(self):
        self.env = swift.Swift()
        self.env.launch(realtime=True)

    def incluir_robot(self):
        robot1 = model_robot()
        robot_analisis = robot1.robot_analisis_1
        self.env.add(robot_analisis)
        # self.env.hold()