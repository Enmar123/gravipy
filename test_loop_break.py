#!/usr/bin/env python3
"""
Test to see if loops can be broken
"""

import time

class World:
    def __init__(self):
        self.timestep = 1
        self.is_running = False
        self.timelimit = 10
        self.time = 0
    
    def start(self):
        self.is_running = True
        self.update()
        
    def stop(self):
        self.is_running = False
    
    def update(self):
        print("update has run")
        self.time += self.timestep
        time.sleep(self.timestep)
        if self.time >= self.timelimit:
            self.stop()
        if self.is_running is True:
            self.update()
    
            
        
                

        
world = World()
world.start()
time.sleep(5)
print('stop')