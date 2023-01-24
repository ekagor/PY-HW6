# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между ними в 2D пространстве.

from functools import reduce
point_a = list(map(int, input('Введите две координаты точки A, через пробел: ').split()))
point_b = list(map(int, input('Введите две координаты точки B, через пробел: ').split()))
def point_range(point_a, point_b):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda point: (point[1] - point[0])**2, zip(point_a, point_b))))
     return round(rng, 2)
print(point_range(point_a, point_b))