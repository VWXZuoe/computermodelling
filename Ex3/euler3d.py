"""
Jude Ferrier - s1808200
CompMod Ex3.

Symplectic Euler method for time integration

"""

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

def main():
    # Read name of output file from command line
    if len(sys.argv)!=2:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " <output file>")
        quit()
    else:
        outfile_name = sys.argv[1]

    # Open output file
    outfile = open(outfile_name, "w")

    # Set up simulation parameters
    atom = str(input("Input 1 for diatomic N, 2 for diatomic O: "))
    dt = 0.01
    numstep = 2000
    time = 0.0

    if atom == str(1):
    #constants for nitrogen
        ire = float(1.09768)
        iDe = float(9.90523)
        ia = float(2.68867)
        im = float(14.01)

    elif atom == str(2):
    #constants for oxygen
        ire = float(1.20752)
        iDe = float(5.21322)
        ia = float(2.65374)
        im = float(16)

    else:
    #only allow for chosen inputs
        print("Invalid option selected.")
        sys.exit()

    initialpos1 = np.array([(ire/2)+0.1, 0, 0])
    initialpos2 = np.array([(-ire/2)-0.1, 0, 0])
    initialv1 = np.array([0.05, 0, 0])
    initialv2 = np.array([-0.05, 0, 0])

    p1 = particle(im, initialpos1, initialv1, str("1st"))
    p2 = particle(im, initialpos2, initialv2, str("2nd"))

    energy = p1.kinetic_e() + potential_energy_morse(p1, p2, ire, iDe, ia)

    # Initialise data lists for plotting later
    t_axis = [time]
    pos_axis = [np.linalg.norm(p1.pos)]
    e_axis = [energy]

    for i in range(numstep):
        # Update particle position
        p1.update_pos_1st(dt)
        p2.update_pos_1st(dt)

        # Calculate force
        force = force_morse(p1, p2, ire, iDe, ia)

        # Update particle velocity
        p1.update_vel(dt, force)
        p2.update_vel(dt, -1*force)

        # Increase time
        time += dt

        # Output particle information
        energy = p1.kinetic_e() + potential_energy_morse(p1, p2, ire, iDe, ia)
        outfile.write("{0:f}, {1:f}, {2:12.8f}\n".format(time,np.linalg.norm(p1.pos),energy))

        # Append information to data lists
        t_axis.append(time)
        pos_axis.append(np.linalg.norm(p1.pos))
        e_axis.append(energy)


    # Post-simulation:
    # Close output file
    outfile.close()

    # Plot particle trajectory to screen
    pyplot.title("Symplectic Euler: position vs time")
    pyplot.xlabel("Time")
    pyplot.ylabel("Position")
    pyplot.plot(t_axis, pos_axis)
    pyplot.show()

    # Plot particle energy to screen
    pyplot.title("Symplectic Euler: total energy vs time")
    pyplot.xlabel("Time")
    pyplot.ylabel("Energy")
    pyplot.plot(t_axis, e_axis)
    pyplot.show()

main()
