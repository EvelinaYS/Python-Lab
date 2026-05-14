import math

def run():
    radius = 42

    area = round(math.pi * radius ** 2, 4)

    print(area)

    point_1 = (23, 34)
    point_2 = (30, 30)

    d1 = math.sqrt(point_1[0] ** 2 + point_1[1] ** 2)
    d2 = math.sqrt(point_2[0] ** 2 + point_2[1] ** 2)

    print(d1 <= radius)
    print(d2 <= radius)

if __name__ == '__main__':
    run()