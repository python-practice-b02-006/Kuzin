# coding: utf-8

"""Visualization module
"""

header_font = "Arial-16"
window_width = 800
window_height = 800


def draw_object(space, obj):
    """Создаёт отображаемый объект.

    Параметры:

    **space** — холст для рисования.
    **obj** — объект.
    """
    x = obj.x
    y = obj.y
    r = obj.R
    #add draw
    pass
    
def draw_button(space, button):
    """Создаёт отображаемый объект кнопки.

    Параметры:

    **space** — холст для рисования.
    **button** — объект кнопки.
    """
    #add draw
    pass


def update_object_position(space, body):
    """Перемещает отображаемый объект на холсте.

    Параметры:

    **space** — холст для рисования.
    **body** — тело, которое нужно переместить.
    """
    pass

if __name__ == "__main__":
    print("This module is not for direct call!")
