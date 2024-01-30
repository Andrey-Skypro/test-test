class Smartphone :
    def __init__(self, марка_телефона, модель_телефона, абонентский_номер):
        print("производитель", марка_телефона)
        print("модель", модель_телефона)
        print("номер", абонентский_номер)

smartphone1 = Smartphone("nokian", "n95", "+79211234567")        
smartphone2 = Smartphone("erisson", "f22", "+79111234567")
smartphone3 = Smartphone("xiaomi", "redmi", "+79871234567")