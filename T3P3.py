from CoolProp.CoolProp import PropsSI as prop
from CoolProp.CoolProp import PhaseSI as fase
from matplotlib import pyplot as plot
from tabulate import tabulate


fluidos = ['air']
eficiencia = {}
trabajo_neto = {}
for fluido in fluidos:
    p = {}
    t = {}
    h = {}
    s = {}
    p[1] = 100 * (10**3)
    p[2] = 300 * (10**3)
    p[3] = 300 * (10**3)
    p[4] = 1000 * (10**3)
    p[5] = 1000 * (10**3)
    p[6] = 1000 * (10**3)
    p[7] = 300 * (10**3)
    p[8] = 300 * (10**3)
    p[9] = 100 * (10**3)
    p[10] = 100 * (10**3)

    t[1] = 300
    t[3] = 300
    t[6] = 1400
    t[8] = 1400

    s[1] = prop('S', 'P', p[1], 'T', t[1], fluido)
    s[21] = s[1]
    s[3] = prop('S', 'T', t[3], 'P', p[3], fluido)
    s[41] = s[3]
    s[6] = prop('S', 'P', p[6], 'T', t[6], fluido)
    s[71] = s[6]
    s[8] = prop('S', 'T', t[8], 'P', p[8], fluido)
    s[91] = s[8]

    h[21] = prop('H', 'P', p[2], 'S', s[21], fluido)
    h[41] = prop('H', 'P', p[4], 'S', s[41], fluido)
    h[71] = prop('H', 'P', p[7], 'S', s[71], fluido)
    h[91] = prop('H', 'P', p[9], 'S', s[91], fluido)
    t[21] = prop('T', 'P', p[2], 'S', s[21], fluido)
    t[41] = prop('T', 'P', p[4], 'S', s[41], fluido)
    t[71] = prop('T', 'P', p[7], 'S', s[71], fluido)
    t[91] = prop('T', 'P', p[9], 'S', s[91], fluido)

    h[1] = prop('H', 'P', p[1], 'T', t[1], fluido)
    h[3] = prop('H', 'T', t[3], 'P', p[3], fluido)
    h[6] = prop('H', 'P', p[6], 'T', t[6], fluido)
    h[8] = prop('H', 'T', t[8], 'P', p[8], fluido)
    h[9] = h[8] - (h[8] - h[91]) * 0.8
    h[7] = h[6] - (h[6] - h[71]) * 0.8
    h[2] = (h[21] - h[1]) / 0.8 + h[1]
    h[4] = (h[41] - h[3]) / 0.8 + h[3]
    h[5] = (h[9] - h[4]) * 0.8 + h[4]
    h[10] = h[9] - (h[5] - h[4])

    t[2] = prop('T', 'P', p[2], 'H', h[2], fluido)
    t[4] = prop('T', 'P', p[4], 'H', h[4], fluido)
    t[5] = prop('T', 'P', p[5], 'H', h[5], fluido)
    t[7] = prop('T', 'P', p[7], 'H', h[7], fluido)
    t[9] = prop('T', 'P', p[9], 'H', h[9], fluido)
    t[10] = prop('T', 'P', p[10], 'H', h[10], fluido)

    for i in range(1, 11):
        if i not in s.keys():
            s[i] = prop('S', 'P', p[i], 'T', t[i], fluido)
        if i not in h.keys():
            h[i] = prop('H', 'P', p[i], 'T', t[i], fluido)
    lista = [['Punto', 'T [°C]', 'P [Pa]',  's [J/kgK]', 'h [J/kg]']]
    for i in range(1, 11):
        lista.append([i, t[i]-273.15, p[i], s[i], h[i]])
    print('\n')
    print(fluido.upper())
    print(tabulate(lista, headers='firstrow', tablefmt='latex'))
    q_in = (h[6] - h[5] + h[8] - h[7])
    q_out = (h[10] - h[1] + h[2] - h[3])
    eficiencia = 1 - q_out/q_in
    w_turbina = ((h[6] - h[7]) + (h[8] - h[9]))
    w_compresor = ((h[2] - h[1]) + (h[4] - h[3]))
    m = 5.807
    print(f'Q_in: {q_in * m/1000} kW')
    print(f'Q_out: {q_out * m/1000} kW')
    print(f'Eficiencia: {eficiencia* 100} %')
    print(f'Relacion compresor turbina: {w_compresor/w_turbina}')
    print(f'Potencia neta: {(w_turbina - w_compresor)* m/1000} kW')
    print('\n')

rango = list(range(374))
lista_eses = [s[i + 1] for i in range(10)]
lista_eses.append(s[21])
lista_eses.append(s[41])
lista_eses.append(s[71])
lista_eses.append(s[91])
lista_tes = [t[i + 1] - 273.15 for i in range(10)]
lista_tes.append(t[21] - 273.15)
lista_tes.append(t[41] - 273.15)
lista_tes.append(t[71] - 273.15)
lista_tes.append(t[91] - 273.15)

plot.figure()
plot.scatter(lista_eses, lista_tes)

for i, txt in enumerate(lista_eses):
    if i == 10:
        plot.annotate(f'{i - 8}`', (lista_eses[i], lista_tes[i]))
    elif i == 11:
        plot.annotate(f'{i - 7}`', (lista_eses[i], lista_tes[i]))
    elif i == 12:
        plot.annotate(f'{i - 5}`', (lista_eses[i], lista_tes[i]))
    elif i == 13:
        plot.annotate(f'{i - 4}`', (lista_eses[i], lista_tes[i]))
    else:
        plot.annotate(f'{i+1}', (lista_eses[i], lista_tes[i]))
plot.ylabel('Temperatura °C')
plot.xlabel('S')
plot.tight_layout()
plot.show()
