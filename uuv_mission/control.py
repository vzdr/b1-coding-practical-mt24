class ControllerPD:

    def __init__(self, Kp, Kd):
        self.Kp = Kp
        self.Kd = Kd
    
    def control(self, error, previous_error):
        return self.Kp*error+self.Kd*(error-previous_error)