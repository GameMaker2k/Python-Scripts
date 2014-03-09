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

    $FileInfo: count.py - Last Update: 03/09/2014 Ver 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import sys, os, time, datetime;
from datetime import datetime

y = 0;
z = 0;
if(len(sys.argv) >= 2):
 x = int(sys.argv[1]);
if(len(sys.argv) >= 3):
 y = int(sys.argv[2]); 
if(len(sys.argv) >= 4):
 z = int(sys.argv[3]);
if(len(sys.argv) >= 5):
 fp = open(sys.argv[4], "w+");
if(len(sys.argv) <= 1):
 print("Executing %s" % (sys.argv[0]));
if(len(sys.argv) == 2):
 print("Executing %s with argument %s" % (sys.argv[0], sys.argv[1]));
if(len(sys.argv) == 3):
 print("Executing %s with argument %s,%s" % (sys.argv[0], sys.argv[1], sys.argv[2]));
if(len(sys.argv) == 4):
 print("Executing %s with argument %s,%s,%s" % (sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3]));
if(len(sys.argv) == 5):
 print("Executing %s with argument %s,%s,%s,%s" % (sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]));
 fp.write("Executing %s with argument %s,%s,%s,%s" % (sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]));
 print("Writing output to file %s" % (sys.argv[4]));
 fp.write("Writing output to file %s" % (sys.argv[4]));
if(len(sys.argv) <= 1):
 try:
  prex = raw_input("Please enter a number to count to: ");
 except NameError:
  prex = input("Please enter a number to count to: ");
 x = int(prex);
if(len(sys.argv) <= 2):
 try:
  prey = raw_input("Please enter a number to start at: ");
 except NameError:
  prey = input("Please enter a number to start at: ");
 y = int(prey);
if(len(sys.argv) <= 3):
 try:
  prez = raw_input("Please enter a number to cont by: ");
 except NameError:
  prez = input("Please enter a number to cont by: ");
 z = int(prez);
print("You entered numbers %d,%d,%d" % (x, y, z));
if(len(sys.argv) >= 5):
 fp.write("You entered numbers %d,%d,%d" % (x, y, z));
tstart = datetime.now();
if(z == 0):
 z = 1;
if(x <= y):
 while (y >= x):
  print(str(y));
  if(len(sys.argv) >= 5):
   fp.write(str(y));
  if(z > 1 or z < 0):
   y = y - z;
  if(z == 1):
   y = y - 1;
elif(x > y):
 while (y <= x):
  print(str(y));
  if(len(sys.argv) >= 5):
   fp.write(str(y));
  if(z > 1 or z < 0):
   y = y + z;
  if(z == 1):
   y = y + 1;
tend = datetime.now();
tcheck = tend - tstart;
print(sys.argv[0]+" executed in "+str(tcheck)+" seconds");
if(len(sys.argv) >= 5):
 fp.write(sys.argv[0]+" executed in "+str(tcheck)+" seconds\n");
if(len(sys.argv) >= 5):
 fp.close();
