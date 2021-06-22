from CoolProp.CoolProp import PropsSI as prop
from CoolProp.CoolProp import PhaseSI as fase
from matplotlib import pyplot as plot
from tabulate import tabulate


t1 = 300
t3 = 300
p1 = 0.1 * (10**6)
p4 = 1.2 * (10**6)
s1 = prop('S', 'T', t1, 'P', p1, 'air')
s2 = s1
for i in range(100):
    p2 = (i/100000000000 + .346574194) * (10**6)
    p3 = p2
    t2 = prop('T', 'P', p2, 'S', s2, 'air')
    s3 = prop('S', 'T', t3, 'P', p3, 'air')
    s4 = s3
    t4 = prop('T', 'P', p4, 'S', s4, 'air')
    h4 = prop('H', 'P', p4, 'T', t4, 'air')
    h3 = prop('H', 'P', p3, 'T', t3, 'air')
    h2 = prop('H', 'P', p2, 'T', t2, 'air')
    h1 = prop('H', 'P', p1, 'T', t1, 'air')
    h43 = h4-h3
    h21 = h2-h1
    print(p2, h43-h21)
