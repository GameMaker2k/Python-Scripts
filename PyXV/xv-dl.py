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
from __future__ import absolute_import, division, print_function

import argparse
import datetime
import gzip
import os
import re
import sys
import time
import urllib

import cookielib
import pygame
import StringIO
import urllib2
import urlparse

parser = argparse.ArgumentParser()
parser.add_argument("-name", help="title name")
parser.add_argument("file", nargs="*", help="file name")
parser.add_argument(
    "--user-agent",
    nargs="?",
    default="Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0",
    help="specify a custom user agent")
parser.add_argument("--referer", nargs="?", default="http://motherless.com/",
                    help="specify a custom referer, use if the video access")
getargs = parser.parse_args()
fakeua = getargs.user_agent
geturls_cj = cookielib.CookieJar()
geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(geturls_cj))
geturls_opener.addheaders = [
    ("Referer",
     getargs.referer),
    ("User-Agent",
     fakeua),
    ("Accept-Encoding",
     "gzip, deflate"),
    ("Accept-Language",
     "en-US,en;q=0.8,en-CA,en-GB;q=0.6"),
    ("Accept-Charset",
     "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"),
    ("Accept",
     "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Connection",
     "close")]
if (getargs.file is None or len(getargs.file) == 0):
    pygame.display.quit()
    pygame.quit()
    sys.exit(0)
numurlarg = len(getargs.file)
cururlarg = 0
while (cururlarg < numurlarg):
    geturls_text = geturls_opener.open(getargs.file[cururlarg])
    if (geturls_text.info().get("Content-Encoding") ==
            "gzip" or geturls_text.info().get("Content-Encoding") == "deflate"):
        strbuf = StringIO.StringIO(geturls_text.read())
        gzstrbuf = gzip.GzipFile(fileobj=strbuf)
        outbuf = StringIO.StringIO(gzstrbuf.read()[:])
    if (geturls_text.info().get("Content-Encoding") !=
            "gzip" and geturls_text.info().get("Content-Encoding") != "deflate"):
        outbuf = StringIO.StringIO(geturls_text.read()[:])
    pygame.display.init()
    pyres = (pygame.display.Info().current_h, pygame.display.Info().current_w)
    ppmimg = pygame.image.load(outbuf)
    width, height = ppmimg.get_size()
    if (width > pyres[0] or height > pyres[1]):
        dest_w = float(pyres[0])
        dest_h = float(pyres[1])
        scale = dest_w / width
        if (height * scale > dest_h):
            scale = dest_h / height
        size = (int(width * scale), int(height * scale))
        width = size[0]
        height = size[1]
    ppmimg = pygame.transform.scale(ppmimg, (width, height))
    screen = pygame.display.set_mode((width, height))
    if (getargs.name is not None):
        pygame.display.set_caption("PyXV - " + str(getargs.name))
    if (getargs.name is None):
        pygame.display.set_caption("PyXV - " + str(getargs.file[cururlarg]))
    pygame.display.get_active()
    pygame.mouse.set_visible(0)
    screen.blit(ppmimg, (0, 0))
    pygame.display.flip()
    pygame.display.toggle_fullscreen()
    done = False
    while not done:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                done = True
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_t) or (event.key == pygame.K_w):
                    pygame.display.toggle_fullscreen()
                if (event.key == pygame.K_i) or (event.key == pygame.K_m):
                    pygame.display.iconify()
                if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                    done = True
    pygame.display.quit()
    pygame.quit()
    cururlarg = cururlarg + 1
sys.exit(0)
