class Termometr:
    def __init__(self, celsius):
        self.__celsius = celsius
        self.__history = []
        self.__history.append(celsius)


    @property
    def celsius(self):
        return self.__celsius
    @property
    def fahrenheit(self):
        return (self.celsius*(9/5)+32)
    @celsius.setter
    def celsius(self, value):
        if value > -273.15:
            self.__celsius = value
            self.__history.append(value)

    def get_history(self):
        return self.__history.copy()
    
t = Termometr(25)
print(t.celsius)                              #→ 25
print(t.fahrenheit)                           #→ 77.0
t.celsius = 30                        #→ celsius=30, fahrenheit=86.0, история [25,30]
t.celsius = -300                     # → "Ошибка: ниже абсолютного нуля", значение 30
#print(t.__celsius)                            #→ AttributeError
print(t.get_history())                        #→ [25, 30]
hist = t.get_history()
hist.append(999)
print(t.get_history())                    # → [25, 30]
