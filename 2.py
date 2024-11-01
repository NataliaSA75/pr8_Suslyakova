# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации): 
# – Ура, можно построить треугольник!; 
# – С отрицательными числами ничего не выйдет!; 
# – Нужно вводить только числа!; 
# – Жаль, но из этого треугольник не сделать.

class TriangleChecker:

    def __init__(self, first, second, third):
        self.__first = first
        self.__second = second
        self.__third = third
    def is_triangle(self):
        arr = [self.__first, self.__second, self.__third]
        n = 0
        try:
            for item in range(0, len(arr)):
                if int(arr[item]) < 0:
                    print("С отрицательными числами ничего не выйдет!")
                elif int(arr[item]) == 0:
                    print("Жаль, но из этого треугольник не сделать")
                else:
                    n+=1
            if n == 3:
                print("Ура, можно построить треугольник!")
        except(ValueError):
            print("Нужно вводить только числа!")


triangle1 = TriangleChecker("123", "xc", 123)
triangle1.is_triangle()

triangle2 = TriangleChecker("0", "123", 123)
triangle2.is_triangle()

triangle3 = TriangleChecker(-9, 3, 123)
triangle3.is_triangle()

triangle4 = TriangleChecker(9, 3, 123)
triangle4.is_triangle()