class ViajeroFrecuente:
    def __init__(self, num, dni, nom, ap, mill):
        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ap
        self.__millas_acum=mill
    def cantidadTotalMillas(self):
        return self.__millas_acum
    def getNum(self):
        return self.__num_viajero
    def acumularMillas(self, millas):
        self.__millas_acum=self.__millas_acum+millas
        return self.__millas_acum
    def canjearMillas(self, cant):
        if ((cant<=self.__millas_acum)):
            self.__millas_acum=self.__millas_acum-cant
            print("Millas canjedas exitosamente")
        else:
            print('Error: La cantidad de millas acumuladas es menor que la cantidad de millas a canjear')
        return self.__millas_acum
    def __ad__(self,millas):
        self.__millas_acum += millas

    def __sub__(self,millas):
        self.__millas_acum -= millas

    def __gt__ (self,otroViajero):
        if(self.__millas_acum > otroViajero.getTotalMillas()):
            mayor = self.__millas_acum
        else:
            mayor = otroViajero.getTotalMillas()
        return (mayor)

    def __eq__(self,millas):
        return self.__millas_acum == millas