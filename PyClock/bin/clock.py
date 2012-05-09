#!/usr/bin/python2

"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2012 iDB Support - http://idb.berlios.de/
    Copyright 2012 Game Maker 2k - http://gamemaker2k.org/

    $FileInfo: clock.py - Last Update: 05/09/2012 Ver 1.0.0-1 - Author: cooldude2k $
"""

import os, sys, time, locale, calendar, pygame, glob;
from os import environ, system, mkdir;
from sys import version, exit;
from time import gmtime, strftime;
from glob import glob;
from pygame import init, quit;
from pygame.locals import *;
import shutil;

pythonver=version;
print('python version "'+pythonver+'"');
init();
print('init pygame');
fpsclock=pygame.time.Clock();
pygamever=pygame.version.ver;
print('pygame version '+pygamever);
print('sdl version %s.%s.%s' % pygame.get_sdl_version());

if(os.path.exists('./config.txt') == True):
   if(os.path.isdir('./config.txtt') == True):
      os.removedirs('./config.txt');
      print('deleting file "./config.txt"');
if(os.path.exists('./config.txt') == False):
   shutil.copyfile('./default/config.txt', './config.txt');
   print('copying config file "./default/config.txt" to "./config.txt"');
if(os.path.exists('./screenshots') == False):
   mkdir('./screenshots');
   print('making screenshot dir "./screenshots"');

pyconfig=open('./config.txt', 'r');
print('loading config file "./config.txt"');
configload=pyconfig.readlines();
bgcpresplit=configload[2].rstrip('\n');
bgcsplit=bgcpresplit.split(',');
displaysize=configload[6].rstrip('\n');
displaysizesplit=displaysize.split('x');
pysoundfiles=configload[7].rstrip('\n');
pysoundconf=configload[8].rstrip('\n');
pysndconfsplit=pysoundconf.split(',');

fontload=configload[0].rstrip('\n');
fontloadsplit=fontload.split('|');
fontsizeload=configload[1].rstrip('\n');
fontsizesplit=fontsizeload.split('|');
pycolorload=configload[3].rstrip('\n');
pycolorsplit=pycolorload.split('|');
fontxyload=configload[4].rstrip('\n');
fontxysplit=fontxyload.split('|');
datetimeload=configload[5].rstrip('\n');
datetimesplit=datetimeload.split('|');
imgbgload=configload[9].rstrip('\n');
imgbgsplit=imgbgload.split('|');
imgbgxyload=configload[10].rstrip('\n');
imgbgxysplit=imgbgxyload.split('|');

environ['SDL_VIDEODRIVER'] = 'x11';
pygame.display.init();
print('init pygame x11 display');

globfiles=glob(pysoundfiles);
numfiles=len(globfiles);
countnum=0;
if(numfiles > 0):
   maxarraynum = numfiles - 1;
   print('number of sound files %i' % numfiles);
   pygame.mixer.init(int(pysndconfsplit[0]),int(pysndconfsplit[1]),int(pysndconfsplit[2]),int(pysndconfsplit[3]));
   print('init pygame sound');

pyscreen=pygame.display.set_mode((int(displaysizesplit[0]),int(displaysizesplit[1])),FULLSCREEN);
print('setting display mode "'+displaysizesplit[0]+'x'+displaysizesplit[1]+'"');
print('setting fullscreen mode');
pybackground=pygame.Surface(pyscreen.get_size());
pybackground.fill((int(bgcsplit[0]),int(bgcsplit[1]),int(bgcsplit[2])));
pygame.display.set_caption('PyClock Test App');
print('setting caption "PyClock Test App"');
pygame.mouse.set_visible(0);
pygame.display.get_active();
# pygame.display.toggle_fullscreen();
pygame.font.init();
print('init pygame font');

fcountall = 0;
done = False;
while not done:
   pyscreen.fill((int(bgcsplit[0]),int(bgcsplit[1]),int(bgcsplit[2])));
   fcount0 = 0;
   while (fcount0 < len(imgbgsplit)):
      if (os.path.exists(imgbgsplit[int(fcount0)]) == True):
         pybgimgall={};
         pybgimgall[int(fcount0)]=pygame.image.load(imgbgsplit[int(fcount0)]);
         pybgimgxyall=imgbgxysplit[int(fcount0)].split(',');
         pyscreen.blit(pybgimgall[int(fcount0)],(int(pybgimgxyall[0]),int(pybgimgxyall[1])));
      fcount0 = fcount0 + 1;
   fcount1 = 0;
   while (fcount1 < len(fontloadsplit)):
      fontsizeall=fontsizesplit[int(fcount1)].split(',');
      pyfontall={};
      pyfontall[int(fcount1)]=pygame.font.Font(fontloadsplit[int(fcount1)], int(fontsizeall[0]));
      pyfontall[int(fcount1)].set_bold(int(fontsizeall[1]));
      pyfontall[int(fcount1)].set_italic(int(fontsizeall[2]));
      pyfontall[int(fcount1)].set_underline(int(fontsizeall[3]));
      if(fcountall == 0):
         print('loading top font file "'+fontloadsplit[int(fcount1)]+'"');
         print('setting top font size '+fontsizeall[0]);
      pycolorall=pycolorsplit[int(fcount1)].split(',');
      fontxyall=fontxysplit[int(fcount1)].split(',');
      pytimeall={};
      pytimeall[int(fcount1)]=pyfontall[int(fcount1)].render(strftime(datetimesplit[int(fcount1)]), 1, (int(pycolorall[0]),int(pycolorall[1]),int(pycolorall[2])));
      pyscreen.blit(pytimeall[int(fcount1)],(int(fontxyall[0]),int(fontxyall[1])));
      fcount1 = fcount1 + 1;
   if(numfiles > 0):
      if(pygame.mixer.get_busy()==0):
         pysound=pygame.mixer.Sound(globfiles[int(countnum)]);
         print('loading sound file "'+globfiles[int(countnum)]+'"');
         pysound.set_volume(float(pysndconfsplit[4]));
         print('setting sound volume %f' % float(pysndconfsplit[4]));
         pychannel=pysound.play(1);
         print('playing sound file "'+globfiles[int(countnum)]+'"');
         if(countnum < maxarraynum):
            countnum = countnum + 1;
         if(countnum > maxarraynum):
            countnum = 0;
   pygame.display.update();
   fpsclock.tick(30);
   fcountall = fcountall + 1;

   for event in pygame.event.get():
      if (event.type == pygame.KEYDOWN):
         if (event.key == pygame.K_LCTRL) or (event.key == pygame.K_RCTRL):
            saveimgnum=0;
            imgdone=False;
            while not imgdone:
               if (os.path.exists('./screenshots/screenshot_%i.png' % saveimgnum) == False):
                  pygame.image.save(pyscreen, './screenshots/screenshot_%i.png' % saveimgnum);
                  print('saving screenshot at file "./screenshots/screenshot_%i.png"' % saveimgnum);
                  imgdone=True;
               saveimgnum = saveimgnum + 1;
         if (event.key == pygame.K_ESCAPE):
            done = True;

if(numfiles > 0):
      pysound.stop();
      print('stoping sound file "'+globfiles[int(countnum)]+'"');
      pygame.mixer.stop();
      print('setting sound mixer');
      pygame.mixer.quit();
      print('uninit pygame sound');

pygame.font.quit();
print('uninit pygame font');
pygame.display.quit();
print('uninit pygame x11 display');
quit();
print('uninit pygame');
print('exiting python');
exit();

