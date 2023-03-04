import roboticstoolbox as rp

class model_robot:

    def __init__(self):
        self.robot_analisis_1 = rp.models.Panda()
        self.robot_analisis_2 = rp.models.Puma560()
        
    def create_model(self):

        print(rp.models.DH.Panda())

        self.robot_analisis_1.q = self.robot_analisis_1.qr
        # print(self.robot_analisis_1.q, type(self.robot_analisis_1.q)) #<class 'numpy.ndarray'>