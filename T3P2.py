from CoolProp.CoolProp import PropsSI as prop
from CoolProp.CoolProp import PhaseSI as fase
from matplotlib import pyplot as plot
from tabulate import tabulate

P = 'P'
Q = 'Q'
T = 'T'
S = 'S'
H = 'H'
fluidos = ['water']
eficiencia = {}
trabajo_neto = {}
for fluido in fluidos:
    p = {}
    t = {}
    h = {}
    s = {}
    q = {}
    p[1] = 0.008 * (10**6)
    p[2] = 0.3 * (10**6)
    p[3] = 0.3 * (10**6)
    p[4] = 8 * (10**6)
    p[5] = 8 * (10**6)
    p[6] = 8 * (10**6)
    p[7] = 0.7 * (10**6)
    p[8] = 0.7 * (10**6)
    p[9] = 2 * (10**6)
    p[10] = 2 * (10**6)
    p[11] = 0.3 * (10**6)
    p[12] = 0.3 * (10**6)
    p[13] = 0.008 * (10**6)
    q[1] = 0
    q[3] = 0
    q[10] = 0
    t[5] = 205 + 273.15
    t[6] = 480 + 273.15
    t[8] = 440 + 273.15
    s[1] = prop('S', 'P', p[1], 'Q', q[1], fluido)
    s[2] = s[1]
    s[3] = prop('S', 'P', p[3], 'Q', q[3], fluido)
    s[4] = s[3]
    s[6] = prop('S', 'T', t[6], 'P', p[6], fluido)
    s[7] = s[6]
    q[7] = prop('Q', 'P', p[7], 'S', s[7], fluido)
    s[9] = s[6]
    s[8] = prop('S', 'T', t[8], 'P', p[8], fluido)
    s[12] = s[8]
    s[13] = s[8]
    h[10] = prop('H', 'P', p[10], 'Q', q[10], fluido)
    h[11] = h[10]
    q[11] = prop('Q', 'P', p[11], 'H', h[11], fluido)
    q[13] = prop('Q', 'P', p[13], 'S', s[13], fluido)
    t[1] = prop('T', 'P', p[1], 'Q', q[1], fluido)
    t[2] = prop('T', 'P', p[2], 'S', s[2], fluido)
    t[3] = prop('T', 'P', p[3], 'Q', q[3], fluido)
    t[4] = prop('T', 'P', p[4], 'S', s[4], fluido)
    t[7] = prop('T', 'P', p[7], 'S', s[7], fluido)
    t[9] = prop('T', 'P', p[9], 'S', s[9], fluido)
    t[10] = prop('T', 'P', p[10], 'H', h[10], fluido)
    t[11] = prop('T', 'P', p[11], 'H', h[11], fluido)
    t[12] = prop('T', 'P', p[12], 'S', s[12], fluido)
    t[13] = prop('T', 'P', p[13], 'S', s[13], fluido)

    for i in range(1, 14):
        if i in q.keys():
            if i not in s.keys():
                s[i] = prop('S', 'P', p[i], 'Q', q[i], fluido)
            if i not in h.keys():
                h[i] = prop('H', 'P', p[i], 'Q', q[i], fluido)
        else:
            if i not in s.keys():
                s[i] = prop('S', 'P', p[i], 'T', t[i], fluido)
            if i not in h.keys():
                h[i] = prop('H', 'P', p[i], 'T', t[i], fluido)
    lista = [['Punto', 'T [°C]', 'P [Pa]',  's [J/kgK]', 'h [J/kg]']]
    for i in range(1, 14):
        lista.append([i, t[i]-273.15, p[i], s[i], h[i]])
    print('\n')
    print(fluido.upper())
    print(tabulate(lista, headers='firstrow', tablefmt='latex'))

rango = list(range(374))
printeable1 = []
printeable2 = []
for j in rango:
    printeable1.append(prop('S', 'T', j + 273.15, 'Q', 0, fluido))
    printeable2.append(prop('S', 'T', j + 273.15, 'Q', 1, fluido))
lista_eses = [s[i + 1] for i in range(13)]
lista_tes = [t[i + 1] - 273.15 for i in range(13)]

plot.figure()
plot.plot(printeable2, rango)
plot.plot(printeable1, rango)

plot.scatter(lista_eses, lista_tes)

for i, txt in enumerate(lista_eses):
    plot.annotate(f'{i+1}', (lista_eses[i], lista_tes[i]))
plot.ylabel('Temperatura °C')
plot.xlabel('S')
plot.tight_layout()
plot.show()
