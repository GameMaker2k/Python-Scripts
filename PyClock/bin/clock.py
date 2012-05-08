#!/usr/bin/python2

import os, sys, time, locale, calendar, pygame, glob;
from os import environ, system;
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

pyconfig=open('./config.txt', 'r');
print('loading config file "./config.txt"');
configload=pyconfig.readlines();
fontload=configload[0].rstrip('\n');
fontloadsplit=fontload.split('|');
fonttopload=fontloadsplit[0];
fontbottomload=fontloadsplit[1];
fontsizeload=configload[1].rstrip('\n');
fontloadboth=fontsizeload.split('|');
fonttopsplit=fontloadboth[0].split(',');
if(int(fonttopsplit[1])>1) or (int(fonttopsplit[1])<0):
   fonttopsplit[1] = 0;
if(int(fonttopsplit[2])>1) or (int(fonttopsplit[2])<0):
   fonttopsplit[2] = 0;
if(int(fonttopsplit[3])>1) or (int(fonttopsplit[3])<0):
   fonttopsplit[3] = 0;
fontbottomsplit=fontloadboth[1].split(',');
if(int(fontbottomsplit[1])>1) or (int(fontbottomsplit[1])<0):
   fontbottomsplit[1] = 0;
if(int(fontbottomsplit[2])>1) or (int(fontbottomsplit[2])<0):
   fontbottomsplit[2] = 0;
if(int(fontbottomsplit[3])>1) or (int(fontbottomsplit[3])<0):
   fontbottomsplit[3] = 0;
pycolorload=configload[2].rstrip('\n');
pycolors=pycolorload.split('|');
bgcsplit=pycolors[0].split(',');
tfncsplit=pycolors[1].split(',');
bfncsplit=pycolors[2].split(',');
fontxyload=configload[3].rstrip('\n');
bothfontxy=fontxyload.split('|');
topfontxy=bothfontxy[0].rstrip('\n');
tfxysplit=topfontxy.split(',');
bottomfontxy=bothfontxy[1].rstrip('\n');
bfxysplit=bottomfontxy.split(',');
datetimeload=configload[4].rstrip('\n');
datetimeformat=datetimeload.split('|');
dateformat=datetimeformat[0];
timeformat=datetimeformat[1];
displayconf=configload[5].rstrip('\n');
displaysize=configload[6].rstrip('\n');
displaysizesplit=displaysize.split('x');
pysoundfiles=configload[7].rstrip('\n');

environ['SDL_VIDEODRIVER'] = 'x11';
pygame.display.init();
print('init pygame x11 display');

globfiles=glob(pysoundfiles);
numfiles=len(globfiles);
countnum=0;
if(numfiles > 0):
   maxarraynum = numfiles - 1;
   print('number of sound files %i' % numfiles);
   pygame.mixer.init();
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
toppyfont=pygame.font.Font(fonttopload, int(fonttopsplit[0]));
toppyfont.set_bold(int(fonttopsplit[1]));
toppyfont.set_italic(int(fonttopsplit[2]));
toppyfont.set_underline(int(fonttopsplit[3]));
print('loading top font file "'+fonttopload+'"');
print('setting top font size '+fonttopsplit[0]);
bottompyfont=pygame.font.Font(fontbottomload, int(fontbottomsplit[0]));
bottompyfont.set_bold(int(fontbottomsplit[1]));
bottompyfont.set_italic(int(fontbottomsplit[2]));
bottompyfont.set_underline(int(fontbottomsplit[3]));
print('loading bottom font file "'+fontbottomload+'"');
print('setting bottom font size '+fontbottomsplit[0]);

done = False;
while not done:
   pyscreen.fill((int(bgcsplit[0]),int(bgcsplit[1]),int(bgcsplit[2])));
   time1=toppyfont.render(strftime(dateformat), 1, (int(tfncsplit[0]),int(tfncsplit[1]),int(tfncsplit[2])));
   time2=bottompyfont.render(strftime(timeformat), 1, (int(bfncsplit[0]),int(bfncsplit[1]),int(bfncsplit[2])));
   if(int(displayconf)<=0):
      pyscreen.blit(time1,(int(tfxysplit[0]),int(tfxysplit[1])));
      pyscreen.blit(time2,(int(bfxysplit[0]),int(bfxysplit[1])));
   if(int(displayconf)>=1):
      a=pygame.sprite.Sprite();
      a.image=time1;
      a.rect=time1.get_rect();
      a.rect.center=((int(tfxysplit[0]),int(tfxysplit[1])));
      b = pygame.sprite.Sprite();
      b.image=time2;
      b.rect=time2.get_rect();
      b.rect.center=((int(bfxysplit[0]),int(bfxysplit[1])));
      group=pygame.sprite.RenderUpdates(a, b);
      group.clear(pyscreen, pybackground);
      rects = group.draw(pyscreen);
      pygame.display.update(rects);
   pygame.display.update();
   if(numfiles > 0):
      if(pygame.mixer.get_busy()==0):
         pysound=pygame.mixer.Sound(globfiles[int(countnum)]);
         print('loading sound file "'+globfiles[int(countnum)]+'"');
         pysound.set_volume(1.0);
         print('setting sound volume');
         pychannel=pysound.play(1);
         print('playing sound file "'+globfiles[int(countnum)]+'"');
         if(countnum < maxarraynum):
            countnum = countnum + 1;
         if(countnum > maxarraynum):
            countnum = 0;

   for event in pygame.event.get():
      if (event.type == KEYUP) or (event.type == KEYDOWN):
         if (event.key == K_ESCAPE):
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

