#!/usr/bin/env python
"""
Created on Sun Aug 25 03:03:02 2019

@author: js_en
"""
import numpy as np
import cv2 as cv
import time



    
    
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
        
if __name__=="__main__":
    blankimg = np.zeros((500,500,3), np.uint8)
    
    point1 = Point([255,255],[1,0],[1,0])
    point2 = Point([255,500],[-1,0],[0,0])
    
    for i in range(500):
        img = np.zeros((500,500,3), np.uint8)

        point1.update(1)
        img[point1.get_pos()[0]%500,point1.get_pos()[1]%500] = [255,255,255]
        #img[255,255] = [255,255,255]
        
        cv.imshow("Screen", img)
        if cv.waitKey(int(1000/25)) == ord('q'): # Press q to stop sim
            break
    cv.destroyAllWindows()