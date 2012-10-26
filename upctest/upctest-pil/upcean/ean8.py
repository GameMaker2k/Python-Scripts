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

    $FileInfo: ean8.py - Last Update: 10/04/2012 Ver. 2.0.0 - Author: cooldude2k $
'''

from __future__ import division;
import Image, ImageDraw, ImageFont, re, os, sys, upcean.prepil, upcean.validate, upcean.convert;
import upcean.ean2, upcean.ean5;
from upcean.prepil import *;
from upcean.validate import *;
from upcean.convert import *;
from upcean.ean2 import *;
from upcean.ean5 import *;

def create_ean8(upc,outfile="./ean8.png",resize=1,hideinfo=(False, False, False),barheight=(47, 53)):
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
 if(len(upc)==7):
  upc = upc+validate_ean8(upc,True);
 if(len(upc)>8 or len(upc)<8):
  return False;
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 if(validate_ean8(upc)==False):
  pre_matches = preg_match("^(\d{7})", upc); 
  upc = pre_matches[0]+str(validate_ean8(pre_matches[0],true));
 upc_matches = re.findall("(\d{4})(\d{4})", upc);
 upc_matches = upc_matches[0];
 if(len(upc_matches)<=0):
  return False;
 LeftDigit = list(upc_matches[0]);
 upc_matches_new = re.findall("(\d{2})(\d{2})", upc_matches[0]);
 upc_matches_new= upc_matches_new[0];
 LeftLeftDigit = upc_matches_new[0];
 LeftRightDigit = upc_matches_new[1];
 RightDigit = list(upc_matches[1]);
 upc_matches_new = re.findall("(\d{2})(\d{2})", upc_matches[1]);
 upc_matches_new= upc_matches_new[0];
 RightLeftDigit = upc_matches_new[0];
 RightRightDigit = upc_matches_new[1];
 addonsize = 0;
 if(supplement!=None and len(supplement)==2): 
  addonsize = 29;
 if(supplement!=None and len(supplement)==5): 
  addonsize = 56;
 upc_preimg = Image.new("RGB", (83 + addonsize, barheight[1] + 9));
 upc_img = ImageDraw.Draw(upc_preimg);
 upc_img.rectangle([(0, 0), (83 + addonsize, barheight[1] + 9)], fill=(256, 256, 256));
 text_color = (0, 0, 0);
 alt_text_color = (256, 256, 256);
 if(hidetext==False):
  if(hidesn!=None and hidesn!=True):
   drawColorText(upc_img, 10, 12, barheight[0], LeftLeftDigit, text_color);
  drawColorText(upc_img, 10, 25, barheight[0], LeftRightDigit, text_color);
  drawColorText(upc_img, 10, 44, barheight[0], RightLeftDigit, text_color);
  drawColorText(upc_img, 10, 57, barheight[0], RightRightDigit, text_color);
 drawColorLine(upc_img, 0, 10, 0, barheight[0], alt_text_color);
 drawColorLine(upc_img, 1, 10, 1, barheight[0], alt_text_color);
 drawColorLine(upc_img, 2, 10, 2, barheight[0], alt_text_color);
 drawColorLine(upc_img, 3, 10, 3, barheight[0], alt_text_color);
 drawColorLine(upc_img, 4, 10, 4, barheight[0], alt_text_color);
 drawColorLine(upc_img, 5, 10, 5, barheight[0], alt_text_color);
 drawColorLine(upc_img, 6, 10, 6, barheight[0], alt_text_color);
 drawColorLine(upc_img, 7, 10, 7, barheight[1], text_color);
 drawColorLine(upc_img, 8, 10, 8, barheight[1], alt_text_color);
 drawColorLine(upc_img, 9, 10, 9, barheight[1], text_color);
 NumZero = 0; 
 LineStart = 10;
 while (NumZero < len(LeftDigit)):
  LineSize = barheight[0];
  if(hidetext==True):
   LineSize = barheight[1];
  left_text_color_l = [0, 0, 0, 0, 0, 0, 0]; 
  left_text_color_g = [1, 1, 1, 1, 1, 1, 1];
  if(int(LeftDigit[NumZero])==0): 
   left_text_color_l = [0, 0, 0, 1, 1, 0, 1]; 
   left_text_color_g = [0, 1, 0, 0, 1, 1, 1];
  if(int(LeftDigit[NumZero])==1): 
   left_text_color_l = [0, 0, 1, 1, 0, 0, 1]; 
   left_text_color_g = [0, 1, 1, 0, 0, 1, 1];
  if(int(LeftDigit[NumZero])==2): 
   left_text_color_l = [0, 0, 1, 0, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 1, 0, 1, 1];
  if(int(LeftDigit[NumZero])==3): 
   left_text_color_l = [0, 1, 1, 1, 1, 0, 1]; 
   left_text_color_g = [0, 1, 0, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==4): 
   left_text_color_l = [0, 1, 0, 0, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 1, 1, 0, 1];
  if(int(LeftDigit[NumZero])==5): 
   left_text_color_l = [0, 1, 1, 0, 0, 0, 1]; 
   left_text_color_g = [0, 1, 1, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==6): 
   left_text_color_l = [0, 1, 0, 1, 1, 1, 1]; 
   left_text_color_g = [0, 0, 0, 0, 1, 0, 1];
  if(int(LeftDigit[NumZero])==7): 
   left_text_color_l = [0, 1, 1, 1, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==8): 
   left_text_color_l = [0, 1, 1, 0, 1, 1, 1]; 
   left_text_color_g = [0, 0, 0, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==9):
   left_text_color_l = [0, 0, 0, 1, 0, 1, 1];
   left_text_color_g = [0, 0, 1, 0, 1, 1, 1];
  left_text_color = left_text_color_l;
  if(int(upc_matches[1])==1):
   if(NumZero==2):
    left_text_color = left_text_color_g;
   if(NumZero==4):
    left_text_color = left_text_color_g;
   if(NumZero==5):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==2):
   if(NumZero==2):
    left_text_color = left_text_color_g;
   if(NumZero==3):
    left_text_color = left_text_color_g;
   if(NumZero==5):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==3):
   if(NumZero==2):
    left_text_color = left_text_color_g;
   if(NumZero==3):
    left_text_color = left_text_color_g;
   if(NumZero==4):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==4):
   if(NumZero==1):
    left_text_color = left_text_color_g;
   if(NumZero==4):
    left_text_color = left_text_color_g;
   if(NumZero==5):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==5):
   if(NumZero==1):
    left_text_color = left_text_color_g;
   if(NumZero==2):
    left_text_color = left_text_color_g;
   if(NumZero==5):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==6):
   if(NumZero==1):
    left_text_color = left_text_color_g;
   if(NumZero==2):
    left_text_color = left_text_color_g;
   if(NumZero==3):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==7):
   if(NumZero==1):
    left_text_color = left_text_color_g;
   if(NumZero==3):
    left_text_color = left_text_color_g;
   if(NumZero==5):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==8):
   if(NumZero==1):
    left_text_color = left_text_color_g;
   if(NumZero==3):
    left_text_color = left_text_color_g;
   if(NumZero==4):
    left_text_color = left_text_color_g;
  if(int(upc_matches[1])==9):
   if(NumZero==1):
    left_text_color = left_text_color_g;
   if(NumZero==2):
    left_text_color = left_text_color_g;
   if(NumZero==4):
    left_text_color = left_text_color_g;
  InnerUPCNum = 0;
  while (InnerUPCNum < len(left_text_color)):
   if(left_text_color[InnerUPCNum]==1):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, text_color);
   if(left_text_color[InnerUPCNum]==0):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, alt_text_color);
   LineStart += 1;
   InnerUPCNum += 1;
  NumZero += 1;
 drawColorLine(upc_img, 38, 10, 38, barheight[1], alt_text_color);
 drawColorLine(upc_img, 39, 10, 39, barheight[1], text_color);
 drawColorLine(upc_img, 40, 10, 40, barheight[1], alt_text_color);
 drawColorLine(upc_img, 41, 10, 41, barheight[1], text_color);
 drawColorLine(upc_img, 42, 10, 42, barheight[1], alt_text_color);
 NumZero = 0; LineStart = 43;
 while (NumZero < len(RightDigit)):
  LineSize = barheight[0];
  if(hidetext==True):
   LineSize = barheight[1];
  right_text_color = [0, 0, 0, 0, 0, 0, 0];
  if(int(RightDigit[NumZero])==0): 
   right_text_color = [1, 1, 1, 0, 0, 1, 0];
  if(int(RightDigit[NumZero])==1): 
   right_text_color = [1, 1, 0, 0, 1, 1, 0];
  if(int(RightDigit[NumZero])==2): 
   right_text_color = [1, 1, 0, 1, 1, 0, 0];
  if(int(RightDigit[NumZero])==3): 
   right_text_color = [1, 0, 0, 0, 0, 1, 0];
  if(int(RightDigit[NumZero])==4): 
   right_text_color = [1, 0, 1, 1, 1, 0, 0];
  if(int(RightDigit[NumZero])==5): 
   right_text_color = [1, 0, 0, 1, 1, 1, 0];
  if(int(RightDigit[NumZero])==6): 
   right_text_color = [1, 0, 1, 0, 0, 0, 0];
  if(int(RightDigit[NumZero])==7): 
   right_text_color = [1, 0, 0, 0, 1, 0, 0];
  if(int(RightDigit[NumZero])==8): 
   right_text_color = [1, 0, 0, 1, 0, 0, 0];
  if(int(RightDigit[NumZero])==9): 
   right_text_color = [1, 1, 1, 0, 1, 0, 0];
  InnerUPCNum = 0;
  while (InnerUPCNum < len(right_text_color)):
   if(right_text_color[InnerUPCNum]==1):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, text_color);
   if(right_text_color[InnerUPCNum]==0):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, alt_text_color);
   LineStart += 1;
   InnerUPCNum += 1;
  NumZero += 1;

 drawColorLine(upc_img, 71, 10, 71, barheight[1], text_color);
 drawColorLine(upc_img, 72, 10, 72, barheight[1], alt_text_color);
 drawColorLine(upc_img, 73, 10, 73, barheight[1], text_color);
 drawColorLine(upc_img, 74, 10, 74, barheight[0], alt_text_color);
 drawColorLine(upc_img, 75, 10, 75, barheight[0], alt_text_color);
 drawColorLine(upc_img, 76, 10, 76, barheight[0], alt_text_color);
 drawColorLine(upc_img, 77, 10, 77, barheight[0], alt_text_color);
 drawColorLine(upc_img, 78, 10, 78, barheight[0], alt_text_color);
 drawColorLine(upc_img, 79, 10, 79, barheight[0], alt_text_color);
 drawColorLine(upc_img, 80, 10, 80, barheight[0], alt_text_color);
 drawColorLine(upc_img, 81, 10, 81, barheight[0], alt_text_color);
 drawColorLine(upc_img, 82, 10, 82, barheight[0], alt_text_color);
 if(supplement!=None and len(supplement)==2):
  create_ean2(supplement,83,upc_img,hidetext,barheight);
 if(supplement!=None and len(supplement)==5):
  create_ean5(supplement,83,upc_img,hidetext,barheight);
 '''
 upc_imgpat = cairo.SurfacePattern(upc_preimg);
 scaler = cairo.Matrix();
 scaler.scale(1/int(resize),1/int(resize));
 upc_imgpat.set_matrix(scaler);
 upc_imgpat.set_filter(cairo.FILTER_BEST);
 new_upc_preimg = cairo.ImageSurface(cairo.FORMAT_RGB24, (83 + addonsize) * int(resize), (barheight[1] + 9) * int(resize));
 new_upc_img = cairo.Context(new_upc_preimg);
 new_upc_img.set_source(upc_imgpat);
 new_upc_img.paint();
 '''
 '''
 new_upc_img = upc_preimg.resize(((83 + addonsize) * int(resize), (barheight[1] + 9) * int(resize)), Image.BILINEAR) # linear interpolation in a 2x2 environment
 '''
 new_upc_img = upc_preimg.resize(((83 + addonsize) * int(resize), (barheight[1] + 9) * int(resize)), Image.NEAREST) # use nearest neighbour
 '''
 new_upc_img = upc_preimg.resize(((83 + addonsize) * int(resize), (barheight[1] + 9) * int(resize)), Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
 new_upc_img = upc_preimg.resize(((83 + addonsize) * int(resize), (barheight[1] + 9) * int(resize)), Image.ANTIALIAS) # best down-sizing filter
 '''
 del(upc_img);
 del(upc_preimg);
 if(outfile=="-" and sys.version[0]=="2"):
  new_upc_img.save(sys.stdout, "PNG");
 if(outfile=="-" and sys.version[0]=="3"):
  new_upc_img.save(outfile, re.findall("^\.([A-Za-z]+)", os.path.splitext(outfile)[1])[0].upper());
 if(outfile!="-"):
  new_upc_img.save(outfile, re.findall("^\.([A-Za-z]+)", os.path.splitext(outfile)[1])[0].upper());
 return True;
