class Venicle:
    __COLORS_ven = ["ICE VINE", "RED", "BLUE", "Black", "Dark Gray",  "matterhorn", 'blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str,  model: str, color:str, engine_power:int):
        self.owner = owner
        self._model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model (self):
        return "Модель: " +  self._model

    def get_horsepower (self):
        return "Мощность двигателя: " +  str( self.__engine_power) + " л.с"
    def get_color (self):
        return "Цвет: " +  self.__color

    def print_info  (self):
        print( self.get_model () )
        print( self.get_horsepower () )
        print( self.get_color () )
        print(f"Владелец: {self.owner}")

    def set_color (self, new_color:str):
        for c in self.__COLORS_ven:
            #print(c.upper(),  new_color.upper())
            if new_color.upper() == c.upper():
                self.__color = c
                print(f"{self._model} перекрашен в цвет {new_color}" )
                return
        # если мы сюда пришли. то не выпали из цикла по break, т.е. подходящий цвет недоступен
        print(f"Цвет {new_color} недоступен для {self._model} ")
        #print(c.upper(), new_color.upper())



class Sedan (Venicle):
    __PASSENGERS_LIMIT = 5
    __DOORS = 4

class Hatchback (Venicle):
    __PASSENGERS_LIMIT = 5
    __DOORS = 4

class Fastback (Venicle):
    __PASSENGERS_LIMIT = 2
    __DOORS = 2

class Universal (Venicle):
    __PASSENGERS_LIMIT = 5
    __DOORS = 5


# НАчало основной программы


#SedRic = Sedan(owner ="DAV", model = "KR", color = "GREEN",  engine_power = 123)
#SedRic.print_info()
#SedRic.set_color ("ICE VINE")

#print(dir (SedRic))
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()






