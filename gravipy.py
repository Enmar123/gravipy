#!/usr/bin/env python3

"""
Desctiption:

    Simple Gravity sim

Code diagram:

    User
      |
    Screen
      |
    Universe
        Particle
            Vector <- not really needed
"""
import numpy as np
import cv2 as cv
import time

# Screen object is a viewport into our universe and will always
# accomodate the size of the universe.
class Screen:
    def __init__(self):
        self.universe = None
        self.fps = 35           # fps of the universe
    pass

# Universe object contains real distances, particles, an dictates
# the rate of time within our system.
class Universe:
    def __init__(self):
        self.size = (500000, 500000)    # m
        self.G = 6.674 * 10**(-11)      # N*(m/kg)**2
        self.timestep = 0.1             # update rate
        self.rate = 1                  # speed of time
        self.simtime = 0
        
        self.particles = []             # list of particles
    
    def update(self):
        # <TODO>
        # Create updating function for the universe
        timepassed = self.timestep * self.rate
        
        
        # forces should be calculated at the start of the timestep
        self.interact()
        # physics should be calculated at the end of the timestep
        self.physics()
        
        
        time.sleep(timepassed)
        self.simtime += timepassed
        
        
        
    # Pits particle1 against every other particle in the universe
    # so that interactions can be calculated.
    def interact(self):
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1 is particle2 :
                    pass #skip interaction
                else:
                    # specify interactions
                    self.gravity(particle1, particle2)
    
    
    def gravity(self, particle1, particle2):
        """
        Updates the acceleration vectors of every particle.
        """
        p1, p2 = particle1, particle2
        m1, m2 = p1.mass, p2.mass
        r = self.get_dist(p1, p2)
        F = self.G * (m1 * m2) / r**2   # Newtons law of gravity
        p1.apply_force(F, direction)
        
    
    def get_dist(self, particle1, particle2):
        p1, p2 = particle1, particle2
        dist = np.sqrt(np.sum(np.square(p1.pos - p2.pos)))
        return dist

    def physics(self):
        """
        Updates velocity and position of particles  
        """
    def spawn_particle(self, mass=0, pos=[0,0,0], 
                                     vel=[0,0,0],
                                     acc=[0,0,0]):
        particle = Particle()
        particle.mass = mass
        particle.pos = np.array(pos)
        particle.vel = np.array(vel)
        particle.acc = np.array(acc)
        return particle


# Particle objects describe themselves int the 
class Particle:
    def __init__(self):
        self.mass = None 
        self.pos = None
        
        self.vel = None
        self.acc = None
        
    def apply_force(self, F):
        
        

        
        
# vector object are an experiment with the intent of making the
# code more organized.
class Vector:
    def __init__(self, x, y, z):
        self.x = None
        self.y = None
        self.z = None
        
    def vector_sum(self):
        pass
        
