# coding: utf-8

from solar_objects import Object
input_filename = 'solar_system'
output_filename = 'statistics'

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    #return objects
    
    pass

def parse_object_parameters(line, obj):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание объекта.
    **obj** — объект.
    """
    obj.R = int(line.split()[1])
    obj.color = line.split()[2]
    obj.m = float(line.split()[3])
    obj.x = float(line.split()[4])
    obj.y = float(line.split()[5])
    obj.Vx = float(line.split()[6])
    obj.Vy = float(line.split()[7])
    
    pass


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    pass

if __name__ == "__main__":
    print("This module is not for direct call!")
