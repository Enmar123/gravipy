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
        self.fps = 35                   # fps of the universe
        self.rez = 500
        self.d = 3
        self.display = self.make_screen
    
    def make_screen(self):
        np.full((self.rez,self.rez, self.d),255, dtype='uint8')
        
        
    def display(self):
        cv.imshow("Universe", self.display)

# Universe object contains real distances, particles, an dictates
# the rate of time within our system.
class Universe:
    def __init__(self):
        self.size = (500000, 500000)    # m
        self.G = 6.674 * 10**(-11)      # N*(m/kg)**2
        self.simfrequency = 10          # update rate
        self.rate = 1                   # speed of time
        self.simtime = 0
        self.is_running = False
        
        self.particles = []             # list of particles
    
        self.update_values()    
    
    def update_values(self):
        self.realtimestep = 1 / (self.simfrequency * self.rate)
        self.simtimestep = 1 / self.simfrequency
    
    def start(self):
        self.is_running = True
        self.update_universe()
            
    def stop(self):
        self.is_running = False
    
    def update_universe(self):
        # forces should be calculated at the start of the timestep
        self.interact()
        # physics should be calculated at the end of the timestep
        self.physics()
        # Pausing sim for time
        time.sleep(self.realtimestep)
        # Updating Time passed in universe
        self.simtime += self.simtimestep
        
        if self.run is True:
            self.update_universe()
            
        
        
        
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
        vector = self.get_vector(p1, p2)
        p1.apply_force(F, vector)
        
    
    def get_dist(self, particle1, particle2):
        p1, p2 = particle1, particle2
        dist = np.sqrt(np.sum(np.square(p1.pos - p2.pos)))
        return dist
    
    def get_vector(self, particle1, particle2):
        vector = particle2 - particle1
        dist = self.get_dist(particle1, particle2)
        scale = 1/dist
        vector = vector * scale
        return vector

    def physics(self):
        """
        Updates velocity and position of particles  
        """
        for p in self.particles:
            t = self.simtimestep
            # Accuracy can be improved by using the average values
            # between accel and vel to calc pos. i think.
            p.pos = p.pos + p.vel * t + (1/2) * p.acc * t**2    # eqn of motion
            p.vel = p.acc * t + p.vel                           # eqn of motion
        
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
        
    def apply_force(self, F, vector):
        add_acc = F * vector / self.mass
        self.acc =  self.acc + add_acc
        
        
# vector object are an experiment with the intent of making the
# code more organized.
class Vector:
    def __init__(self, x, y, z):
        self.x = None
        self.y = None
        self.z = None
        
    def vector_sum(self):
        pass
        
if __name__=="__main__":
    
    universe = Universe()
    screen = Screen
    screen.universe = universe
    