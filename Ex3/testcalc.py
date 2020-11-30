import sys
import math
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import particle


def force_morse(particle1, particle2, re, De, a):

    # Force on particle 1 from 2
    r12 = particle2.pos - particle1.pos
    force = 2*a*De*(1-np.exp(-a*(np.linalg.norm(r12)-re))*np.exp(-a*(np.linalg.norm(r12)-re)))*(r12/(np.linalg.norm(r12)))

    return force

def potential_energy_morse(particle1, particle2, re, De, a):

    r12 = particle2.pos - particle1.pos
    potential = De*(((1-np.exp(-a*(np.linalg.norm(r12)-re)))**2)-1)
    return potential

dt = 0.01
numstep = 2000
time = 0.0

ire = float(1.20752)
iDe = float(5.21322)
ia = float(2.65374)
im = float(16)

initialpos1 = np.array([(ire/2)+0.1E-10, 0, 0])
initialpos2 = np.array([(-ire/2)-0.1E-10, 0, 0])
initialv1 = np.array([0.05E-10, 0, 0])
initialv2 = np.array([-0.05E-10, 0, 0])

p1 = particle(im, initialpos1, initialv1, str("1st"))
p2 = particle(im, initialpos2, initialv2, str("2nd"))

energy = p1.kinetic_e() + p2.kinetic_e() + potential_energy_morse(p1, p2, ire, iDe, ia)
print ("energy = " , energy)

p1.update_pos_1st(dt)
p2.update_pos_1st(dt)

print (p1.pos, p2.pos)
# Calculate force
force = force_morse(p1, p2, ire, iDe, ia)
print ("force = " , force)

print ("v ", p1.vel, p2.vel)
# Update particle velocity
p1.update_vel(dt, force)
p2.update_vel(dt, -1*force)

print ("new v " , p1.vel, p2.vel)
# Increase time
time += dt

# Output particle information
energy = p1.kinetic_e() + potential_energy_morse(p1, p2, ire, iDe, ia)
