import roboticstoolbox as rp

class model_robot:

    # Model attributes
    def __init__(self):
        self.robot_analisis_0 = rp.models.AL5D()
        self.robot_analisis_1 = rp.models.Panda()
        self.robot_analisis_2 = rp.models.Puma560()

    def create_model_robot_PR2(self):
        print(rp.models.DH.AL5D())
        
    def create_model_robot_panda(self):
        print(rp.models.DH.Panda())
        self.robot_analisis_1.q = self.robot_analisis_1.qr
        # print(self.robot_analisis_1.q, type(self.robot_analisis_1.q)) #<class 'numpy.ndarray'>

    def create_model_robot_puma560(self):
        print(rp.models.DH.Puma560())
        self.robot_analisis_2.q = self.robot_analisis_2.qr