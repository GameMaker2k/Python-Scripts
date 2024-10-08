#!/usr/bin/env python

'''
This program is free software; you can redistribute it and/or modify
it under the terms of the Revised BSD License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
Revised BSD License for more details.

Copyright 2014 Cool Dude 2k - http://idb.berlios.de/
Copyright 2014 Game Maker 2k - http://intdb.sourceforge.net/
Copyright 2014 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

$FileInfo: miss-bone-alt.py - Last Update: 6/12/2014 Ver. 1.0.0 RC 1 - Author: cooldude2k $
'''

import argparse
import datetime
import gzip
import os
import re
import sys
import time
import urllib

import cookielib
import StringIO
import urllib2
import urlparse

fakeua = "Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0"
geturls_cj = cookielib.CookieJar()
geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(geturls_cj))
geturls_opener.addheaders = [
    ("Referer",
     "http://www.cute-factor.com/general-news/835-more-than-400-miss-bone-emoticons.html"),
    ("User-Agent",
     fakeua),
    ("Accept-Encoding",
     "gzip, deflate"),
    ("Accept-Language",
     "en-US,en-CA,en-GB,en-UK,en-AU,en-NZ,en-ZA,en;q=0.5"),
    ("Accept-Charset",
     "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"),
    ("Accept",
     "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Connection",
     "close")]
sfcountsub = 0
sfcountfull = 0
i = 1
il = 11
while (i < il):
    print(
        str(i) +
        " Reading URL: http://www.cute-factor.com/imlister.php?cid=missbone&type=e&pp=49&page=" +
        str(i))
    geturls_text = geturls_opener.open(
        "http://www.cute-factor.com/imlister.php?cid=missbone&type=e&pp=49&page=" +
        str(i))
    if (geturls_text.info().get("Content-Encoding") ==
            "gzip" or geturls_text.info().get("Content-Encoding") == "deflate"):
        strbuf = StringIO.StringIO(geturls_text.read())
        gzstrbuf = gzip.GzipFile(fileobj=strbuf)
        out_text = gzstrbuf.read()[:]
    if (geturls_text.info().get("Content-Encoding") !=
            "gzip" and geturls_text.info().get("Content-Encoding") != "deflate"):
        out_text = geturls_text.read()[:]
    regex_text = re.escape("<img alt='Miss Bone Emoticons ") + \
        "([0-9]+)" + re.escape("' src=\"") + "(.*?)" + re.escape("\" border=0>")
    post_text = re.findall(regex_text, out_text)
    isub = 0
    ilsub = len(post_text)
    print(str(i) + " Found " + str(ilsub) + " GIF Images.")
    while (isub < ilsub):
        getsub2xurls_cj = geturls_cj
        getsub2xurls_opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(getsub2xurls_cj))
        getsub2xurls_opener.addheaders = [
            ("Referer",
             "http://www.cute-factor.com/imlister.php?cid=missbone&type=e&pp=49&page=" +
             str(i)),
            ("User-Agent",
             fakeua),
            ("Accept-Encoding",
             "gzip, deflate"),
            ("Accept-Language",
             "en-US,en-CA,en-GB,en-UK,en-AU,en-NZ,en-ZA,en;q=0.5"),
            ("Accept-Charset",
             "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"),
            ("Accept",
             "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
            ("Connection",
             "close")]
        print(str(i) + "," + str(isub + 1) + " Start Downloading Image File: " +
              str(isub + 1) + " of " + str(ilsub))
        print(str(i) + "," + str(isub + 1) +
              " Downloading Image: " + post_text[isub][1])
        getsub2xurls_text = getsub2xurls_opener.open(post_text[isub][1])
        gif_file_name = os.path.basename(
            urlparse.urlparse(post_text[isub][1]).path)
        print(str(i) + "," + str(isub + 1) +
              " Finished Downloading Image: " + post_text[isub][1])
        print(str(i) + "," + str(isub + 1) +
              " Saving File: ./" + gif_file_name)
        gifsf = open("./" + gif_file_name, "wb")
        gifsf.write(getsub2xurls_text.read())
        gifsf.close()
        isub = isub + 1
        sfcountsub = sfcountsub + 1
    print(str(i) + " Downloaded " + str(sfcountsub) + " GIF Images")
    sfcountfull = sfcountfull + sfcountsub
    sfcountsub = 0
    i = i + 1
print("Downloaded " + str(sfcountfull) + " GIF Images")
sfcountfull = 0
