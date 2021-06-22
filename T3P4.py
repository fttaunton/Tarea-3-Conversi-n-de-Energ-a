from CoolProp.CoolProp import PropsSI as prop
from CoolProp.CoolProp import PhaseSI as fase
from matplotlib import pyplot as plot
from tabulate import tabulate


temperaturas = [i for i in range(500)]
presiones = [i for i in range(1, 10)]
ss = []
puntos = {}
for j in presiones:
    ss.append([])
    for i in temperaturas:
        ss[j - 1].append(prop('S', 'P', j * (10 ^ 3), 'T', i + 273.15, 'air'))

plot.figure()

for presion in ss:
    plot.plot(presion, temperaturas)
plot.grid()
plot.ylabel('Temperatura °C')
plot.xlabel('S')
plot.tight_layout()
plot.show()
