"""
Ex2.
Jude Ferrier - s1808200

Class describing a particle in 3D space
Velocity and position are described by numpy arrays

Includes time integrator methods and functions to output properties of the particles
as well as static methods to output system properties.

"""

import numpy as np


class particle(object):
    """
    Class to describe point-particles in 3D space

        Properties:
    name: name of the particle
    mass: mass of the particle
    pos: position of the particle
    vel: velocity of the particle

        Methods:
    __init__
    __str__
    kinetic_e  - computes the kinetic energy
    momentum - computes the linear momentum
    update_pos_1st - updates the position to 1st order
    update_pos_2nd - updates the position to 2nd order
    update_vel - updates the velocity

        Static Methods:
    new_particle - initializes a particle from a file handle
    sys_kinetic - computes total kinetic energy of a particle list
    com_velocity - computes total mass and CoM velocity of a particle list
    """


    def __init__(self, mass, position, velocity, name):
        """
        Initialises a particle in 3D space

        :param name: String w/ the name of the particle
        :param mass: float, mass of the particle
        :param position: [3] float array w/ position
        :param velocity: [3] float array w/ velocity
        """
        self.name = str(name)
        self.m = float(mass)
        self.pos = np.array(position, float)
        self.vel = np.array(velocity, float)

    def __str__(self):
        """
        XYZ-compliant string. The format is
        <label>    <x>  <y>  <z>
        """

        xyz_string = "{} {:.0001f} {:.0001f} {:.0001f}".format(self.name, self.pos[0], self.pos[1], self.pos[2])
        return xyz_string

    def kinetic_e(self):
        """
        Returns the kinetic energy of a particle instance

        :return ke: float, 1/2 m v**2
        """

        ke = (self.m*(np.linalg.norm(self.vel)**2))/2
        return ke

    def momentum(self):
        """
        Returns the linear momentum of a particle instance

        :return p: [3] float np.array, m*v
        """

        p = self.m*self.vel
        return np.array(p)

    def update_pos_1st(self, dt):
        """
        1st order position update

        :param dt: timestep
        """
        self.pos += self.vel*dt


    def update_pos_2nd(self, dt, force):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """
        self.pos += self.vel*dt + (force/(2*self.m))*(dt**2)


    def update_vel(self, dt, force):
        """
        Velocity update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """
        self.vel += (force/self.m)*dt


    @staticmethod
    def new_particle(filehandle):
        """
        Initialises a particle instance given an input file handle.

        The input file should contain one per particle in the following format:
        label   <mass>  <x> <y> <z>    <vx> <vy> <vz>

        :param inputFile: Readable file handle in the above format

        :return particle instance
        """

        ats = filehandle.readline().split()
        name = ats[0]
        mass = float(ats[1])
        x_pos = float(ats[2])
        y_pos = float(ats[3])
        z_pos = float(ats[4])
        vx = float(ats[5])
        vy = float(ats[6])
        vz = float(ats[7])

        return particle(mass, np.array([x_pos, y_pos, z_pos]), np.array([vx, vy, vz]), name)

    @staticmethod
    def sys_kinetic(particle_list):
        """
        Returns the kinetic energy of the whole system

        :param particle_list: list in which each item is a particle instance

        :return sys_ke: sum 1/2 m_i v_i^2
        """

        sys_ke = 0

        for n in range(len(particle_list)):
            sys_ke += particle_list[n].kinetic_e()
        return sys_ke

    @staticmethod
    def com_velocity(particle_list):
        """
        Computes the total mass and CoM velocity of a list of particles

        :param particle_list: list in which each item is a particle instance

        :return total_mass: The total mass of the system
        :return com_vel: Centre-of-mass velocity
        """


        total_mass = 0
        com_vel = 0

        for p in range(len(particle_list)):
            total_mass += particle_list[p].m
        for q in range(len(particle_list)):
            com_vel += (particle_list[q].m*particle_list[q].vel)/total_mass

        return total_mass, np.array(com_vel)
