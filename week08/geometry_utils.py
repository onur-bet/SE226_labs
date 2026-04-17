import math
def circle_area(radius):
    if radius<=0:
        return "enter a valid value"

    else: return math.pi*(radius**2)

def circle_perimeter(radius):
    if radius<=0:
        return "enter a valid value"
    else: return 2*math.pi*radius

def rectangle_area(width,height):
    if width<=0 or height<=0:
        return "enter a valid value"
    else: return width*height

def rectangle_perimeter(width,height):
    if width<=0 or height<=0:
        return "enter a valid value"
    else: return 2*(width+height)

def triangle_area(base,height):
    if base<=0 or height<=0:
        return "enter a valid value"
    else: return (base*height)/2
