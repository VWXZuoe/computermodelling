import numpy as np
from Particle3D import particle


def main():

    f = open("particle1.txt", "r")

    p1 = particle.new_particle(f)
    p2 = particle.new_particle(f)

    f.close()

    print (p1, p2)

    sys_ke = particle.sys_kinetic([p1, p2])
    totmass, massv = particle.com_velocity([p1, p2])

    print (sys_ke)
    print (massv)

    dt = 1
    force = np.array([1, 0, -1])
    print (p1.kinetic_e())
    print (p2.momentum())

    p1.update_pos_1st(dt)
    print (p1)
    p1.update_pos_2nd(dt, force)
    print (p1)

    p2.update_vel(dt,force)
    print (p2.vel)
    p2.update_vel(dt,force)
    print (p2.vel)

main()
