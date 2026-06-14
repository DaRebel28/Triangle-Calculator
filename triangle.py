# John Burghardt
import os
from math import pi, sqrt, sin, cos, asin, acos
a = None
b = None
c = None
A = None
B = None
C = None
while True :
    os.system('clear')
    print("Triangle Dimensions Calculator")
    print("Enter three sides, two sides and the angle between, or two angles and a side.")
    print("Enter length in meters. Enter angle in degrees.")
    print("  /A\\ ")
    print("c/   \\b")
    print("/B   C\\")
    print("-------")
    print("   a   ")
    if ((isinstance(a, float) and isinstance(b, float) and isinstance(c, float)) and (not (a + b > c) or not (a + c > b) or not (b + c > a))) or (a == "" and b == "" and c == "") :
        a = None
        b = None
        c = None
        continue
    if isinstance(a, float) and isinstance(b, float) and isinstance(c, float) :
        A = acos((b**2 + c**2 - a**2) / (2 * b * c)) * 180 / pi
        B = acos((a**2 + b**2 - c**2)/(2 * a * c)) * 180 / pi
    if isinstance(A, float) and isinstance(B, float) and not isinstance(C, float) :
        C = 180 - A - B
    elif isinstance(A, float) and isinstance(C, float) and not isinstance(B, float) :
        B = 180 - A - C
    elif isinstance(B, float) and isinstance(C, float) and not isinstance(A, float) :
        A = 180 - B - C
    if isinstance(A, float) and isinstance(B, float) and isinstance(a, float) and not isinstance(b, float) :
        b = a * sin(B * pi / 180) / sin(A * pi / 180)
        c = a * sin(C * pi / 180) / sin(A * pi / 180)
    elif isinstance(A, float) and isinstance(B, float) and isinstance(b, float) and not isinstance(a, float) :
        a = b * sin(A * pi / 180) / sin(B * pi / 180)
        c = b * sin(C * pi / 180) / sin(B * pi / 180)
    elif isinstance(A, float) and isinstance(B, float) and isinstance(c, float) and not isinstance(a, float) :
        a = c * sin(A * pi / 180) / sin(C * pi / 180)
        b = c * sin(B * pi / 180) / sin(C * pi / 180)
    elif isinstance(A, float) and isinstance(C, float) and isinstance(a, float) and not isinstance(b, float) :
        b = a * sin(B * pi / 180) / sin(A * pi / 180)
        c = a * sin(C * pi / 180) / sin(A * pi / 180)
    elif isinstance(A, float) and isinstance(C, float) and isinstance(b, float) and not isinstance(a, float) :
        a = b * sin(A * pi / 180) / sin(B * pi / 180)
        c = b * sin(C * pi / 180) / sin(B * pi / 180)
    elif isinstance(A, float) and isinstance(C, float) and isinstance(c, float) and not isinstance(a, float) :
        a = c * sin(A * pi / 180) / sin(C * pi / 180)
        b = c * sin(B * pi / 180) / sin(C * pi / 180)
    elif isinstance(B, float) and isinstance(C, float) and isinstance(a, float) and not isinstance(b, float) :
        b = a * sin(B * pi / 180) / sin(A * pi / 180)
        c = a * sin(C * pi / 180) / sin(A * pi / 180)
    elif isinstance(B, float) and isinstance(C, float) and isinstance(b, float) and not isinstance(a, float) :
        a = b * sin(A * pi / 180) / sin(B * pi / 180)
        c = b * sin(C * pi / 180) / sin(B * pi / 180)
    elif isinstance(B, float) and isinstance(C, float) and isinstance(c, float) and not isinstance(a, float) :
        a = c * sin(A * pi / 180) / sin(C * pi / 180)
        b = c * sin(B * pi / 180) / sin(C * pi / 180)
    if isinstance(a, float) and isinstance(b, float) and isinstance(C, float) and not isinstance(c, float) :
        c = sqrt(a**2 + b**2 - 2 * a * b * cos(C * pi / 180))
        A = asin(a * sin(C * pi / 180) / c)
    elif isinstance(a, float) and isinstance(c, float) and isinstance(B, float) and not isinstance(b, float) :
        b = sqrt(a**2 + c**2 - 2 * a * c * cos(B * pi / 180))
        A = asin(a * sin(B * pi / 180) / b)
    elif isinstance(b, float) and isinstance(c, float) and isinstance(A, float) and not isinstance(a, float) :
        a = sqrt(b**2 + c**2 - 2 * b * c * cos(A * pi / 180))
        B = asin(b * sin(A * pi / 180) / a)
    if a == None :
        a = input("Enter a: ")
        if a != "" :
            try :
                a = float(a)
                if a <= 0 :
                    a = None
            except :
                a = None
        continue
    elif a != "" :
        print("a = " + str(a) + " m")
    if b == None :
        b = input("Enter b: ")
        if b != "" :
            try :
                b = float(b)
                if b <= 0 :
                    b = None
            except :
                b = None
        continue
    elif b != "" :
        print("b = " + str(b) + " m")
    if c == None :
        c = input("Enter c: ")
        if c != "" :
            try :
                c = float(c)
                if c <= 0 :
                    c = None
            except :
                c = None
        continue
    elif c != "" :
        print("c = " + str(c) + " m")
    if a == b and b == c :
        A = 60
        B = 60
        C = 60
    if A == None :
        A = input("Enter A: ")
        if A != "" :
            try :
                A = float(A)
                if A <= 0 or A >= 180 :
                    A = None
            except :
                A = None
        continue
    elif A != "" :
        print("A = " + str(A) + "°")
    if B == None :
        B = input("Enter B: ")
        if B != "" :
            try :
                B = float(B)
                if B <= 0 or B >= 180 :
                    B = None
            except :
                B = None
        continue
    elif B != "" :
        print("B = " + str(B) + "°")
    if C == None :
        C = input("Enter C: ")
        if C != "" :
            try :
                C = float(C)
                if C <= 0 or C >= 180 :
                    C = None
            except :
                C = None
        continue
    elif C != "" :
        print("C = " + str(C) + "°")
    if (A == 60 and B == 60 and C == 60) :
        if a != "" and b != "" and c != "" :
            break
        if a != "" :
            b = a
            c = a
        if b != "" :
            a = b
            c = b
        if c != "" :
            a = c
            b = c
        continue
    if (((not isinstance(A, float) and not isinstance(B, float) and isinstance(C, float)) and 
         (not isinstance(a, float) or not isinstance(b, float) or isinstance(c, float))) or
        (not isinstance(a, float) and not isinstance(A, float)) or
        (not isinstance(b, float) and not isinstance(B, float)) or
        (not isinstance(c, float) and not isinstance(C, float))) :
        a = None
        b = None
        c = None
        A = None
        B = None
        C = None
        continue
    break
print("Perimeter = " + str(a + b + c) + " m")
print("Area = " + str(a * b * sin(C * pi / 180) / 2) + " m")
print("Height = " + str(b * sin(C * pi / 180)) + " m")