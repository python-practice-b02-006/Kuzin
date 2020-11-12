# coding: utf-8

def calculate_force(body, space_objects):
    """Calculate force that move object.


    **body** — Object that force move.
    **space_objects** — list of objects that make force.
    """




def move(body, dt):
    """Function that move object

    **body** — Object to move.
    """
    pass


def objects_positions(space_objects, dt):
    """Recalculate objects coords.

    **space_objects** — list of objects which coords need to recalculate.
    **dt** — time step
    """
    pass

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        movet(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
