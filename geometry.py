#This program contains functions that evaluate formulas used in geometry
#
#Tatem Pearson
#August 30, 2017

import math

def triangle_area(b,h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

# function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b,h):
    a = b * h
    return a

def trapezoid_area(a,b,h):
    a = (a+b)/2 *h
    return a

def rectangular_prism_volume(w,b,h):
    v = w * b * h
    return v

def cone_volume(r,h):
    v = math.pi * r **2 * (h/3)
    return v

def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v

print(parallelogram_area(5,9))
print(trapezoid_area(2,3,5))
print(rectangular_prism_volume(6,5,4))
print(cone_volume(5,15))
print(sphere_volume(16))

def rectangular_prism_sur_area(l,w,h):
    a = 2*(w * l + h * l + h * w)
    return a

def sphere_sur_area(r):
    a = 4 * math.pi * r**2
    return a

def right_triangle_hypotenuse(a,b):
    h = math.sqrt((a**2 + b**2))
    return h

print(rectangular_prism_sur_area(5,6,7))
print(sphere_sur_area(56))
print(right_triangle_hypotenuse(5,7))


