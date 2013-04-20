#!/usr/bin/python
# -*- coding: utf-8 -*- 
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

    $FileInfo: cyrpol.py - Last Update: 04/20/2013 Ver. 1.0.0  - Author: cooldude2k $
'''
import re, sys

'''
A Cyrillic orthography for the Polish language
http://steen.free.fr/cyrpol/
© Jan van Steenbergen, September 2008
'''
fcry = open(sys.argv[1], "rb");
fcryexp = fcry.readlines();
fcry.close();
fcryi = 0;
fcrynum = len(fcryexp);
if(len(sys.argv)>=3):
 fout = open(sys.argv[2], "w+b");
while(fcryi<fcrynum):
 iW = fcryexp[fcryi][:-1].lower();
 iW = re.sub("ó", "u",  iW);
 iW = re.sub("ch", "h",  iW);
 iW = re.sub("j", "jj",  iW);
 iW = re.sub("rz", "rj", iW);
 iW = re.sub("cz", "čJ", iW);
 iW = re.sub("sz", "šJ", iW);
 iW = re.sub("ż", "žJ", iW);
 iW = re.sub("ci", "ti", iW);
 iW = re.sub("dzi", "di", iW);
 iW = re.sub("l", "lj", iW);
 iW = re.sub("lji", "li", iW);
 iW = re.sub("ł", "l", iW);
 iW = re.sub("ć", "tj", iW);
 iW = re.sub("dź", "dj", iW);
 iW = re.sub("ś", "sj", iW);
 iW = re.sub("ź", "zj", iW);
 iW = re.sub("ń", "nj", iW);
 iW = re.sub("w", "v", iW);
 iW = re.sub("q", "k", iW);
 iW = re.sub("x", "ks", iW);
 iW = re.sub("ia", "ja", iW);
 iW = re.sub("ie", "je", iW);
 iW = re.sub("io", "jo", iW);
 iW = re.sub("iu", "ju", iW);
 iW = re.sub("ią", "ją", iW);
 iW = re.sub("ię", "ję", iW);
 iW = re.sub("i", "ji", iW);
 iW = re.sub("ljlj", "llj", iW);
 iW = re.sub("sjtj", "stj", iW);
 iW = re.sub("zjdj", "zdj", iW);
 iW = re.sub("sjpj", "spj", iW);
 iW = re.sub("zjbj", "zbj", iW);
 iW = re.sub("sjnj", "snj", iW);
 iW = re.sub("zjnj", "znj", iW);
 iW = re.sub("sjmj", "smj", iW);
 iW = re.sub("zjmj", "zmj", iW);
 iW = re.sub("tjvj", "tvj", iW);
 iW = re.sub("djvj", "dvj", iW);
 iW = re.sub("sjvj", "svj", iW);
 iW = re.sub("zjvj", "zvj", iW);
 iW = re.sub("sjlj", "slj", iW);
 iW = re.sub("zjlj", "zlj", iW);
 iW = re.sub("sjr", "srj", iW);
 iW = re.sub("zjr", "zrj", iW);
 iW = re.sub("ji", "i", iW);
 iW = re.sub("jy", "i", iW);
 iW = re.sub("Ji", "ji", iW);
 iW = re.sub("Jy", "i", iW);
 iW = re.sub("Je", "je", iW);
 iW = re.sub("J", "", iW);
 iW = re.sub("ja", "JяV", iW);
 iW = re.sub("je", "JеV", iW);
 iW = re.sub("i", "JиV", iW);
 iW = re.sub("jo", "JëV", iW);
 iW = re.sub("ju", "JюV", iW);
 iW = re.sub("ją", "Jя̨V", iW);
 iW = re.sub("ję", "Jе̨V", iW);
 iW = re.sub("a", "аV", iW);
 iW = re.sub("e", "эV", iW);
 iW = re.sub("y", "ыV", iW);
 iW = re.sub("o", "оV", iW);
 iW = re.sub("u", "уV", iW);
 iW = re.sub("ą", "а̨V", iW);
 iW = re.sub("ę", "э̨V", iW);
 iW = re.sub("Vjj", "й", iW);
 iW = re.sub("%jJ", "%", iW);
 iW = re.sub("VjJ", "", iW);
 iW = re.sub("jJ", "ъ", iW);
 iW = re.sub("J", "", iW);
 iW = re.sub("V", "", iW);
 iW = re.sub("j", "ь", iW);
 iW = re.sub("p", "п", iW);
 iW = re.sub("b", "б", iW);
 iW = re.sub("f", "ф", iW);
 iW = re.sub("v", "в", iW);
 iW = re.sub("t", "т", iW);
 iW = re.sub("d", "д", iW);
 iW = re.sub("s", "с", iW);
 iW = re.sub("z", "з", iW);
 iW = re.sub("k", "к", iW);
 iW = re.sub("g", "г", iW);
 iW = re.sub("h", "х", iW);
 iW = re.sub("m", "м", iW);
 iW = re.sub("n", "н", iW);
 iW = re.sub("l", "л", iW);
 iW = re.sub("r", "р", iW);
 iW = re.sub("šč", "щ", iW);
 iW = re.sub("č", "ч", iW);
 iW = re.sub("š", "ш", iW);
 iW = re.sub("ž", "ж", iW);
 iW = re.sub("c", "ц", iW);
 iW = re.sub("цъ", "ц", iW);
 iW = re.sub("цьъ", "ц", iW);
 if(len(sys.argv)<3):
  print(iW.capitalize());
 if(len(sys.argv)>=3):
  fout.write(iW.capitalize()+"\n");
 fcryi = fcryi + 1;
if(len(sys.argv)>=3):
 fout.close();
