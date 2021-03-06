#!/usr/bin/env python
from random import randint
from pygame import *
from pygame import gfxdraw
import sys
sys.path.append("..")
import FunnyPathGetter.PathGetter as PathGetter
font.init()
font = font.Font(None,40)

scr = display.set_mode((800,800))
scr.blit(font.render("hold the left mouse button to draw",1,(255,255,255)),(50,50))
scr.blit(font.render("d = undo",1,(255,255,255)),(50,90))
scr.blit(font.render("s = save",1,(255,255,255)),(50,130))
scr.blit(font.render("hit any key",1,(255,255,255)),(50,190))
display.flip()
while event.wait().type != KEYDOWN: pass
scr.fill(0)
display.flip()

a = []
c = []
color = [randint(0,255) for i in [1,2,3]]+[50]

while 1:
    ev = event.wait()
    if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
        a.append([ev.pos])
        c.append(color)
    if ev.type == MOUSEMOTION and ev.buttons[0]:
        a[-1].append(ev.pos)
        if len(a[-1]) >= 2:
            draw.aaline(scr,color,a[-1][-1],a[-1][-2],1)
            display.flip() 
    if ev.type == MOUSEBUTTONUP and ev.button == 1:
        if len(a[-1]) >= 2:
            draw.aaline(scr,color,a[-1][0],a[-1][-1],1)
            gfxdraw.filled_polygon(scr,a[-1],color)
            display.flip() 
        color = [randint(0,255) for i in [1,2,3]]+[50]
    if ev.type == QUIT: break
    if ev.type == KEYDOWN and ev.key == K_s:
        p = PathGetter.get()
        if p: image.save(scr,p)
    if ev.type == KEYDOWN and ev.key == K_d and a:
        a.pop()
        c.pop()
        scr.fill(0)
        for lines,color in zip(a,c):
            draw.aalines(scr,color,1,lines,1)
            gfxdraw.filled_polygon(scr,lines,color)
        display.flip()
         
    
