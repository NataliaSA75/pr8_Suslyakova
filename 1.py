class soda:
    def __init__(self, name, dobavka):
        self.__dobavka = dobavka
        self.__name = name
    def show_my_drink(self):
        if self.__dobavka != "":
            print(f"{self.__name} и {self.__dobavka}")
        else:
            print("Обычная газировка")

s = soda("soda", "e1234")
s.show_my_drink()

s2 = soda("Газировка", "")
s2.show_my_drink()