import math
# H = Höhe
# v = Fallgeschwindigkeit in m/s

# h in m
h = int(input('h: '))
print(h, 'm Höhe')

# v in m/s
v = math.sqrt(2 * 9.81 * h)

# float to double
v_rounded = round(v, 2)
print(v_rounded, 'm/s', 'Fallgeschwindigkeit')

# v in km/h
kmh = v * 3.6

# float to double
kmh_rounded = round(kmh, 2)
print(kmh_rounded, 'km/h', 'Fallgeschwindkeit')






