
class Control():
    def __init__(self):
        pass
    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()
    
    def volumenDown(self):
        self.tv.volumenDown()

    def volumenUp(self):
        self.tv.volumenUp()
    
    def setCanal(self,canal):
        self.tv.setCanal(canal)

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def enlazar(self,tv):
        self.tv = tv
        tv.control = self
    
    def getTv(self):
        return self.tv
    
    def setTv(self,tv):
        self.tv = tv
        tv.control = self

