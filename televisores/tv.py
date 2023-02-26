   
class TV():
    numTV = 0
    def __init__(self,marca,estado):
        self.marca = marca
        self.estado = estado
        self.volumen = 1
        self.canal =1
        self.precio = 500
        self.control  = None
        TV.numTV+=1
        

    # Metodos get
    def getMarca(self):
        return self.marca
    def getControl(self):
        return self.control
    def getPrecio(self):
        return self.precio
    def getVolumen(self):
        return self.volumen
    def getMarca(self):
        return self.marca
    def getNumTV():
        return TV.numTV
    def getEstado(self):
        return self.estado
    
    # metodos set

    def setMarca(self,marca):
        self.marca = marca
    def setControl(self,control):
        self.control = control
    def setPrecio(self,precio):
        self.precio = precio
    def setVolumen(self,volumen):
        self.volumen = volumen
    def setMarca(self,marca):
        self.marca = marca
    def setNumTV(numTV):
        TV.numTV = numTV

    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado == True and self.canal!=120:
            self.canal +=1

    def canalDown(self):
        if self.estado == True and self.canal!=1:
            self.canal -=1

    def setCanal(self,canal):
        if self.estado == True and canal <=120 and canal >=1:
            self.canal = canal

    def getCanal(self):
        return self.canal

    def volumenUp(self):
        if self.estado == True and self.volumen!=7:
            self.volumen +=1

    def volumenDown(self):
        if self.estado == True and self.volumen!=0:
            self.volumen -=1
