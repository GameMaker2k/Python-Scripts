#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2016 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2016 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2016 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: pymotherless.py - Last Update: 1/19/2016 Ver. 0.2.9 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import re, os, sys, urllib, gzip, time, datetime, argparse, cgi, subprocess;
if(sys.version[0]=="2"):
 try:
  from cStringIO import StringIO;
 except ImportError:
  from StringIO import StringIO;
 import urllib2, urlparse, cookielib;
if(sys.version[0]=="3"):
 from io import StringIO, BytesIO;
 import urllib.request as urllib2;
 import urllib.parse as urlparse;
 import http.cookiejar as cookielib;
#if(__name__ == "__main__"):
# sys.tracebacklimit = 0;
__program_name__ = "PyMotherless";
__version_info__ = (0, 2, 9, "RC 1");
__version_date__ = "2016.01.19";
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

geturls_cj = cookielib.CookieJar();
geturls_ua_firefox_windows7 = "Mozilla/5.0 (Windows NT 6.1; rv:43.0) Gecko/20100101 Firefox/43.0";
geturls_ua_chrome_windows7 = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36";
geturls_ua_internet_explorer_windows7 = "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko";
geturls_ua = geturls_ua_firefox_windows7;
geturls_headers = [("Referer", "http://motherless.com/"), ("User-Agent", geturls_ua), ("Accept-Encoding", "gzip, deflate"), ("Accept-Language", "en-US,en;q=0.8,en-CA,en-GB;q=0.6"), ("Accept-Charset", "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"), ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"), ("Connection", "close")];
geturls_download_sleep = 0;

def add_url_param(url, **params):
 n=3;
 parts = list(urlparse.urlsplit(url));
 d = dict(cgi.parse_qsl(parts[n])); # use cgi.parse_qs for list values
 d.update(params);
 parts[n]=urllib.urlencode(d);
 return urlparse.urlunsplit(parts);

os.environ["PATH"] = os.environ["PATH"] + os.pathsep + os.path.dirname(os.path.realpath(__file__)) + os.pathsep + os.getcwd();
def which_exec(execfile):
 for path in os.environ["PATH"].split(":"):
  if os.path.exists(path + "/" + execfile):
   return path + "/" + execfile;

def listize(varlist):
 il = 0;
 ix = len(varlist);
 ilx = 1;
 newlistreg = {};
 newlistrev = {};
 newlistfull = {};
 while(il < ix):
  newlistreg.update({ilx: varlist[il]});
  newlistrev.update({varlist[il]: ilx});
  ilx = ilx + 1;
  il = il + 1;
 newlistfull = {1: newlistreg, 2: newlistrev, 'reg': newlistreg, 'rev': newlistrev};
 return newlistfull;

def twolistize(varlist):
 il = 0;
 ix = len(varlist);
 ilx = 1;
 newlistnamereg = {};
 newlistnamerev = {};
 newlistdescreg = {};
 newlistdescrev = {};
 newlistfull = {};
 while(il < ix):
  newlistnamereg.update({ilx: varlist[il][0].strip()});
  newlistnamerev.update({varlist[il][0].strip(): ilx});
  newlistdescreg.update({ilx: varlist[il][1].strip()});
  newlistdescrev.update({varlist[il][1].strip(): ilx});
  ilx = ilx + 1;
  il = il + 1;
 newlistnametmp = {1: newlistnamereg, 2: newlistnamerev, 'reg': newlistnamereg, 'rev': newlistnamerev};
 newlistdesctmp = {1: newlistdescreg, 2: newlistdescrev, 'reg': newlistdescreg, 'rev': newlistdescrev};
 newlistfull = {1: newlistnametmp, 2: newlistdesctmp, 'name': newlistnametmp, 'desc': newlistdesctmp}
 return newlistfull;

def arglistize(proexec, *varlist):
 il = 0;
 ix = len(varlist);
 ilx = 1;
 newarglist = [proexec];
 while(il < ix):
  if varlist[il][0] is not None:
   newarglist.append(varlist[il][0]);
  if varlist[il][1] is not None:
   newarglist.append(varlist[il][1]);
  il = il + 1;
 return newarglist;

def make_http_headers_from_dict(headers={'Referer': "http://motherless.com/", 'User-Agent': geturls_ua, 'Accept-Encoding': "gzip, deflate", 'Accept-Language': "en-US,en;q=0.8,en-CA,en-GB;q=0.6", 'Accept-Charset': "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7", 'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 'Connection': "close"}):
 returnval = [];
 for headkey, headvalue in headers.iteritems():
  returnval.append((headkey, headvalue));
 return returnval;

def download_from_url(httpurl, httpheaders, httpcookie, sleep=-1):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(httpcookie));
 geturls_opener.addheaders = httpheaders;
 time.sleep(sleep);
 geturls_text = geturls_opener.open(httpurl);
 if(geturls_text.info().get("Content-Encoding")=="gzip" or geturls_text.info().get("Content-Encoding")=="deflate"):
  if(sys.version[0]=="2"):
   strbuf = StringIO(geturls_text.read());
  if(sys.version[0]=="3"):
   strbuf = BytesIO(geturls_text.read());
  gzstrbuf = gzip.GzipFile(fileobj=strbuf);
  if(sys.version[0]=="2"):
   returnval = gzstrbuf.read()[:];
  if(sys.version[0]=="3"):
   returnval = gzstrbuf.read()[:].decode('ascii', 'replace');
 if(geturls_text.info().get("Content-Encoding")!="gzip" and geturls_text.info().get("Content-Encoding")!="deflate"):
  returnval = geturls_text.read()[:];
 return returnval;

def download_from_url_file(httpurl, httpheaders, httpcookie, sleep=-1):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(httpcookie));
 geturls_opener.addheaders = httpheaders;
 time.sleep(sleep);
 geturls_text = geturls_opener.open(httpurl);
 if(geturls_text.info().get("Content-Encoding")=="gzip" or geturls_text.info().get("Content-Encoding")=="deflate"):
  if(sys.version[0]=="2"):
   strbuf = StringIO(geturls_text.read());
  if(sys.version[0]=="3"):
   strbuf = BytesIO(geturls_text.read());
  gzstrbuf = gzip.GzipFile(fileobj=strbuf);
  returnval = gzstrbuf.read()[:];
 if(geturls_text.info().get("Content-Encoding")!="gzip" and geturls_text.info().get("Content-Encoding")!="deflate"):
  returnval = geturls_text.read()[:];
 return returnval;

def download_from_url_to_file(httpurl, httpheaders, httpcookie, outfile="-", outpath=os.getcwd(), sleep=-1):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 if(not outfile=="-"):
  outpath = outpath.rstrip(os.path.sep);
  filepath = os.path.realpath(outpath+os.path.sep+outfile);
  if(not os.path.exists(outpath)):
   os.makedirs(outpath);
  if(os.path.exists(outpath) and os.path.isfile(outpath)):
   return False;
  if(os.path.exists(filepath) and os.path.isdir(filepath)):
   return False;
  with open(filepath, 'wb+') as f:
   f.write(download_from_url_file(httpurl, httpheaders, httpcookie, sleep));
  f.closed;
  returnval = True;
 if(outfile=="-" and sys.version[0]=="2"):
  f = StringIO();
  f.write(download_from_url_file(httpurl, httpheaders, httpcookie, sleep));
  returnval = f.getvalue();
  f.closed;
 if(outfile=="-" and sys.version[0]=="3"):
  f = BytesIO();
  f.write(download_from_url_file(httpurl, httpheaders, httpcookie, sleep));
  returnval = f.getvalue();
  f.closed;
 return returnval;

def get_motherless_get_number_pages(httpurl, httpheaders, httpcookie):
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_getpagenum = re.escape("page=")+"([0-9]+)"+re.escape("\" class=\"pop\" rel=\"")+"([0-9]+)"+re.escape("\">")+"([0-9]+)"+re.escape("</a>");
 mlesspagenum = re.findall(mregex_getpagenum, mrtext);
 try:
  returnval = mlesspagenum[-1][0];
 except:
  returnval = 1;
 return returnval;

def get_motherless_get_link_type(httpurl):
 mlessvidqstr = urlparse.parse_qs(urlparse.urlparse(httpurl).query);
 mlessvidid_parts = urlparse.urlparse(httpurl);
 mlessvidid = mlessvidid_parts.path.split("/");
 returnval = False;
 if(mlessvidid[1]=="videos" and len(mlessvidid)==3 and (mlessvidid[2]=="recent" or mlessvidid[2]=="favorited" or mlessvidid[2]=="viewed" or mlessvidid[2]=="commented" or mlessvidid[2]=="popular")):
  returnval = "gallery";
 if(mlessvidid[1]=="images" and len(mlessvidid)==3 and (mlessvidid[2]=="recent" or mlessvidid[2]=="favorited" or mlessvidid[2]=="viewed" or mlessvidid[2]=="commented" or mlessvidid[2]=="popular")):
  returnval = "gallery";
 if(mlessvidid[1]=="galleries" and len(mlessvidid)==3 and (mlessvidid[2]=="recent" or mlessvidid[2]=="favorited" or mlessvidid[2]=="viewed" or mlessvidid[2]=="commented" or mlessvidid[2]=="popular")):
  returnval = "gallery";
 if(mlessvidid[1]=="videos" and len(mlessvidid)==2):
  returnval = "sample-videos";
 if(mlessvidid[1]=="images" and len(mlessvidid)==2):
  returnval = "sample-images";
 if(mlessvidid[1]=="galleries" and len(mlessvidid)==2):
  returnval = "sample-galleries";
 if(mlessvidid[1]=="" and len(mlessvidid)==2):
  returnval = "sample";
 if(mlessvidid[1]=="live" and len(mlessvidid)==3 and (mlessvidid[2]=="videos" or mlessvidid[2]=="images")):
  returnval = "gallery";
 if(mlessvidid[1]=="u" and len(mlessvidid)==3):
  returnval = "gallery";
 if(mlessvidid[1]=="f" and len(mlessvidid)==4 and (mlessvidid[2]=="videos" or mlessvidid[2]=="images" or mlessvidid[2]=="galleries")):
  returnval = "gallery";
 if(mlessvidid[1]=="galleries" and len(mlessvidid)==4 and mlessvidid[2]=="member"):
  returnval = "gallery";
 if(mlessvidid[1]=="galleries" and len(mlessvidid)==5 and mlessvidid[2]=="member" and (mlessvidid[4]=="created" or mlessvidid[4]=="viewed" or mlessvidid[4]=="favorited" or mlessvidid[4]=="commented")):
  returnval = "gallery";
 if(mlessvidid[1]=="gv" and len(mlessvidid)==3):
  returnval = "gallery";
 if(mlessvidid[1]=="gi" and len(mlessvidid)==3):
  returnval = "gallery";
 if(mlessvidid[1]=="term" and len(mlessvidid)==3 and (mlessvidid[2]=="videos" or mlessvidid[2]=="images" or mlessvidid[2]=="galleries")):
  returnval = "gallery";
 if(mlessvidid[1]=="g" and len(mlessvidid)==4):
  returnval = "file";
 if(mlessvidid[1]=="random" and len(mlessvidid)==3 and (mlessvidid[2]=="video" or mlessvidid[2]=="image")):
  returnval = "file";
 if(re.match("^V", mlessvidid[1]) and len(mlessvidid)==2):
  returnval = "board";
 if(mlessvidid[1]=="members" and len(mlessvidid)==2):
  returnval = "member";
 if(mlessvidid[1]=="members" and mlessvidid[2]=="search" and len(mlessvidid)==3):
  returnval = "member";
 if(mlessvidid[1]=="members" and len(mlessvidid)==4 and (mlessvidid[2]=="uploader" or mlessvidid[2]=="viewed" or mlessvidid[2]=="social" or mlessvidid[2]=="favorited" or mlessvidid[2]=="commented" or mlessvidid[2]=="mentioned" or mlessvidid[2]=="verified")):
  returnval = "member";
 if(mlessvidid[1]=="girls" and len(mlessvidid)==2):
  returnval = "girls";
 if(mlessvidid_parts.netloc=="cdn.images.motherlessmedia.com" or mlessvidid_parts.netloc=="cdn.videos.motherlessmedia.com" or mlessvidid_parts.netloc=="cdn.thumbs.motherlessmedia.com"):
  returnval = "download";
 if(returnval==False and len(mlessvidid)==2):
  returnval = "file";
 return returnval;

def get_motherless_links(httpurl, httpheaders, httpcookie):
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_gettitle = re.escape("<title>")+"(.*)"+re.escape(" - MOTHERLESS.COM</title>");
 mlesstitle = re.findall(mregex_gettitle, mrtext);
 mregex_geturlone = re.escape("__fileurl = 'http://cdn.")+"(images|videos)"+re.escape(".motherlessmedia.com/")+"(images|videos)"+re.escape("/")+"([\w\/\?\&\=\.\-]+)"+re.escape("';");
 mlesslinkone = re.findall(mregex_geturlone, mrtext);
 mregex_geturltwo = re.escape("<meta property=\"og:image\" content=\"http://cdn.")+"(images|thumbs)"+re.escape(".motherlessmedia.com/")+"(images|thumbs)"+re.escape("/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\">");
 mlesslinktwo = re.findall(mregex_geturltwo, mrtext);
 filenameext = os.path.basename(urlparse.urljoin("http://cdn."+mlesslinkone[0][0]+".motherlessmedia.com/"+mlesslinkone[0][1]+"/"+mlesslinkone[0][2], urlparse.urlparse("http://cdn."+mlesslinkone[0][0]+".motherlessmedia.com/"+mlesslinkone[0][1]+"/"+mlesslinkone[0][2]).path));
 filename, fileextension = os.path.splitext(filenameext);
 thumbfilenameext = os.path.basename(urlparse.urljoin("http://cdn.images.motherlessmedia.com/"+mlesslinktwo[0][1]+"/"+mlesslinktwo[0][2], urlparse.urlparse("http://cdn.images.motherlessmedia.com/"+mlesslinktwo[0][1]+"/"+mlesslinktwo[0][2]).path));
 thumbfilename, thumbfileextension = os.path.splitext(thumbfilenameext);
 mregex_getuname = re.escape("<tr rel=\"")+"([\w\/\?\&\=\.\-]+)"+re.escape("\"");
 mlessuname = re.findall(mregex_getuname, mrtext);
 mlessuname = mlessuname[0];
 mregex_geturlname = re.escape("<a href=\"/m/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\" target=\"_blank\">\n            <img");
 mlessurlname = re.findall(mregex_geturlname, mrtext);
 mlessurlname = mlessurlname[0];
 mregex_getavatar = re.escape("<img\n    src=\"")+"(.*)"+re.escape("\"\n    class=\"avatar avatar-small\"");
 mlessavatar = re.findall(mregex_getavatar, mrtext);
 mlessavatar = mlessavatar[0];
 avatarfilenameext = os.path.basename(urlparse.urljoin(mlessavatar, urlparse.urlparse(mlessavatar).path));
 avatarfilename, avatarfileextension = os.path.splitext(avatarfilenameext);
 if(mlesslinkone[0][1]=="images"):
  thumbnailaltpart = thumbfilename+"-zoom"+thumbfileextension;
  thumbnailalt = "http://cdn.thumbs.motherlessmedia.com/thumbs/"+thumbnailaltpart;
  thumbnailaltfilenameext = os.path.basename(urlparse.urljoin(thumbnailalt, urlparse.urlparse(thumbnailalt).path));
  thumbnailaltfilename, thumbnailaltfileextension = os.path.splitext(thumbnailaltfilenameext);
 if(mlesslinkone[0][1]=="videos"):
  thumbnailaltpart = +thumbfilename+"-small"+thumbfileextension;
  thumbnailalt = "http://cdn.thumbs.motherlessmedia.com/thumbs/"+thumbnailaltpart;
  thumbnailaltfilenameext = os.path.basename(urlparse.urljoin(thumbnailalt, urlparse.urlparse(thumbnailalt).path));
  thumbnailaltfilename, thumbnailaltfileextension = os.path.splitext(thumbnailaltfilenameext);
 returnval = False;
 mlessurltype = get_motherless_get_link_type("http://cdn."+mlesslinkone[0][0]+".motherlessmedia.com/"+mlesslinkone[0][1]+"/"+mlesslinkone[0][2]);
 if(mlesslinkone[0][1]=="images"):
  returnval = {'type': mlesslinkone[0][1], 'urltype': mlessurltype, 'url': "http://cdn."+mlesslinkone[0][0]+".motherlessmedia.com/"+mlesslinkone[0][1]+"/"+mlesslinkone[0][2], 'orginurl': httpurl, 'orginurltype': get_motherless_get_link_type(httpurl), 'thumbnail': "http://cdn.thumbs.motherlessmedia.com/thumbs/"+mlesslinktwo[0][2], 'thumbnailalt': thumbnailalt+"?from_helper", 'title': mlesstitle[0], 'fullfilename': filenameext, 'filename': filename, 'extension': fileextension, 'thumbfullfilename': thumbfilenameext, 'thumbfilename': thumbfilename, 'thumbextension': thumbfileextension, 'thumbnailaltfullfilename': thumbnailaltpart, 'thumbnailaltfilename': thumbnailaltfilename, 'thumbnailaltextension': thumbnailaltfileextension, 'username': mlessuname, 'avatarurl': mlessavatar, 'avatarfullfilename': avatarfilenameext, 'avatarfilename': avatarfilename, 'avatarextension': avatarfileextension};
 if(mlesslinkone[0][1]=="videos"):
  returnval = {'type': mlesslinkone[0][1], 'url': "http://cdn."+mlesslinkone[0][0]+".motherlessmedia.com/"+mlesslinkone[0][1]+"/"+mlesslinkone[0][2], 'orginurl': httpurl, 'orginurltype': get_motherless_get_link_type(httpurl), 'thumbnail': "http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[0][1]+"/"+mlesslinktwo[0][2], 'thumbnailalt': thumbnailalt+"?from_helper", 'title': mlesstitle[0], 'fullfilename': filenameext, 'filename': filename, 'extension': fileextension, 'thumbfullfilename': thumbfilenameext, 'thumbfilename': thumbfilename, 'thumbextension': thumbfileextension, 'thumbnailaltfullfilename': thumbnailaltpart, 'thumbnailaltfilename': thumbnailaltfilename, 'thumbnailaltextension': thumbnailaltfileextension, 'username': mlessuname, 'avatarurl': mlessavatar, 'avatarfullfilename': avatarfilenameext, 'avatarfilename': avatarfilename, 'avatarextension': avatarfileextension};
 return returnval;

def get_motherless_galleries_links(httpurl, httpheaders, httpcookie, page=1, getlinks=[0, -1]):
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_getpagenum = re.escape("page=")+"([0-9]+)"+re.escape("\" class=\"pop\" rel=\"")+"([0-9]+)"+re.escape("\">")+"([0-9]+)"+re.escape("</a>");
 mlesspagenum = re.findall(mregex_getpagenum, mrtext);
 try:
  lastpage = mlesspagenum[-1][0];
 except:
  lastpage = 1;
 if(page>lastpage):
  page = lastpage;
 httpurl = add_url_param(httpurl, page=str(page));
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_geturlone = re.escape("<a href=\"/")+"([\w\/]+)"+re.escape("\" class=\"img-container\" target=\"_self\">");
 mrtext_tmp = re.sub(re.escape("http://motherless.com"), "", mrtext);
 mrtext_tmp = re.sub(re.escape("http://www.motherless.com"), "", mrtext_tmp);
 mrtext_tmp = re.sub(re.escape("http://motherless.com"), "", mrtext_tmp);
 mrtext_tmp = re.sub(re.escape("http://www.motherless.com"), "", mrtext_tmp);
 mlesslinkone = re.findall(mregex_geturlone, mrtext_tmp);
 mregex_geturltwo = re.escape("<img class=\"static\" src=\"http://cdn.thumbs.motherlessmedia.com/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\" data-strip-src=\"http://cdn.thumbs.motherlessmedia.com/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\" alt=\"")+"(.*)"+re.escape("\" />");
 mlesslinktwo = re.findall(mregex_geturltwo, mrtext);
 mregex_getuserinfo = re.escape("<a class=\"caption left\" href=\"/m/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\">");
 mlessuname = re.findall(mregex_getuserinfo, mrtext);
 if(getlinks[1]>len(mlesslinkone) or getlinks[1]==-1):
  getlinks[1] = len(mlesslinkone);
 if(getlinks[0]>getlinks[1] and not getlinks[1]==-1):
  tmpgetlinks0 = getlinks[0];
  tmpgetlinks1 = getlinks[1];
  getlinks[0] = tmpgetlinks1;
  getlinks[1] = tmpgetlinks0;
 if(getlinks[0]<0):
  getlinks[0] = 0;
 mli = getlinks[0];
 mlil = getlinks[1];
 returnval = {'pages': lastpage};
 returnval.update({'curpage': page});
 returnval.update({'numoflinks': mlil});
 returnval.update({'numofalllinks': len(mlesslinkone)});
 returnval.update({'orginurl': httpurl});
 returnval.update({'orginurltype': get_motherless_get_link_type(httpurl)});
 mlessrooturltype = get_motherless_get_link_type(httpurl);
 returnval.update({'urltype': mlessrooturltype});
 while(mli<mlil):
  stripfilenameext = os.path.basename(urlparse.urljoin("http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[mli][1], urlparse.urlparse("http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[mli][1]).path));
  stripfilename, stripfileextension = os.path.splitext(stripfilenameext);
  thumbfilenameext = os.path.basename(urlparse.urljoin("http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[mli][0], urlparse.urlparse("http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[mli][0]).path));
  thumbfilename, thumbfileextension = os.path.splitext(thumbfilenameext);
  mlessurltype = get_motherless_get_link_type("http://motherless.com/"+mlesslinkone[mli]);
  avatarfilenameext = os.path.basename(urlparse.urljoin("http://cdn.avatars.motherlessmedia.com/thumbs/"+mlessuname[mli]+"-avatar.jpg", urlparse.urlparse("http://cdn.avatars.motherlessmedia.com/thumbs/"+mlessuname[mli]+"-avatar.jpg").path));
  avatarfilename, avatarfileextension = os.path.splitext(avatarfilenameext);
  returnval.update({mli: {'urltype': mlessurltype, 'url': "http://motherless.com/"+mlesslinkone[mli], 'thumbnail': "http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[mli][0], 'strip': "http://cdn.thumbs.motherlessmedia.com/"+mlesslinktwo[mli][1], 'title': mlesslinktwo[mli][2], 'thumbfullfilename': thumbfilenameext, 'thumbfilename': thumbfilename, 'thumbextension': thumbfileextension, 'stripfullfilename': stripfilenameext, 'stripfilename': stripfilename, 'stripextension': stripfileextension, 'username': mlessuname[mli], 'avatarurl': "http://cdn.avatars.motherlessmedia.com/thumbs/"+mlessuname[mli]+"-avatar.jpg", 'avatarfullfilename': avatarfilenameext, 'avatarfilename': avatarfilename, 'avatarextension': avatarfileextension} });
  mli = mli + 1;
 return returnval;

def get_motherless_random_links(httpheaders, httpcookie, linktype, getlinks=[0, 80]):
 if(getlinks[0]>getlinks[1] and not getlinks[1]==-1):
  tmpgetlinks0 = getlinks[0];
  tmpgetlinks1 = getlinks[1];
  getlinks[0] = tmpgetlinks1;
  getlinks[1] = tmpgetlinks0;
 if(getlinks[0]<0):
  getlinks[0] = 0;
 mli = getlinks[0];
 mlil = getlinks[1];
 if(linktype=="image"):
  returnval = {'pages': 1};
  returnval.update({'curpage': 1});
  returnval.update({'numoflinks': 80});
  returnval.update({'numofalllinks': mlil});
  returnval.update({'orginurl': "http://motherless.com/random/image"});
  returnval.update({'orginurltype': "gallery"});
  returnval.update({'urltype': "gallery"});
  while(mli<mlil):
   get_links = get_motherless_links("http://motherless.com/random/image", httpheaders, httpcookie);
   returnval.update({mli: {'urltype': get_motherless_get_link_type("http://motherless.com/"+get_links['filename']), 'url': "http://motherless.com/"+get_links['filename'], 'thumbnail': get_links['thumbnail'], 'strip': get_links['thumbnailalt'], 'title': get_links['title'], 'thumbfullfilename': get_links['thumbfullfilename'], 'thumbfilename': get_links['thumbfilename'], 'thumbextension': get_links['thumbextension'], 'stripfullfilename': get_links['thumbnailaltfullfilename'], 'stripfilename': get_links['thumbnailaltextension'], 'stripextension': get_links['thumbnailaltfilename'], 'username': get_links['username'], 'avatarurl': get_links['avatarurl'], 'avatarfullfilename': get_links['avatarfullfilename'], 'avatarfilename': get_links['avatarfilename'], 'avatarextension': get_links['avatarextension']} });
   mli = mli + 1;
 if(linktype=="video"):
  returnval = {'pages': 1};
  returnval.update({'curpage': 1});
  returnval.update({'numoflinks': 80});
  returnval.update({'numofalllinks': mlil});
  returnval.update({'orginurl': "http://motherless.com/random/video"});
  returnval.update({'orginurltype': "gallery"});
  returnval.update({'urltype': "gallery"});
  while(mli<mlil):
   get_links = get_motherless_links("http://motherless.com/random/video", httpheaders, httpcookie);
   returnval.update({mli: {'urltype': get_motherless_get_link_type("http://motherless.com/"+get_links['filename']), 'url': "http://motherless.com/"+get_links['filename'], 'thumbnail': get_links['thumbnail'], 'strip': get_links['thumbnailalt'], 'title': get_links['title'], 'thumbfullfilename': get_links['thumbfullfilename'], 'thumbfilename': get_links['thumbfilename'], 'thumbextension': get_links['thumbextension'], 'stripfullfilename': get_links['thumbnailaltfullfilename'], 'stripfilename': get_links['thumbnailaltextension'], 'stripextension': get_links['thumbnailaltfilename'], 'username': get_links['username'], 'avatarurl': get_links['avatarurl'], 'avatarfullfilename': get_links['avatarfullfilename'], 'avatarfilename': get_links['avatarfilename'], 'avatarextension': get_links['avatarextension']} });
   mli = mli + 1;
 return returnval;

def get_motherless_boards_links(httpurl, httpheaders, httpcookie, getlinks=[0, -1]):
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_geturlone = re.escape("<a href=\"/")+"([\w\/]+)"+re.escape("\" title=\"motherless link\">");
 mrtext_tmp = re.sub(re.escape("http://motherless.com"), "", mrtext);
 mrtext_tmp = re.sub(re.escape("http://www.motherless.com"), "", mrtext_tmp);
 mrtext_tmp = re.sub(re.escape("http://motherless.com"), "", mrtext_tmp);
 mrtext_tmp = re.sub(re.escape("http://www.motherless.com"), "", mrtext_tmp);
 mlesslinkone = re.findall(mregex_geturlone, mrtext_tmp);
 if(getlinks[1]>len(mlesslinkone) or getlinks[1]==-1):
  getlinks[1] = len(mlesslinkone);
 if(getlinks[0]>getlinks[1] and not getlinks[1]==-1):
  tmpgetlinks0 = getlinks[0];
  tmpgetlinks1 = getlinks[1];
  getlinks[0] = tmpgetlinks1;
  getlinks[1] = tmpgetlinks0;
 if(getlinks[0]<0):
  getlinks[0] = 0;
 mli = getlinks[0];
 mlil = getlinks[1];
 returnval = {'numoflinks': mlil};
 returnval.update({'numofalllinks': len(mlesslinkone)});
 returnval.update({'orginurl': httpurl});
 returnval.update({'orginurltype': get_motherless_get_link_type(httpurl)});
 mlessrooturltype = get_motherless_get_link_type(httpurl);
 returnval.update({'urltype': mlessrooturltype});
 while(mli<mlil):
  mlessurltype = get_motherless_get_link_type("http://motherless.com/"+mlesslinkone[mli]);
  returnval.update({mli: {'urltype': mlessurltype, 'url': "http://motherless.com/"+mlesslinkone[mli]} });
  mli = mli + 1;
 return returnval;

def get_motherless_search_members(httpurl, httpheaders, httpcookie, page=1, getlinks=[0, -1]):
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_getpagenum = re.escape("page=")+"([0-9]+)"+re.escape("\" class=\"pop\" rel=\"")+"([0-9]+)"+re.escape("\">")+"([0-9]+)"+re.escape("</a>");
 mlesspagenum = re.findall(mregex_getpagenum, mrtext);
 try:
  lastpage = mlesspagenum[-1][0];
 except:
  lastpage = 1;
 if(page>lastpage):
  page = lastpage;
 httpurl = add_url_param(httpurl, page=str(page));
 mrtext = download_from_url(httpurl, httpheaders, httpcookie);
 mregex_getuname = re.escape("<tr rel=\"")+"([\w\/\?\&\=\.\-]+)"+re.escape("\"");
 mlessuname = re.findall(mregex_getuname, mrtext);
 mregex_geturlname = re.escape("<a href=\"/m/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\" target=\"_blank\">\n            <img");
 mlessurlname = re.findall(mregex_geturlname, mrtext);
 mregex_getavatar = re.escape("<img\n    src=\"")+"(.*)"+re.escape("\"\n    class=\"avatar avatar-small\"");
 mlessavatar = re.findall(mregex_getavatar, mrtext);
 if(getlinks[1]>len(mlesslinkone) or getlinks[1]==-1):
  getlinks[1] = len(mlesslinkone);
 if(getlinks[0]>getlinks[1] and not getlinks[1]==-1):
  tmpgetlinks0 = getlinks[0];
  tmpgetlinks1 = getlinks[1];
  getlinks[0] = tmpgetlinks1;
  getlinks[1] = tmpgetlinks0;
 if(getlinks[0]<0):
  getlinks[0] = 0;
 mli = getlinks[0];
 mlil = getlinks[1];
 returnval = {'numoflinks': mlil};
 returnval.update({'numofalllinks': len(mlessuname)});
 returnval.update({'pages': lastpage});
 returnval.update({'curpage': page});
 returnval.update({'orginurl': httpurl});
 returnval.update({'orginurltype': get_motherless_get_link_type(httpurl)});
 mlessrooturltype = get_motherless_get_link_type(httpurl);
 returnval.update({'urltype': mlessrooturltype});
 while(mli<mlil):
  avatarfilenameext = os.path.basename(urlparse.urljoin(mlessavatar[mli], urlparse.urlparse(mlessavatar[mli]).path));
  avatarfilename, avatarfileextension = os.path.splitext(avatarfilenameext);
  mlessurltype = get_motherless_get_link_type("http://motherless.com/"+mlessurlname[mli]);
  returnval.update({mli: {'urltype': mlessurltype, 'url': "http://motherless.com/"+mlessurlname[mli], 'username': mlessuname[mli], 'avatarurl': mlessavatar[mli], 'avatarfullfilename': avatarfilenameext, 'avatarfilename': avatarfilename, 'avatarextension': avatarfileextension} });
  mli = mli + 1;
 return returnval;

def get_motherless_girls(httpheaders, httpcookie, getlinks=[0, -1]):
 mrtext = download_from_url("http://motherless.com/girls", httpheaders, httpcookie);
 mregex_getuname = re.escape("<a href=\"")+"(.*)"+re.escape("\" rev=\"")+"([\w\/\?\&\=\.\-]+)"+re.escape("\" rel=\"")+"(.*)"+re.escape("\">");
 mlessuname = re.findall(mregex_getuname, mrtext);
 mregex_geturlname = re.escape("\n\t\t\t\t\t\t<a href=\"/m/")+"([\w\/\?\&\=\.\-]+)"+re.escape("\" target=\"_blank\">");
 mlessurlname = re.findall(mregex_geturlname, mrtext);
 if(getlinks[1]>len(mlesslinkone) or getlinks[1]==-1):
  getlinks[1] = len(mlesslinkone);
 if(getlinks[0]>getlinks[1] and not getlinks[1]==-1):
  tmpgetlinks0 = getlinks[0];
  tmpgetlinks1 = getlinks[1];
  getlinks[0] = tmpgetlinks1;
  getlinks[1] = tmpgetlinks0;
 if(getlinks[0]<0):
  getlinks[0] = 0;
 mli = getlinks[0];
 mlil = getlinks[1];
 returnval = {'numoflinks': mlil};
 returnval.update({'numofalllinks': len(mlessuname)});
 returnval.update({'orginurl': "http://motherless.com/girls"});
 returnval.update({'orginurltype': get_motherless_get_link_type("http://motherless.com/girls")});
 mlessrooturltype = get_motherless_get_link_type("http://motherless.com/girls");
 returnval.update({'urltype': mlessrooturltype});
 while(mli<mlil):
  avatarfilenameext = os.path.basename(urlparse.urljoin(mlessuname[mli][0], urlparse.urlparse(mlessuname[mli][0]).path));
  avatarfilename, avatarfileextension = os.path.splitext(avatarfilenameext);
  mlessurltype = get_motherless_get_link_type("http://motherless.com/"+mlessuname[mli][1]);
  returnval.update({mli: {'urltype': mlessurltype, 'url': "http://motherless.com/"+mlessuname[mli][1], 'username': mlessuname[mli][1], 'usernamealt': mlessuname[mli][2], 'avatarurl': mlessuname[mli][0], 'avatarfullfilename': avatarfilenameext, 'avatarfilename': avatarfilename, 'avatarextension': avatarfileextension} });
  mli = mli + 1;
 return returnval;

def get_motherless_sample_links(httpheaders, httpcookie, numoflinks=10, urltype="video"):
 if(urltype=="video"):
  returnval = {'numoflinks': numoflinks, 'orginurl': "http://motherless.com/videos", 'orginurltype': get_motherless_get_link_type("http://motherless.com/videos"), 'videos': {'recent': get_motherless_galleries_links("http://motherless.com/videos/recent", httpheaders, httpcookie, 1, [0, numoflinks]), 'favorited': get_motherless_galleries_links("http://motherless.com/videos/favorited", httpheaders, httpcookie, 1, [0, numoflinks]), 'viewed': get_motherless_galleries_links("http://motherless.com/videos/viewed", httpheaders, httpcookie, 1, [0, numoflinks]), 'commented': get_motherless_galleries_links("http://motherless.com/videos/commented", httpheaders, httpcookie, 1, [0, numoflinks]), 'popular': get_motherless_galleries_links("http://motherless.com/videos/popular", httpheaders, httpcookie, 1, [0, numoflinks]), 'live': get_motherless_galleries_links("http://motherless.com/live/videos", httpheaders, httpcookie, 1, [0, numoflinks]), 'random': get_motherless_random_links(httpheaders, httpcookie, "video", [0, numoflinks])} };
 if(urltype=="image"):
  returnval = {'numoflinks': numoflinks, 'orginurl': "http://motherless.com/images", 'orginurltype': get_motherless_get_link_type("http://motherless.com/images"), 'images': {'recent': get_motherless_galleries_links("http://motherless.com/images/recent", httpheaders, httpcookie, 1, [0, numoflinks]), 'favorited': get_motherless_galleries_links("http://motherless.com/images/favorited", httpheaders, httpcookie, 1, [0, numoflinks]), 'viewed': get_motherless_galleries_links("http://motherless.com/images/viewed", httpheaders, httpcookie, 1, [0, numoflinks]), 'commented': get_motherless_galleries_links("http://motherless.com/images/commented", httpheaders, httpcookie, 1, [0, numoflinks]), 'popular': get_motherless_galleries_links("http://motherless.com/images/popular", httpheaders, httpcookie, 1, [0, numoflinks]), 'live': get_motherless_galleries_links("http://motherless.com/live/images", httpheaders, httpcookie, 1, [0, numoflinks]), 'random': get_motherless_random_links(httpheaders, httpcookie, "image", [0, numoflinks])} };
 if(urltype=="gallery"):
  returnval = {'numoflinks': numoflinks, 'orginurl': "http://motherless.com/galleries", 'orginurltype': get_motherless_get_link_type("http://motherless.com/galleries"), 'galleries': {'updated': get_motherless_galleries_links("http://motherless.com/galleries/updated", httpheaders, httpcookie, 1, [0, numoflinks]), 'created': get_motherless_galleries_links("http://motherless.com/galleries/created", httpheaders, httpcookie, 1, [0, numoflinks]), 'viewed': get_motherless_galleries_links("http://motherless.com/galleries/viewed", httpheaders, httpcookie, 1, [0, numoflinks]), 'favorited': get_motherless_galleries_links("http://motherless.com/galleries/favorited", httpheaders, httpcookie, 1, [0, numoflinks]), 'commented': get_motherless_galleries_links("http://motherless.com/galleries/commented", httpheaders, httpcookie, 1, [0, numoflinks])} };
 if(urltype=="all"):
  returnval = {'numoflinks': numoflinks, 'orginurl': "http://motherless.com/", 'orginurltype': get_motherless_get_link_type("http://motherless.com/"), 'videos': {'recent': get_motherless_galleries_links("http://motherless.com/videos/recent", httpheaders, httpcookie, 1, [0, numoflinks]), 'favorited': get_motherless_galleries_links("http://motherless.com/videos/favorited", httpheaders, httpcookie, 1, [0, numoflinks]), 'viewed': get_motherless_galleries_links("http://motherless.com/videos/viewed", httpheaders, httpcookie, 1, [0, numoflinks]), 'commented': get_motherless_galleries_links("http://motherless.com/videos/commented", httpheaders, httpcookie, 1, [0, numoflinks]), 'popular': get_motherless_galleries_links("http://motherless.com/videos/popular", httpheaders, httpcookie, 1, [0, numoflinks]), 'live': get_motherless_galleries_links("http://motherless.com/live/videos", httpheaders, httpcookie, 1, [0, numoflinks]), 'random': get_motherless_random_links(httpheaders, httpcookie, "video", [0, numoflinks])}, 'images': {'recent': get_motherless_galleries_links("http://motherless.com/images/recent", httpheaders, httpcookie, 1, [0, numoflinks]), 'favorited': get_motherless_galleries_links("http://motherless.com/images/favorited", httpheaders, httpcookie, 1, [0, numoflinks]), 'viewed': get_motherless_galleries_links("http://motherless.com/images/viewed", httpheaders, httpcookie, 1, [0, numoflinks]), 'commented': get_motherless_galleries_links("http://motherless.com/images/commented", httpheaders, httpcookie, 1, [0, numoflinks]), 'popular': get_motherless_galleries_links("http://motherless.com/images/popular", httpheaders, httpcookie, 1, [0, numoflinks]), 'live': get_motherless_galleries_links("http://motherless.com/live/images", httpheaders, httpcookie, 1, [0, numoflinks]), 'random': get_motherless_random_links(httpheaders, httpcookie, "image", [0, numoflinks])}, 'galleries': {'updated': get_motherless_galleries_links("http://motherless.com/galleries/updated", httpheaders, httpcookie, 1, [0, numoflinks]), 'created': get_motherless_galleries_links("http://motherless.com/galleries/created", httpheaders, httpcookie, 1, [0, numoflinks]), 'viewed': get_motherless_galleries_links("http://motherless.com/galleries/viewed", httpheaders, httpcookie, 1, [0, numoflinks]), 'favorited': get_motherless_galleries_links("http://motherless.com/galleries/favorited", httpheaders, httpcookie, 1, [0, numoflinks]), 'commented': get_motherless_galleries_links("http://motherless.com/galleries/commented", httpheaders, httpcookie, 1, [0, numoflinks])} };
 return returnval;

def get_motherless_get_link_by_type(httpurl, httpheaders, httpcookie, page=1, getlinks=[0, -1]):
 returnval = False;
 if(get_motherless_get_link_type(httpurl)=="file"):
  returnval = get_motherless_links(httpurl, httpheaders, httpcookie);
 if(get_motherless_get_link_type(httpurl)=="gallery"):
  returnval = get_motherless_galleries_links(httpurl, httpheaders, httpcookie, page);
 if(get_motherless_get_link_type(httpurl)=="sample-videos"):
  returnval = get_motherless_sample_links(httpheaders, httpcookie, 10, "video");
 if(get_motherless_get_link_type(httpurl)=="sample-images"):
  returnval = get_motherless_sample_links(httpheaders, httpcookie, 10, "image");
 if(get_motherless_get_link_type(httpurl)=="sample-galleries"):
  returnval = get_motherless_sample_links(httpheaders, httpcookie, 10, "gallery");
 if(get_motherless_get_link_type(httpurl)=="sample"):
  returnval = get_motherless_sample_links(httpheaders, httpcookie, 10, "all");
 if(get_motherless_get_link_type(httpurl)=="board"):
  returnval = get_motherless_boards_links(httpurl, httpheaders, httpcookie);
 if(get_motherless_get_link_type(httpurl)=="member"):
  returnval = get_motherless_search_members(httpurl, httpheaders, httpcookie, page);
 if(get_motherless_get_link_type(httpurl)=="girls"):
  returnval = get_motherless_girls(httpheaders, httpcookie);
 if(get_motherless_get_link_type(httpurl)=="download"):
  returnval = httpurl;
 return returnval;

def view_motherless_links(httpurl, httpheaders, httpcookie, viewerpro, prearg=[], proarg=[]):
 commandlist = [viewerpro] + prearg;
 commandlist = commandlist + [get_motherless_links(httpurl, httpheaders, httpcookie)['url']];
 commandlist = commandlist + proarg;
 mpvplaylistp = subprocess.Popen(commandlist, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
 mpvplayout, mpvplayerr = mpvplaylistp.communicate();
 return True;

def download_motherless_links(httpurl, httpheaders, httpcookie, sleep=-1, outfile="-", outpath=os.getcwd(), usetitlename=False):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 mlessurl = get_motherless_links(httpurl, httpheaders, httpcookie);
 outputname = mlessurl['fullfilename'];
 outpath = outpath.rstrip(os.path.sep);
 if(usetitlename==True):
  outputname = mlessurl['title'];
 if(usetitlename=="-" and outfile=="-"):
  outputname = "-";
 if(usetitlename=="-" and not outfile=="-"):
  outputname = outfile;
 returnval = download_from_url_to_file(mlessurl['url'], httpheaders, httpcookie, outputname, outpath, sleep);
 return returnval;

def download_motherless_links_by_type(httpurl, httpheaders, httpcookie, sleep=-1, outfile="-", outpath=os.getcwd(), usetitlename=False, page=1, getlinks=[0, -1]):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 mlessurl = get_motherless_get_link_by_type(httpurl, httpheaders, httpcookie, page);
 if(mlessurl['urltype']=="download"):
  outputname = mlessurl['fullfilename'];
  outpathname = outpath.rstrip(os.path.sep);
  if(usetitlename==True):
   outputname = mlessurl['title'];
  if(usetitlename=="-" and outfile[mli]=="-"):
   outputname = "-";
  if(usetitlename=="-" and not outfile[mli]=="-"):
   outputname = outfile;
  returnval = download_from_url_to_file(mlessurl['url'], httpheaders, httpcookie, outputname, outpathname, sleep);
 if(not mlessurl['urltype']=="download"):
  returnval = mlessurl;
 return returnval;

def download_motherless_galleries_links(httpurl, httpheaders, httpcookie, sleep=-1, outfile="-", outpath=os.getcwd(), usetitlename=False, page=1, getlinks=[0, -1]):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 mlessgalleries = get_motherless_galleries_links(httpurl, httpheaders, httpcookie, page, getlinks);
 mli = 0;
 mlil = mlessgalleries['numoflinks'];
 returnval = {'pages': mlessgalleries['pages']};
 returnval.update({'numoflists': mlessgalleries['numoflinks']});
 returnval.update({'curpage': mlessgalleries['curpage']});
 returnval.update({'numoflinks': mlessgalleries['numoflinks']});
 returnval.update({'numofalllinks': mlessgalleries['numofalllinks']});
 returnval.update({'orginurl': httpurl});
 returnval.update({'orginurltype': get_motherless_get_link_type(httpurl)});
 while(mli<mlil):
  mlesslink = get_motherless_links(mlessgalleries[mli]['url'], httpheaders, httpcookie);
  outputname = mlesslink['fullfilename'];
  outpath = outpath.rstrip(os.path.sep);
  if(usetitlename==True):
   outputname = mlesslink['title'];
  if(usetitlename=="-" and outfile=="-"):
   outputname = "-";
  if(usetitlename=="-" and not outfile=="-"):
   outputname = outfile;
  returnval.update({mli: {'download': download_from_url_to_file(mlesslink['url'], httpheaders, httpcookie, outputname, outpath, sleep), 'linkinfo': mlesslink} });
  mli = mli + 1;
 return returnval;

def download_get_motherless_boards_links(httpurl, httpheaders, httpcookie, sleep=-1, outfile="-", outpath=os.getcwd(), usetitlename=False, getlinks=[0, -1]):
 global geturls_download_sleep;
 if(sleep<0):
  sleep = geturls_download_sleep;
 mlessgalleries = get_motherless_boards_links(httpurl, httpheaders, httpcookie, getlinks);
 mli = 0;
 mlil = mlessgalleries['numoflinks'];
 returnval = {'numoflists': mlessgalleries['numoflinks']};
 returnval.update({'numofalllinks': mlessgalleries['numofalllinks']});
 returnval.update({'orginurl': httpurl});
 returnval.update({'orginurltype': get_motherless_get_link_type(httpurl)});
 while(mli<mlil):
  mlesslink = get_motherless_links(mlessgalleries[mli]['url'], httpheaders, httpcookie);
  outputname = mlesslink['fullfilename'];
  outpath = outpath.rstrip(os.path.sep);
  if(usetitlename==True):
   outputname = mlesslink['title'];
  if(usetitlename=="-" and outfile=="-"):
   outputname = "-";
  if(usetitlename=="-" and not outfile=="-"):
   outputname = outfile;
  returnval.update({mli: {'download': download_from_url_to_file(mlesslink['url'], httpheaders, httpcookie, outputname, outpath, sleep), 'linkinfo': mlesslink} });
  mli = mli + 1;
 return returnval;
