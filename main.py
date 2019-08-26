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
            self.img[pt[0]%self.size,pt[1]%self.size] = [255,255,255]
            
    def clear(self):
        self.img = np.zeros((self.size,self.size,3), np.uint8)
        
        
if __name__=="__main__":
    screen = Screen(500)
    point1 = Point([255,255],[1,0],[0.5,0])
    point2 = Point([255,300],[1,1],[0.1,0])
    #point2 = Point([255,500],[-1,0],[0,0])
    
    for i in range(500):
        screen.clear()

        point1.update(1)
        point2.update(1)
        points = [point1, point2]
        pts = screen.project(points)
        screen.draw_pts(pts)
        
        cv.imshow("Screen", screen.img)
        if cv.waitKey(int(1000/25)) == ord('q'): # Press q to stop sim
            break
    cv.destroyAllWindows()