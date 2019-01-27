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
            Vector
"""
# Screen object is a viewport into our universe and will always
# accomodate the size of the universe.
class Screen:
    pass

# Universe object contains real distances, particles, an dictates
# the rate of time within our system.
class Universe:
    def __init__(self):
        self.size = None
    
    
    def gravity(self):
        """
        Updates the acceleration vectors of every particle.
        """
        pass

    def physics(self):
        """
        Updates velocity and position of particles  
        """


# Particle objects describe themselves int the 
class Particle:
    def __init__(self):
        self.mass = None 
        self.pos = None
        
        self.vel = None
        self.acc = None
        

        
        
# vector object are an experiment with the intent of making the
# code more organized.
class Vector:
    def __init__(self, x, y, z):
        self.x = None
        self.y = None
        self.z = None
        
def make_particle():
    particle = Particle()
    particle.mass = 10