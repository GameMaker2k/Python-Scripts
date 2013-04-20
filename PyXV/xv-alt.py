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

    $FileInfo: xv-alt.py - Last Update: 04/01/2013 Ver. 1.0.0  - Author: cooldude2k $
'''
import os, sys, pygame, argparse;

parser = argparse.ArgumentParser();
parser.add_argument("-name", help="title name");
parser.add_argument("file", help="file name");
getargs = parser.parse_args();

if(getargs.file!=None):
 pygame.display.quit();
 pygame.quit();
 sys.exit(0);
if(not os.path.exists(getargs.file) or not os.path.isfile(getargs.file)):
 pygame.display.quit();
 pygame.quit();
 sys.exit(0);

pygame.display.init();
pyicon=pygame.image.load("/mnt/utmp/upctest/old_icon.png");
pygame.display.set_icon(pyicon);
ppmimg=pygame.image.load(getargs.file);
width, height = ppmimg.get_size();
screen = pygame.display.set_mode((width, height));
if(getargs.name!=None):
 pygame.display.set_caption("PyXV - "+str(getargs.name));
if(getargs.name==None):
 pygame.display.set_caption("PyXV - "+str(os.path.basename(getargs.file)));
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
