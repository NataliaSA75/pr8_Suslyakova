# Евгения создала класс KgToPounds с параметром kg, куда передается определенное количество килограмм,
# а с помощью метода to_pounds() они переводятся в фунты.
# Чтобы закрыть доступ к переменной “kg” она реализовала методы set_kg() - для задания нового значения килограммов, 
# get_kg() - для вывода текущего значения кг. 
# Из-за этого возникло неудобство: нам нужно теперь использовать эти 2 метода для задания и вывода значений. 
# Помогите ей переделать класс с использованием функции property() и свойств-декораторов. Код приведен ниже.

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg
    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы могут быть только числами!")
    
    def to_pounds(self, kg):
        return kg * 2.205
    
weight1 = KgToPounds(12)
print(weight1.to_pounds(weight1.kg))