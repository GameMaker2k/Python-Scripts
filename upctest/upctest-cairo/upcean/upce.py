#!/usr/bin/python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2012 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2012 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2012 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: upce.py - Last Update: 10/04/2012 Ver. 2.0.0 - Author: cooldude2k $
'''

from __future__ import division;
import cairo, re, sys, upcean.precairo, upcean.validate, upcean.convert;
import upcean.ean2, upcean.ean5;
from upcean.precairo import *;
from upcean.validate import *;
from upcean.convert import *;
from upcean.ean2 import *;
from upcean.ean5 import *;

def create_upce(upc,outfile="./upce.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54)):
 upc = str(upc);
 hidesn = hideinfo[0];
 hidecd = hideinfo[1];
 hidetext = hideinfo[2];
 upc_pieces = None; supplement = None;
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(re.findall("([0-9]+)([ |\|]){1}([0-9]{5})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]){1}([0-9]{5})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(len(upc)==12):
  upc = convert_upca_to_upce(upc);
 if(len(upc)==13):
  upc = convert_ean13_to_upce(upc);
 if(len(upc)==7):
  upc = upc+validate_upce(upc,True);
 if(len(upc)>8 or len(upc)<8):
  return False;
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 if(not re.findall("^(0|1)", upc)):
  return False;
 if(validate_upce(upc)==False):
  pre_matches = re.findall("^(\d{7})", upc); 
  upc = pre_matches[0]+str(validate_upce(pre_matches[0],True));
 upc_matches = re.findall("(\d{1})(\d{6})(\d{1})", upc);
 upc_matches = upc_matches[0];
 if(len(upc_matches)<=0):
  return False;
 if(int(upc_matches[0])>1):
  return False;
 PrefixDigit = upc_matches[0];
 LeftDigit = list(upc_matches[1]);
 CheckDigit = upc_matches[2];
 addonsize = 0;
 if(supplement!=None and len(supplement)==2): 
  addonsize = 29;
 if(supplement!=None and len(supplement)==5): 
  addonsize = 56;
 upc_preimg = cairo.ImageSurface(cairo.FORMAT_RGB24, 69 + addonsize, barheight[1] + 8);
 upc_img = cairo.Context (upc_preimg);
 upc_img.set_antialias(cairo.ANTIALIAS_NONE);
 upc_img.rectangle(0, 0, 69 + addonsize, barheight[1] + 8);
 upc_img.set_source_rgb(256, 256, 256);
 upc_img.fill();
 text_color = (0, 0, 0);
 alt_text_color = (256, 256, 256);
 if(hidetext==False):
  if(hidesn!=None and hidesn!=True):
   drawColorText(upc_img, 10, 0, barheight[1] + 2, upc_matches[0], text_color);
  drawColorText(upc_img, 10, 14, barheight[1] + 2, upc_matches[1], text_color);
  if(hidecd!=None and hidecd!=True):
   drawColorText(upc_img, 10, 60, barheight[1] + 2, upc_matches[2], text_color);
 drawColorLine(upc_img, 0, 10, 0, barheight[0], alt_text_color);
 drawColorLine(upc_img, 1, 10, 1, barheight[0], alt_text_color);
 drawColorLine(upc_img, 2, 10, 2, barheight[0], alt_text_color);
 drawColorLine(upc_img, 3, 10, 3, barheight[0], alt_text_color);
 drawColorLine(upc_img, 4, 10, 4, barheight[0], alt_text_color);
 drawColorLine(upc_img, 5, 10, 5, barheight[0], alt_text_color);
 drawColorLine(upc_img, 6, 10, 6, barheight[0], alt_text_color);
 drawColorLine(upc_img, 7, 10, 7, barheight[0], alt_text_color);
 drawColorLine(upc_img, 8, 10, 8, barheight[0], alt_text_color);
 drawColorLine(upc_img, 9, 10, 9, barheight[1], text_color);
 drawColorLine(upc_img, 10, 10, 10, barheight[1], alt_text_color);
 drawColorLine(upc_img, 11, 10, 11, barheight[1], text_color);
 NumZero = 0; 
 LineStart = 12;
 while (NumZero < len(LeftDigit)):
  LineSize = barheight[0];
  if(hidetext==True):
   LineSize = barheight[1];
  left_text_color = [0, 0, 0, 0, 0, 0, 0];
  left_text_color_odd = [0, 0, 0, 0, 0, 0, 0];
  left_text_color_even = [0, 0, 0, 0, 0, 0, 0];
  if(int(LeftDigit[NumZero])==0): 
   left_text_color_odd = [0, 0, 0, 1, 1, 0, 1]; 
   left_text_color_even = [0, 1, 0, 0, 1, 1, 1];
  if(int(LeftDigit[NumZero])==1): 
   left_text_color_odd = [0, 0, 1, 1, 0, 0, 1]; 
   left_text_color_even = [0, 1, 1, 0, 0, 1, 1];
  if(int(LeftDigit[NumZero])==2): 
   left_text_color_odd = [0, 0, 1, 0, 0, 1, 1]; 
   left_text_color_even = [0, 0, 1, 1, 0, 1, 1];
  if(int(LeftDigit[NumZero])==3): 
   left_text_color_odd = [0, 1, 1, 1, 1, 0, 1]; 
   left_text_color_even = [0, 1, 0, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==4): 
   left_text_color_odd = [0, 1, 0, 0, 0, 1, 1]; 
   left_text_color_even = [0, 0, 1, 1, 1, 0, 1];
  if(int(LeftDigit[NumZero])==5): 
   left_text_color_odd = [0, 1, 1, 0, 0, 0, 1]; 
   left_text_color_even = [0, 1, 1, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==6): 
   left_text_color_odd = [0, 1, 0, 1, 1, 1, 1]; 
   left_text_color_even = [0, 0, 0, 0, 1, 0, 1];
  if(int(LeftDigit[NumZero])==7): 
   left_text_color_odd = [0, 1, 1, 1, 0, 1, 1]; 
   left_text_color_even = [0, 0, 1, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==8): 
   left_text_color_odd = [0, 1, 1, 0, 1, 1, 1]; 
   left_text_color_even = [0, 0, 0, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==9):
   left_text_color_odd = [0, 0, 0, 1, 0, 1, 1];
   left_text_color_even = [0, 0, 1, 0, 1, 1, 1];
  left_text_color = left_text_color_odd;
  if(int(upc_matches[2])==0 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==1 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==2 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==3 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==4 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==5 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==6 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==7 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==8 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==9 and int(upc_matches[0])==0):
   if(NumZero==0): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==0 and int(upc_matches[0])==1):
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==1 and int(upc_matches[0])==1):
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==2 and int(upc_matches[0])==1):
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==3 and int(upc_matches[0])==1):
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==4 and int(upc_matches[0])==1):
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==5 and int(upc_matches[0])==1):
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==6 and int(upc_matches[0])==1):
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==7 and int(upc_matches[0])==1):
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==5): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==8 and int(upc_matches[0])==1):
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==3): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
  if(int(upc_matches[2])==9 and int(upc_matches[0])==1):
   if(NumZero==1): 
    left_text_color = left_text_color_even;
   if(NumZero==2): 
    left_text_color = left_text_color_even;
   if(NumZero==4): 
    left_text_color = left_text_color_even;
  InnerUPCNum = 0;
  while (InnerUPCNum < len(left_text_color)):
   if(left_text_color[InnerUPCNum]==1):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, text_color);
   if(left_text_color[InnerUPCNum]==0):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, alt_text_color);
   LineStart += 1;
   InnerUPCNum += 1;
  NumZero += 1;
 drawColorLine(upc_img, 54, 10, 54, barheight[1], alt_text_color);
 drawColorLine(upc_img, 55, 10, 55, barheight[1], text_color);
 drawColorLine(upc_img, 56, 10, 56, barheight[1], alt_text_color);
 drawColorLine(upc_img, 57, 10, 57, barheight[1], text_color);
 drawColorLine(upc_img, 58, 10, 58, barheight[1], alt_text_color);
 drawColorLine(upc_img, 59, 10, 59, barheight[1], text_color);
 drawColorLine(upc_img, 60, 10, 60, barheight[0], alt_text_color);
 drawColorLine(upc_img, 61, 10, 61, barheight[0], alt_text_color);
 drawColorLine(upc_img, 62, 10, 62, barheight[0], alt_text_color);
 drawColorLine(upc_img, 63, 10, 63, barheight[0], alt_text_color);
 drawColorLine(upc_img, 64, 10, 64, barheight[0], alt_text_color);
 drawColorLine(upc_img, 65, 10, 65, barheight[0], alt_text_color);
 drawColorLine(upc_img, 66, 10, 66, barheight[0], alt_text_color);
 drawColorLine(upc_img, 67, 10, 67, barheight[0], alt_text_color);
 drawColorLine(upc_img, 68, 10, 68, barheight[0], alt_text_color);
 if(supplement!=None and len(supplement)==2):
  create_ean2(supplement,69,upc_img,hidetext,barheight);
 if(supplement!=None and len(supplement)==5):
  create_ean5(supplement,69,upc_img,hidetext,barheight);
 upc_imgpat = cairo.SurfacePattern(upc_preimg);
 scaler = cairo.Matrix();
 scaler.scale(1/int(resize),1/int(resize));
 upc_imgpat.set_matrix(scaler);
 upc_imgpat.set_filter(cairo.FILTER_NEAREST);
 new_upc_preimg = cairo.ImageSurface(cairo.FORMAT_RGB24, (69 + addonsize) * int(resize), (barheight[1] + 8) * int(resize));
 new_upc_img = cairo.Context(new_upc_preimg);
 new_upc_img.set_source(upc_imgpat);
 new_upc_img.paint();
 del(upc_preimg);
 if(sys.version[0]=="2"):
  if(outfile=="-" or outfile=="" or outfile==" "):
   new_upc_preimg.write_to_png(sys.stdout);
 if(sys.version[0]=="3"):
  if(outfile=="-" or outfile=="" or outfile==" "):
   new_upc_preimg.write_to_png(sys.stdout.buffer);
 if(outfile!="-" and outfile!="" and outfile!=" "):
  new_upc_preimg.write_to_png(outfile);
 return True;
