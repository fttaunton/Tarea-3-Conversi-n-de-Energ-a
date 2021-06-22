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
    p[1] = 10 * (10**3)
    q[1] = 0
    t[1] = prop('T', 'P', p[1], 'Q', q[1], fluido)
    s[1] = prop('S', 'T', t[1], 'Q', q[1], fluido)
    h[1] = prop('H', 'T', t[1], 'Q', q[1], fluido)

    p[2] = 8 * (10**6)
    s[2] = s[1]
    t[2] = prop('T', 'S', s[2], 'P', p[2], fluido)
    h[2] = prop('H', 'S', s[2], 'P', p[2], fluido)

    p[3] = 7.2 * (10**6)
    t[3] = 500 + 273.15
    s[3] = prop('S', 'T', t[3], 'P', p[3], fluido)
    h[3] = prop('H', 'T', t[3], 'P', p[3], fluido)

    p[4] = 11.111 * (10**3)
    s[4] = s[3]
    t[4] = prop('T', 'S', s[4], 'P', p[4], fluido)
    h[4] = prop('H', 'S', s[4], 'P', p[4], fluido)

    h[21] = (h[2] - h[1])/0.75 + h[1]
    t[21] = prop('T', 'H', h[21], 'P', p[2], fluido)
    s[21] = prop('S', 'H', h[21], 'P', p[2], fluido)

    h[41] = h[3] - (0.75*(h[3]-h[4]))
    t[41] = prop('T', 'H', h[41], 'P', p[4], fluido)
    s[41] = prop('S', 'H', h[41], 'P', p[4], fluido)
    q[41] = prop('Q', 'H', h[41], 'P', p[4], fluido)
    q[4] = prop('Q', 'H', h[4], 'P', p[4], fluido)

    print(f'''h2` = {h[21]}
t2` = {t[21]-273.15}
s2` = {s[21]}''')
    print(f'''h4` = {h[41]}
t4` = {t[41]-273.15}
q4` = {q[41], q[4]}
s4` = {s[41]}''')

    lista = [['Punto', 'T [°C]', 'P [Pa]',  's [J/kgK]', 'h [J/kg]']]
    lista.append([1, t[1]-273.15, p[1], s[1], h[1]])
    lista.append([2, t[2]-273.15, p[2], s[2], h[2]])
    lista.append([3, t[3]-273.15, p[3], s[3], h[3]])
    lista.append([4, t[4]-273.15, p[4], s[4], h[4]])
    print('\n')
    print(fluido.upper())
    print(tabulate(lista, headers='firstrow', tablefmt='latex'))

    lista = [['Punto', 'T [°C]', 'P [Pa]',  's [J/kgK]', 'h [J/kg]']]
    lista.append([1, t[1]-273.15, p[1], s[1], h[1]])
    lista.append([21, t[21]-273.15, p[2], s[21], h[21]])
    lista.append([3, t[3]-273.15, p[3], s[3], h[3]])
    lista.append([41, t[41]-273.15, p[4], s[41], h[41]])

    print('\n')
    print(fluido.upper())
    print(tabulate(lista, headers='firstrow', tablefmt='latex'))

    trabajo_neto = (h[3] - h[41]) - (h[21] - h[1])
    eficiencia = 0.75*(trabajo_neto / (h[3] - h[21]))

    print((h[3] - h[21]))
    print((h[3] - h[21])/(0.75*45000*1000))

    print(f'Eficiencia ciclo con elementos al 75%: {eficiencia*100}%, Trabajo neto con elementos al 75%: {trabajo_neto/1000} kJ/kg')
    print('\n')
