#!/usr/bin/env python
"""
Created on Sun Aug 25 03:03:02 2019

@author: js_en
"""
import numpy as np
import cv2 as cv
import math as ma
import time
import copy



       
    
class Point:
    def __init__(self, pos, vel, acc):
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.acc = np.array(acc)
        
    def update(self, sec):
        self.pos = self.pos + self.vel*sec
        self.vel = self.vel + self.acc*sec
        
    def get_pos(self):
        return list(self.pos)
    
class Particle(Point):
    def __init__(self, pos, vel, acc, mass):
        Point.__init__(self, pos, vel, acc)
        self.mass = mass
        self.force = [0,0]
        self.forces = [[0,0]]
        
    def update(self):
        if len(self.forces) <= 1:
            self.force = self.forces[0]
        else:
            self.force = np.add.reduce(self.forces)
        self.forces = [np.array([0,0])]
        self.acc = np.array(self.force)/self.mass
        Point.update(self, 1)
        
        
    def apply_force(self, force):
        self.forces.append(force)
        
    def get_mass(self):
        return self.mass

        
class Universe():
    def __init__(self):
        self.G = 1
        
        self.particles = []
        
        self.bounded = True
       
    def update(self):
        """ Updates the forces and properties of particles in the universe """
        self.gravity()
        self.update_motion()
   
    def gravity(self):
        for particle1 in self.particles:
            for particle2 in self.particles:
                if particle1 == particle2:
                    pass
                else:
                    m1 = particle1.get_mass()
                    m2 = particle2.get_mass()
                    r = self.get_dist(particle1, particle2)
                    F = self.G*m1*m2/r**2
                    x, y = np.array(particle2.get_pos()) - np.array(particle1.get_pos())
                    Fx = F * np.cos(np.arccos(x/r))
                    Fy = F * np.sin(np.arcsin(y/r))
                    particle1.apply_force(np.array([Fx,Fy]))
                    
   
    def update_motion(self):
        [particle.update() for particle in self.particles]
        if self.bounded:
            for particle in self.particles:
                x, y = particle.get_pos()
                if x<0 or x>500:
                    particle.vel[0] = particle.vel[0]*-1
                if y<0 or y>500:
                    particle.vel[1] = particle.vel[1]*-1
                
    def get_dist(self, p1, p2):
       xydist = np.array(p1.get_pos()) - np.array(p2.get_pos())
       rdist = np.hypot(xydist[0], xydist[1])
       return rdist
   
    def add_prt(self, particles):
        if type(particles) is list:
            [self.particles.append(particle) for particle in particles]
        else:
            self.particles.append(particles)
    
    
class Screen:
    def __init__(self, size):
        self.size = size
        self.img = np.zeros((size,size,3), np.uint8)
    
    def project(self, points):
        pts = []
        for point in points:
            pts.append(list(np.round(point.get_pos()).astype(np.int)))
        return pts
    
    def draw_pts(self, pts):
        for pt in pts:
            self.img[pt[0]%self.size,pt[1]%self.size] = [255,255,255] # draw points
            cv.circle("Screen",(pt[0]%self.size, pt[1]%self.size), [255,255,255] )
    
    def draw_circles(self, ps):
        for p in ps:
            r = int(round((p.get_mass()**(1/2))))
            x, y = p.get_pos()
            x = int(round(x))
            y = int(round(y))
            cv.circle(screen.img,(x%self.size, y%self.size), r, [255,255,255] )
    
    def clear(self):
        self.img = np.zeros((self.size,self.size,3), np.uint8)
        
        
if __name__=="__main__":
    screen = Screen(500)
    uni = Universe()
    # Testing particles
    particle1 = Particle([255,255],[0,0.3],[0,0],20)   # @500 "fps"
    particle2 = Particle([200,255],[0,-.3],[0,0],20)   # @500
    #particle1 = Particle([255,255],[0,-.15],[0,0],100) # @500
    #particle2 = Particle([200,255],[0,1.5],[0,0],10)   # @500
    #particle1 = Particle([255,255],[-1,0],[0,0],100)    # @500
    #particle2 = Particle([200,255],[0,3],[0,0],10)      # @500
    uni.add_prt([particle1, particle2])
    
    
    for i in range(10000): # Duaration of playback 
        screen.clear()

        uni.update()
        #pts = screen.project(uni.particles)
        screen.draw_circles(uni.particles)
        
        cv.imshow("Screen", screen.img)
        if cv.waitKey(int(1000/500)) == ord('q'): # Press q to stop sim
            break
    cv.destroyAllWindows()