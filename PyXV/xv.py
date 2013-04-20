#!/usr/bin/python
'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2013 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2013 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2013 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: xv.py - Last Update: 04/01/2013 Ver. 1.0.0  - Author: cooldude2k $
'''
import os, sys, pygame;

pygame.display.init();
pyicon=pygame.image.load("/mnt/utmp/upctest/old_icon.png");
pygame.display.set_icon(pyicon);
if(len(sys.argv)==2):
 ppmimg=pygame.image.load(sys.argv[1]);
if(len(sys.argv)==4):
 ppmimg=pygame.image.load(sys.argv[3]);
width, height = ppmimg.get_size();
screen = pygame.display.set_mode((width, height));
if(len(sys.argv)==2):
 pygame.display.set_caption("PyXV - "+str(os.path.basename(sys.argv[1])));
if(len(sys.argv)==4):
 pygame.display.set_caption("PyXV - "+str(sys.argv[2]));
pygame.display.get_active();
pygame.mouse.set_visible(0);

screen.blit(ppmimg, (0, 0));
pygame.display.flip();
done = False;
while not done:
 for event in pygame.event.get():
  if (event.type == pygame.QUIT):
   done = True;
  if (event.type == pygame.KEYDOWN):
   if (event.key == pygame.K_t) or (event.key == pygame.K_w):
    pygame.display.toggle_fullscreen();
   if (event.key == pygame.K_i) or (event.key == pygame.K_m):
    pygame.display.iconify();
   if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
    done = True;
pygame.display.quit();
pygame.quit();
os._exit(0);
