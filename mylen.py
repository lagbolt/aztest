import math

def mylen(s, x, y, z):
    l = len(s)
    x, y = (y, x) if z < 0 else (x, y)
    z = abs(z)
    x = l-x if x < 0 else x
    x = x % z if x < 0 else x
    y = l-y if y < 0 else y
    # y = y - z * math.ceil((y - l) / z) if y > l else y
    y = y - z*((y-l)//z) if y > l else y 
    return math.ceil((y-x) / z) if (y-x)*z > 0 else 0


s = "abcdefghij"

for x in range(-15, 16, 3):
    for y in range(-15, 16, 3):
        for z in list(range(-6, 0)) + list(range(1, 7)):
            if (a := mylen(s, x, y, z)) != (b := len(s[x:y:z])):
                print("BAD", x, y, z, a, b)