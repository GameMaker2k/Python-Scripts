#!/usr/bin/python2

import gzip, bz2, binascii, os, re, sys, math, time;

enable_gfxdraw = False;
code_output = "Python";

if(len(sys.argv)>2 and (sys.argv[2]=="C" or sys.argv[2]=="Python" or sys.argv[2]=="Py")):
	code_output = sys.argv[2];

if(len(sys.argv)>3 and sys.argv[3]=="draw"):
	enable_gfxdraw = False;

if(len(sys.argv)>3 and sys.argv[3]=="gfxdraw"):
	enable_gfxdraw = True;

if(code_output=="Python" or code_output=="Py"):
	print "#!/usr/bin/python2\n";
	print "import gzip, bz2, binascii, os, re, sys, math, time, pygame, pygame.draw, pygame.gfxdraw;";
	print "from pygame.locals import *;\n";
	print "pygame.init();";
	print "pygame.display.init();";
	print "tstart = time.clock();";
	print "pyicon = pygame.image.load(\"./icon.png\");";
	print "pygame.display.set_icon(pyicon);";
	print "ds_screen = pygame.display.set_mode((256, 384), pygame.HWSURFACE | pygame.DOUBLEBUF);";
	print "pygame.display.set_caption(\"Petit Computer\");";
	print "ds_screen.fill((0, 0, 0));";
	print "pygame.display.update();\n";
	print "ds_top_screen = pygame.Surface((256, 192));";
	print "ds_top_screen.fill((0, 0, 0));";
	print "ds_bottom_screen = pygame.Surface((256, 192));";
	print "ds_bottom_screen.fill((0, 0, 0));";
	print "draw_screen = ds_top_screen;";
	print "ptgcolor = 0;";
	print "done = False;\n";
	print "# We need this if we want to be able to specify our";
	print "#  arc in degrees instead of radians";
	print "def degreesToRadians(deg):";
	print "	return deg / 180.0 * math.pi;\n";
	print "# Draw an arc that is a portion of a circle.";
	print "# We pass in screen and color,";
	print "# followed by a tuple (x,y) that is the center of the circle, and the radius.";
	print "# Next comes the start and ending angle on the \"unit circle\" (0 to 360)";
	print "#  of the circle we want to draw, and finally the thickness in pixels";
	print "def drawCircleArc(screen, color, center, radius, startDeg, endDeg, thickness):";
	print "	(x, y) = center;";
	print "	rect = (x - radius, y - radius, radius * 2, radius * 2);";
	print "	startRad = degreesToRadians(startDeg);";
	print "	endRad = degreesToRadians(endDeg);";
	print "	pygame.draw.arc(screen, color, rect, startRad, endRad, thickness);\n";

if(code_output=="C"):
	print "#include \"stdio.h\"";
	print "#include \"stdbool.h\"";
	print "#include \"SDL.h\"\n";
	print "#include \"SDL_gfxPrimitives.h\"\n";
	print "int main ( int argc, char *argv[] )\n{";
	print "  bool done;";
	print "  SDL_Event event;";
	print "  SDL_Surface* ds_screen;";
	print "  SDL_Surface* ds_top_screen;";
	print "  SDL_Surface* ds_bottom_screen;";
	print "  SDL_Rect ds_top_screen_rect;";
	print "  SDL_Rect ds_bottom_screen_rect;\n";
	print "  ds_top_screen_rect.x = 0;";
	print "  ds_top_screen_rect.y = 0;";
	print "  ds_bottom_screen_rect.x = 0;";
	print "  ds_bottom_screen_rect.y = 192;\n";
	print "  SDL_Init(SDL_INIT_VIDEO);";
	print "  SDL_WM_SetCaption(\"Petit Computer\", \"Petit Computer\");";
	print "  ds_screen = SDL_SetVideoMode(256, 384, 0, SDL_HWSURFACE | SDL_DOUBLEBUF);";
	print "  ds_top_screen = SDL_CreateRGBSurface(SDL_HWSURFACE | SDL_DOUBLEBUF, 256, 192, 24, 0, 0, 0, 0);";
	print "  SDL_FillRect(ds_top_screen, NULL, SDL_MapRGB(ds_top_screen->format, 0, 0, 0));";
	print "  SDL_Flip(ds_top_screen);";
	print "  SDL_BlitSurface(ds_top_screen, NULL, ds_screen, &ds_top_screen_rect);";
	print "  ds_bottom_screen = SDL_CreateRGBSurface(SDL_HWSURFACE | SDL_DOUBLEBUF, 256, 192, 24, 0, 0, 0, 0);";
	print "  SDL_FillRect(ds_bottom_screen, NULL, SDL_MapRGB(ds_bottom_screen->format, 0, 0, 0));";
	print "  SDL_Flip(ds_bottom_screen);";
	print "  SDL_BlitSurface(ds_bottom_screen, NULL, ds_screen, &ds_bottom_screen_rect);";
	print "  SDL_Flip(ds_screen);\n";

def SmileBasic_Console_Palette(sb_color):
	if(sb_color==0):
		return (0, 0, 0);
	if(sb_color==1):
		return (57, 56, 57);
	if(sb_color==2):
		return (255, 24, 0);
	if(sb_color==3):
		return (255, 89, 198);
	if(sb_color==4):
		return (0, 56, 247);
	if(sb_color==5):
		return (123, 56, 255);
	if(sb_color==6):
		return (0, 186, 255);
	if(sb_color==7):
		return (148, 89, 41);
	if(sb_color==8):
		return (255, 162, 0);
	if(sb_color==9):
		return (255, 203, 165);
	if(sb_color==10):
		return (0, 121, 0);
	if(sb_color==11):
		return (0, 243, 24);
	if(sb_color==12):
		return (255, 227, 0);
	if(sb_color==13):
		return (189, 186, 189);
	if(sb_color==14):
		return (0, 0, 0);
	if(sb_color==15):
		return (255, 251, 255);
	if(sb_color==16):
		return (0, 0, 0);
	if(sb_color==17):
		return (41, 40, 41);
	if(sb_color==18):
		return (140, 48, 41);
	if(sb_color==19):
		return (156, 89, 132);
	if(sb_color==20):
		return (33, 56, 132);
	if(sb_color==21):
		return (99, 73, 148);
	if(sb_color==22):
		return (41, 113, 140);
	if(sb_color==23):
		return (90, 65, 49);
	if(sb_color==24):
		return (140, 97, 41);
	if(sb_color==25):
		return (165, 146, 132);
	if(sb_color==26):
		return (16, 65, 16);
	if(sb_color==27):
		return (33, 130, 49);
	if(sb_color==28):
		return (140, 121, 41);
	if(sb_color==29):
		return (132, 130, 132);
	if(sb_color==30):
		return (255, 251, 255);
	if(sb_color==31):
		return (0, 0, 0);
	if(sb_color==32):
		return (0, 0, 0);
	if(sb_color==33):
		return (16, 48, 82);
	if(sb_color==34):
		return (66, 97, 255);
	if(sb_color==35):
		return (181, 211, 255);
	if(sb_color==36):
		return (173, 0, 0);
	if(sb_color==37):
		return (255, 65, 16);
	if(sb_color==38):
		return (255, 195, 189);
	if(sb_color==39):
		return (115, 73, 24);
	if(sb_color==40):
		return (206, 178, 123);
	if(sb_color==41):
		return (255, 227, 181);
	if(sb_color==42):
		return (66, 65, 66);
	if(sb_color==43):
		return (148, 146, 148);
	if(sb_color==44):
		return (231, 227, 231);
	if(sb_color==45):
		return (255, 251, 255);
	if(sb_color==46):
		return (0, 0, 0);
	if(sb_color==47):
		return (189, 186, 189);
	if(sb_color==48):
		return (0, 0, 0);
	if(sb_color==49):
		return (82, 0, 0);
	if(sb_color==50):
		return (181, 24, 0);
	if(sb_color==51):
		return (255, 97, 82);
	if(sb_color==52):
		return (74, 65, 16);
	if(sb_color==53):
		return (123, 97, 49);
	if(sb_color==54):
		return (198, 162, 99);
	if(sb_color==55):
		return (115, 105, 0);
	if(sb_color==56):
		return (189, 178, 0);
	if(sb_color==57):
		return (255, 251, 0);
	if(sb_color==58):
		return (90, 56, 255);
	if(sb_color==59):
		return (148, 130, 255);
	if(sb_color==60):
		return (222, 211, 255);
	if(sb_color==61):
		return (255, 251, 255);
	if(sb_color==62):
		return (0, 0, 0);
	if(sb_color==63):
		return (255, 227, 0);
	if(sb_color==64):
		return (0, 0, 0);
	if(sb_color==65):
		return (123, 0, 0);
	if(sb_color==66):
		return (255, 40, 24);
	if(sb_color==67):
		return (255, 146, 107);
	if(sb_color==68):
		return (0, 73, 255);
	if(sb_color==69):
		return (0, 178, 255);
	if(sb_color==70):
		return (82, 251, 255);
	if(sb_color==71):
		return (140, 73, 0);
	if(sb_color==72):
		return (198, 154, 90);
	if(sb_color==73):
		return (255, 203, 123);
	if(sb_color==74):
		return (0, 113, 0);
	if(sb_color==75):
		return (0, 227, 0);
	if(sb_color==76):
		return (156, 251, 156);
	if(sb_color==77):
		return (255, 251, 255);
	if(sb_color==78):
		return (0, 0, 0);
	if(sb_color==79):
		return (0, 243, 24);
	if(sb_color==80):
		return (0, 0, 0);
	if(sb_color==81):
		return (0, 73, 165);
	if(sb_color==82):
		return (107, 130, 255);
	if(sb_color==83):
		return (181, 211, 255);
	if(sb_color==84):
		return (33, 73, 8);
	if(sb_color==85):
		return (33, 146, 0);
	if(sb_color==86):
		return (16, 243, 0);
	if(sb_color==87):
		return (140, 97, 49);
	if(sb_color==88):
		return (189, 170, 82);
	if(sb_color==89):
		return (239, 227, 156);
	if(sb_color==90):
		return (148, 32, 0);
	if(sb_color==91):
		return (222, 65, 0);
	if(sb_color==92):
		return (255, 130, 74);
	if(sb_color==93):
		return (255, 251, 255);
	if(sb_color==94):
		return (0, 0, 0);
	if(sb_color==95):
		return (0, 121, 0);
	if(sb_color==96):
		return (0, 0, 0);
	if(sb_color==97):
		return (99, 81, 0);
	if(sb_color==98):
		return (255, 251, 0);
	if(sb_color==99):
		return (255, 251, 156);
	if(sb_color==100):
		return (156, 0, 66);
	if(sb_color==101):
		return (255, 0, 132);
	if(sb_color==102):
		return (255, 178, 214);
	if(sb_color==103):
		return (148, 97, 24);
	if(sb_color==104):
		return (214, 195, 123);
	if(sb_color==105):
		return (255, 251, 239);
	if(sb_color==106):
		return (33, 178, 0);
	if(sb_color==107):
		return (99, 251, 74);
	if(sb_color==108):
		return (206, 251, 189);
	if(sb_color==109):
		return (255, 251, 255);
	if(sb_color==110):
		return (0, 0, 0);
	if(sb_color==111):
		return (255, 203, 165);
	if(sb_color==112):
		return (0, 0, 0);
	if(sb_color==113):
		return (99, 0, 107);
	if(sb_color==114):
		return (255, 0, 255);
	if(sb_color==115):
		return (255, 113, 255);
	if(sb_color==116):
		return (74, 73, 0);
	if(sb_color==117):
		return (189, 178, 16);
	if(sb_color==118):
		return (255, 251, 0);
	if(sb_color==119):
		return (181, 97, 24);
	if(sb_color==120):
		return (247, 195, 123);
	if(sb_color==121):
		return (255, 251, 239);
	if(sb_color==122):
		return (66, 65, 255);
	if(sb_color==123):
		return (132, 130, 255);
	if(sb_color==124):
		return (222, 219, 255);
	if(sb_color==125):
		return (255, 251, 255);
	if(sb_color==126):
		return (0, 0, 0);
	if(sb_color==127):
		return (255, 162, 0);
	if(sb_color==128):
		return (0, 0, 0);
	if(sb_color==129):
		return (74, 32, 8);
	if(sb_color==130):
		return (99, 56, 16);
	if(sb_color==131):
		return (123, 65, 24);
	if(sb_color==132):
		return (148, 89, 41);
	if(sb_color==133):
		return (181, 121, 66);
	if(sb_color==134):
		return (206, 170, 115);
	if(sb_color==135):
		return (33, 113, 0);
	if(sb_color==136):
		return (16, 162, 16);
	if(sb_color==137):
		return (74, 211, 90);
	if(sb_color==138):
		return (148, 138, 231);
	if(sb_color==139):
		return (189, 178, 239);
	if(sb_color==140):
		return (222, 211, 255);
	if(sb_color==141):
		return (255, 251, 255);
	if(sb_color==142):
		return (0, 0, 0);
	if(sb_color==143):
		return (148, 89, 41);
	if(sb_color==144):
		return (0, 0, 0);
	if(sb_color==145):
		return (33, 0, 0);
	if(sb_color==146):
		return (66, 24, 0);
	if(sb_color==147):
		return (123, 56, 0);
	if(sb_color==148):
		return (132, 73, 33);
	if(sb_color==149):
		return (148, 97, 41);
	if(sb_color==150):
		return (165, 121, 74);
	if(sb_color==151):
		return (0, 48, 0);
	if(sb_color==152):
		return (0, 97, 24);
	if(sb_color==153):
		return (33, 154, 66);
	if(sb_color==154):
		return (99, 65, 181);
	if(sb_color==155):
		return (165, 138, 214);
	if(sb_color==156):
		return (198, 178, 247);
	if(sb_color==157):
		return (181, 219, 255);
	if(sb_color==158):
		return (0, 0, 0);
	if(sb_color==159):
		return (0, 186, 255);
	if(sb_color==160):
		return (0, 0, 0);
	if(sb_color==161):
		return (0, 32, 0);
	if(sb_color==162):
		return (41, 81, 41);
	if(sb_color==163):
		return (90, 121, 90);
	if(sb_color==164):
		return (132, 170, 132);
	if(sb_color==165):
		return (181, 211, 181);
	if(sb_color==166):
		return (231, 251, 231);
	if(sb_color==167):
		return (132, 89, 0);
	if(sb_color==168):
		return (173, 146, 49);
	if(sb_color==169):
		return (214, 203, 148);
	if(sb_color==170):
		return (132, 105, 0);
	if(sb_color==171):
		return (255, 251, 0);
	if(sb_color==172):
		return (255, 251, 214);
	if(sb_color==173):
		return (255, 251, 255);
	if(sb_color==174):
		return (0, 0, 0);
	if(sb_color==175):
		return (123, 56, 255);
	if(sb_color==176):
		return (0, 0, 0);
	if(sb_color==177):
		return (57, 56, 57);
	if(sb_color==178):
		return (82, 81, 90);
	if(sb_color==179):
		return (123, 121, 132);
	if(sb_color==180):
		return (156, 162, 173);
	if(sb_color==181):
		return (181, 186, 198);
	if(sb_color==182):
		return (206, 211, 231);
	if(sb_color==183):
		return (222, 121, 0);
	if(sb_color==184):
		return (255, 195, 16);
	if(sb_color==185):
		return (255, 251, 90);
	if(sb_color==186):
		return (231, 24, 0);
	if(sb_color==187):
		return (255, 97, 57);
	if(sb_color==188):
		return (255, 154, 156);
	if(sb_color==189):
		return (255, 251, 255);
	if(sb_color==190):
		return (0, 0, 0);
	if(sb_color==191):
		return (0, 56, 247);
	if(sb_color==192):
		return (0, 0, 0);
	if(sb_color==193):
		return (0, 32, 132);
	if(sb_color==194):
		return (16, 48, 148);
	if(sb_color==195):
		return (57, 81, 165);
	if(sb_color==196):
		return (115, 138, 198);
	if(sb_color==197):
		return (173, 186, 231);
	if(sb_color==198):
		return (222, 227, 255);
	if(sb_color==199):
		return (8, 32, 57);
	if(sb_color==200):
		return (99, 113, 156);
	if(sb_color==201):
		return (181, 203, 255);
	if(sb_color==202):
		return (132, 8, 0);
	if(sb_color==203):
		return (255, 32, 0);
	if(sb_color==204):
		return (255, 211, 173);
	if(sb_color==205):
		return (255, 251, 255);
	if(sb_color==206):
		return (0, 0, 0);
	if(sb_color==207):
		return (255, 89, 198);
	if(sb_color==208):
		return (0, 0, 0);
	if(sb_color==209):
		return (148, 40, 0);
	if(sb_color==210):
		return (156, 56, 24);
	if(sb_color==211):
		return (173, 81, 49);
	if(sb_color==212):
		return (193, 113, 99);
	if(sb_color==213):
		return (239, 178, 165);
	if(sb_color==214):
		return (255, 211, 206);
	if(sb_color==215):
		return (57, 32, 8);
	if(sb_color==216):
		return (156, 113, 99);
	if(sb_color==217):
		return (255, 203, 181);
	if(sb_color==218):
		return (0, 8, 156);
	if(sb_color==219):
		return (0, 130, 255);
	if(sb_color==220):
		return (173, 211, 255);
	if(sb_color==221):
		return (255, 251, 255);
	if(sb_color==222):
		return (0, 0, 0);
	if(sb_color==223):
		return (255, 24, 0);
	if(sb_color==224):
		return (0, 0, 0);
	if(sb_color==225):
		return (41, 48, 0);
	if(sb_color==226):
		return (82, 89, 24);
	if(sb_color==227):
		return (115, 113, 49);
	if(sb_color==228):
		return (156, 154, 74);
	if(sb_color==229):
		return (198, 195, 107);
	if(sb_color==230):
		return (247, 243, 140);
	if(sb_color==231):
		return (107, 89, 0);
	if(sb_color==232):
		return (165, 113, 0);
	if(sb_color==233):
		return (231, 211, 132);
	if(sb_color==234):
		return (132, 8, 148);
	if(sb_color==235):
		return (255, 32, 173);
	if(sb_color==236):
		return (255, 170, 255);
	if(sb_color==237):
		return (255, 251, 255);
	if(sb_color==238):
		return (0, 0, 0);
	if(sb_color==239):
		return (57, 56, 57);
	if(sb_color==240):
		return (99, 97, 99);
	if(sb_color==241):
		return (123, 121, 123);
	if(sb_color==242):
		return (132, 130, 132);
	if(sb_color==243):
		return (148, 146, 148);
	if(sb_color==244):
		return (156, 154, 156);
	if(sb_color==245):
		return (165, 162, 165);
	if(sb_color==246):
		return (173, 170, 173);
	if(sb_color==247):
		return (189, 186, 189);
	if(sb_color==248):
		return (198, 195, 198);
	if(sb_color==249):
		return (206, 203, 206);
	if(sb_color==250):
		return (214, 211, 214);
	if(sb_color==251):
		return (231, 227, 231);
	if(sb_color==252):
		return (49, 48, 49);
	if(sb_color==253):
		return (181, 178, 181);
	if(sb_color==254):
		return (0, 0, 0);
	if(sb_color==255):
		return (239, 235, 239);
	return (0, 0, 0);

def SmileBasic_Hex_Console_Palette(sb_color):
	return SmileBasic_Console_Palette(int(sb_code, 16));

def SmileBasic_Graphic_Palette(sb_color):
	if(sb_color==0):
		return (0, 0, 0);
	if(sb_color==1):
		return (57, 56, 57);
	if(sb_color==2):
		return (255, 24, 0);
	if(sb_color==3):
		return (255, 89, 198);
	if(sb_color==4):
		return (0, 56, 247);
	if(sb_color==5):
		return (123, 56, 255);
	if(sb_color==6):
		return (0, 186, 255);
	if(sb_color==7):
		return (148, 89, 41);
	if(sb_color==8):
		return (255, 162, 0);
	if(sb_color==9):
		return (255, 203, 165);
	if(sb_color==10):
		return (0, 121, 0);
	if(sb_color==11):
		return (0, 243, 24);
	if(sb_color==12):
		return (255, 227, 0);
	if(sb_color==13):
		return (189, 186, 189);
	if(sb_color==14):
		return (0, 0, 0);
	if(sb_color==15):
		return (255, 251, 255);
	if(sb_color==16):
		return (0, 0, 0);
	if(sb_color==17):
		return (41, 40, 41);
	if(sb_color==18):
		return (140, 48, 41);
	if(sb_color==19):
		return (156, 89, 132);
	if(sb_color==20):
		return (33, 56, 132);
	if(sb_color==21):
		return (99, 73, 148);
	if(sb_color==22):
		return (41, 113, 140);
	if(sb_color==23):
		return (90, 65, 49);
	if(sb_color==24):
		return (140, 97, 41);
	if(sb_color==25):
		return (165, 146, 132);
	if(sb_color==26):
		return (16, 65, 16);
	if(sb_color==27):
		return (33, 130, 49);
	if(sb_color==28):
		return (140, 121, 41);
	if(sb_color==29):
		return (132, 130, 132);
	if(sb_color==30):
		return (255, 251, 255);
	if(sb_color==31):
		return (0, 0, 0);
	if(sb_color==32):
		return (255, 251, 255);
	if(sb_color==33):
		return (255, 251, 206);
	if(sb_color==34):
		return (255, 251, 156);
	if(sb_color==35):
		return (255, 251, 99);
	if(sb_color==36):
		return (255, 251, 49);
	if(sb_color==37):
		return (255, 251, 0);
	if(sb_color==38):
		return (255, 203, 255);
	if(sb_color==39):
		return (255, 203, 206);
	if(sb_color==40):
		return (255, 203, 156);
	if(sb_color==41):
		return (255, 203, 99);
	if(sb_color==42):
		return (255, 203, 49);
	if(sb_color==43):
		return (255, 203, 0);
	if(sb_color==44):
		return (255, 154, 255);
	if(sb_color==45):
		return (255, 154, 206);
	if(sb_color==46):
		return (255, 154, 156);
	if(sb_color==47):
		return (255, 154, 99);
	if(sb_color==48):
		return (255, 154, 49);
	if(sb_color==49):
		return (255, 154, 0);
	if(sb_color==50):
		return (255, 97, 255);
	if(sb_color==51):
		return (255, 97, 206);
	if(sb_color==52):
		return (255, 97, 156);
	if(sb_color==53):
		return (255, 97, 99);
	if(sb_color==54):
		return (255, 97, 49);
	if(sb_color==55):
		return (255, 97, 0);
	if(sb_color==56):
		return (255, 48, 255);
	if(sb_color==57):
		return (255, 48, 206);
	if(sb_color==58):
		return (255, 48, 156);
	if(sb_color==59):
		return (255, 48, 99);
	if(sb_color==60):
		return (255, 48, 49);
	if(sb_color==61):
		return (255, 48, 0);
	if(sb_color==62):
		return (255, 0, 255);
	if(sb_color==63):
		return (255, 0, 206);
	if(sb_color==64):
		return (255, 0, 156);
	if(sb_color==65):
		return (255, 0, 99);
	if(sb_color==66):
		return (255, 0, 49);
	if(sb_color==67):
		return (255, 0, 0);
	if(sb_color==68):
		return (206, 251, 255);
	if(sb_color==69):
		return (206, 251, 206);
	if(sb_color==70):
		return (206, 251, 156);
	if(sb_color==71):
		return (206, 251, 99);
	if(sb_color==72):
		return (206, 251, 49);
	if(sb_color==73):
		return (206, 251, 0);
	if(sb_color==74):
		return (206, 203, 255);
	if(sb_color==75):
		return (206, 203, 206);
	if(sb_color==76):
		return (206, 203, 156);
	if(sb_color==77):
		return (206, 203, 99);
	if(sb_color==78):
		return (206, 203, 49);
	if(sb_color==79):
		return (206, 203, 0);
	if(sb_color==80):
		return (206, 154, 255);
	if(sb_color==81):
		return (206, 154, 206);
	if(sb_color==82):
		return (206, 154, 156);
	if(sb_color==83):
		return (206, 154, 99);
	if(sb_color==84):
		return (206, 154, 49);
	if(sb_color==85):
		return (206, 154, 0);
	if(sb_color==86):
		return (206, 97, 255);
	if(sb_color==87):
		return (206, 97, 206);
	if(sb_color==88):
		return (206, 97, 156);
	if(sb_color==89):
		return (206, 97, 99);
	if(sb_color==90):
		return (206, 97, 49);
	if(sb_color==91):
		return (206, 97, 0);
	if(sb_color==92):
		return (206, 48, 255);
	if(sb_color==93):
		return (206, 48, 206);
	if(sb_color==94):
		return (206, 48, 156);
	if(sb_color==95):
		return (206, 48, 99);
	if(sb_color==96):
		return (206, 48, 49);
	if(sb_color==97):
		return (206, 48, 0);
	if(sb_color==98):
		return (206, 0, 255);
	if(sb_color==99):
		return (206, 0, 206);
	if(sb_color==100):
		return (206, 0, 156);
	if(sb_color==101):
		return (206, 0, 99);
	if(sb_color==102):
		return (206, 0, 49);
	if(sb_color==103):
		return (206, 0, 0);
	if(sb_color==104):
		return (156, 251, 255);
	if(sb_color==105):
		return (156, 251, 206);
	if(sb_color==106):
		return (156, 251, 156);
	if(sb_color==107):
		return (156, 251, 99);
	if(sb_color==108):
		return (156, 251, 49);
	if(sb_color==109):
		return (156, 251, 0);
	if(sb_color==110):
		return (156, 203, 255);
	if(sb_color==111):
		return (156, 203, 206);
	if(sb_color==112):
		return (156, 203, 156);
	if(sb_color==113):
		return (156, 203, 99);
	if(sb_color==114):
		return (156, 203, 49);
	if(sb_color==115):
		return (156, 203, 0);
	if(sb_color==116):
		return (156, 154, 255);
	if(sb_color==117):
		return (156, 154, 206);
	if(sb_color==118):
		return (156, 154, 156);
	if(sb_color==119):
		return (156, 154, 99);
	if(sb_color==120):
		return (156, 154, 49);
	if(sb_color==121):
		return (156, 154, 0);
	if(sb_color==122):
		return (156, 97, 255);
	if(sb_color==123):
		return (156, 97, 206);
	if(sb_color==124):
		return (156, 97, 156);
	if(sb_color==125):
		return (156, 97, 99);
	if(sb_color==126):
		return (156, 97, 49);
	if(sb_color==127):
		return (156, 97, 0);
	if(sb_color==128):
		return (156, 48, 255);
	if(sb_color==129):
		return (156, 48, 206);
	if(sb_color==130):
		return (156, 48, 156);
	if(sb_color==131):
		return (156, 48, 99);
	if(sb_color==132):
		return (156, 48, 49);
	if(sb_color==133):
		return (156, 48, 0);
	if(sb_color==134):
		return (156, 0, 255);
	if(sb_color==135):
		return (156, 0, 206);
	if(sb_color==136):
		return (156, 0, 156);
	if(sb_color==137):
		return (156, 0, 99);
	if(sb_color==138):
		return (156, 0, 49);
	if(sb_color==139):
		return (156, 0, 0);
	if(sb_color==140):
		return (99, 251, 255);
	if(sb_color==141):
		return (99, 251, 206);
	if(sb_color==142):
		return (99, 251, 156);
	if(sb_color==143):
		return (99, 251, 99);
	if(sb_color==144):
		return (99, 251, 49);
	if(sb_color==145):
		return (99, 251, 0);
	if(sb_color==146):
		return (99, 203, 255);
	if(sb_color==147):
		return (99, 203, 206);
	if(sb_color==148):
		return (99, 203, 156);
	if(sb_color==149):
		return (99, 203, 99);
	if(sb_color==150):
		return (99, 203, 49);
	if(sb_color==151):
		return (99, 203, 0);
	if(sb_color==152):
		return (99, 154, 255);
	if(sb_color==153):
		return (99, 154, 206);
	if(sb_color==154):
		return (99, 154, 156);
	if(sb_color==155):
		return (99, 154, 99);
	if(sb_color==156):
		return (99, 154, 49);
	if(sb_color==157):
		return (99, 154, 0);
	if(sb_color==158):
		return (99, 97, 255);
	if(sb_color==159):
		return (99, 97, 206);
	if(sb_color==160):
		return (99, 97, 156);
	if(sb_color==161):
		return (99, 97, 99);
	if(sb_color==162):
		return (99, 97, 49);
	if(sb_color==163):
		return (99, 97, 0);
	if(sb_color==164):
		return (99, 48, 255);
	if(sb_color==165):
		return (99, 48, 206);
	if(sb_color==166):
		return (99, 48, 156);
	if(sb_color==167):
		return (99, 48, 99);
	if(sb_color==168):
		return (99, 48, 49);
	if(sb_color==169):
		return (99, 48, 0);
	if(sb_color==170):
		return (99, 0, 255);
	if(sb_color==171):
		return (99, 0, 206);
	if(sb_color==172):
		return (99, 0, 156);
	if(sb_color==173):
		return (99, 0, 99);
	if(sb_color==174):
		return (99, 0, 49);
	if(sb_color==175):
		return (99, 0, 0);
	if(sb_color==176):
		return (49, 251, 255);
	if(sb_color==177):
		return (49, 251, 206);
	if(sb_color==178):
		return (49, 251, 156);
	if(sb_color==179):
		return (49, 251, 99);
	if(sb_color==180):
		return (49, 251, 49);
	if(sb_color==181):
		return (49, 251, 0);
	if(sb_color==182):
		return (49, 203, 255);
	if(sb_color==183):
		return (49, 203, 206);
	if(sb_color==184):
		return (49, 203, 156);
	if(sb_color==185):
		return (49, 203, 99);
	if(sb_color==186):
		return (49, 203, 49);
	if(sb_color==187):
		return (49, 203, 0);
	if(sb_color==188):
		return (49, 154, 255);
	if(sb_color==189):
		return (49, 154, 206);
	if(sb_color==190):
		return (49, 154, 156);
	if(sb_color==191):
		return (49, 154, 99);
	if(sb_color==192):
		return (49, 154, 49);
	if(sb_color==193):
		return (49, 154, 0);
	if(sb_color==194):
		return (49, 97, 255);
	if(sb_color==195):
		return (49, 97, 206);
	if(sb_color==196):
		return (49, 97, 156);
	if(sb_color==197):
		return (49, 97, 99);
	if(sb_color==198):
		return (49, 97, 49);
	if(sb_color==199):
		return (49, 97, 0);
	if(sb_color==200):
		return (49, 48, 255);
	if(sb_color==201):
		return (49, 48, 206);
	if(sb_color==202):
		return (49, 48, 156);
	if(sb_color==203):
		return (49, 48, 99);
	if(sb_color==204):
		return (49, 48, 49);
	if(sb_color==205):
		return (49, 48, 0);
	if(sb_color==206):
		return (49, 0, 255);
	if(sb_color==207):
		return (49, 0, 206);
	if(sb_color==208):
		return (49, 0, 156);
	if(sb_color==209):
		return (49, 0, 99);
	if(sb_color==210):
		return (49, 0, 49);
	if(sb_color==211):
		return (49, 0, 0);
	if(sb_color==212):
		return (0, 251, 255);
	if(sb_color==213):
		return (0, 251, 206);
	if(sb_color==214):
		return (0, 251, 156);
	if(sb_color==215):
		return (0, 251, 99);
	if(sb_color==216):
		return (0, 251, 49);
	if(sb_color==217):
		return (0, 251, 0);
	if(sb_color==218):
		return (0, 203, 255);
	if(sb_color==219):
		return (0, 203, 206);
	if(sb_color==220):
		return (0, 203, 156);
	if(sb_color==221):
		return (0, 203, 99);
	if(sb_color==222):
		return (0, 203, 49);
	if(sb_color==223):
		return (0, 203, 0);
	if(sb_color==224):
		return (0, 154, 255);
	if(sb_color==225):
		return (0, 154, 206);
	if(sb_color==226):
		return (0, 154, 156);
	if(sb_color==227):
		return (0, 154, 99);
	if(sb_color==228):
		return (0, 154, 49);
	if(sb_color==229):
		return (0, 154, 0);
	if(sb_color==230):
		return (0, 97, 255);
	if(sb_color==231):
		return (0, 97, 206);
	if(sb_color==232):
		return (0, 97, 156);
	if(sb_color==233):
		return (0, 97, 99);
	if(sb_color==234):
		return (0, 97, 49);
	if(sb_color==235):
		return (0, 97, 0);
	if(sb_color==236):
		return (0, 48, 255);
	if(sb_color==237):
		return (0, 48, 206);
	if(sb_color==238):
		return (0, 48, 156);
	if(sb_color==239):
		return (0, 48, 99);
	if(sb_color==240):
		return (0, 48, 49);
	if(sb_color==241):
		return (0, 48, 0);
	if(sb_color==242):
		return (0, 0, 255);
	if(sb_color==243):
		return (0, 0, 206);
	if(sb_color==244):
		return (0, 0, 156);
	if(sb_color==245):
		return (0, 0, 99);
	if(sb_color==246):
		return (0, 0, 49);
	if(sb_color==247):
		return (235, 235, 239);
	if(sb_color==248):
		return (222, 219, 222);
	if(sb_color==249):
		return (189, 186, 189);
	if(sb_color==250):
		return (173, 170, 173);
	if(sb_color==251):
		return (140, 138, 140);
	if(sb_color==252):
		return (115, 113, 115);
	if(sb_color==253):
		return (82, 81, 82);
	if(sb_color==254):
		return (66, 65, 66);
	if(sb_color==255):
		return (33, 32, 33);
	return (0, 0, 0);

def Print_Color(color):
	return "("+str(color[0])+", "+str(color[1])+", "+str(color[2])+")";

def Print_C_Color(color):
	return str(color[0])+", "+str(color[1])+", "+str(color[2]);

def SmileBasic_Hex_Graphic_Palette(sb_color):
	return SmileBasic_Graphic_Palette(int(sb_code, 16));

use_screen = 0;

'''
http://www.petitcomputer.com/manual/manual.pdf
'''
def Parse_SmileBasic(sb_code, screen, usegfx, code_output):
	global use_screen;
	codedone = False;
	drawupdate = False;
	if(use_screen==0):
		draw_screen = "ds_top_screen";
	if(use_screen==1):
		draw_screen = "ds_bottom_screen";
	if(re.findall("^CODE (.*)", sb_code, re.IGNORECASE) and codedone==False):
		gcode_exp = re.findall("^CODE (.*)", sb_code, re.IGNORECASE);
		if(code_output=="Python" or code_output=="Py"):
			print gcode_exp[0];
		if(code_output=="C"):
			print "  "+gcode_exp[0];
		codedone = True;
		drawupdate = False;
	if(re.findall("^PYCODE (.*)", sb_code, re.IGNORECASE) and codedone==False):
		gcode_exp = re.findall("^PYCODE (.*)", sb_code, re.IGNORECASE);
		if(code_output=="Python" or code_output=="Py"):
			print gcode_exp[0];
		codedone = True;
		drawupdate = False;
	if(re.findall("^CCODE (.*)", sb_code, re.IGNORECASE) and codedone==False):
		gcode_exp = re.findall("^CCODE (.*)", sb_code, re.IGNORECASE);
		if(code_output=="C"):
			print "  "+gcode_exp[0];
		codedone = True;
		drawupdate = False;
	if(re.findall("^GOTO \@([A-Z0-9])", sb_code, re.IGNORECASE) and codedone==False):
		glabel_exp = re.findall("^GOTO \@([A-Z0-9])", sb_code, re.IGNORECASE);
		if(code_output=="C"):
			print "  goto "+glabel_exp[0]+";";
		codedone = True;
		drawupdate = False;
	if(re.findall("^\@([A-Z0-9])", sb_code, re.IGNORECASE) and codedone==False):
		glabel_exp = re.findall("^\@([A-Z0-9])", sb_code, re.IGNORECASE);
		if(code_output=="C"):
			print "  "+glabel_exp[0]+": ";
		codedone = True;
		drawupdate = False;
	if(re.findall("^REM(.*)", sb_code, re.IGNORECASE) and codedone==False):
		grem_exp = re.findall("^REM(.*)", sb_code, re.IGNORECASE);
		if(code_output=="Python" or code_output=="Py"):
			print "#"+grem_exp[0];
		if(code_output=="C"):
			print "  //"+grem_exp[0];
		codedone = True;
		drawupdate = False;
	if(re.findall("^\'(.*)", sb_code, re.IGNORECASE) and codedone==False):
		grem_exp = re.findall("^\'(.*)", sb_code, re.IGNORECASE);
		if(code_output=="Python" or code_output=="Py"):
			print "#"+grem_exp[0];
		if(code_output=="C"):
			print "  //"+grem_exp[0];
		codedone = True;
		drawupdate = False;
	if(re.findall("^GCLS ([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gcls_exp = re.findall("^GCLS\s*([0-9]+)", sb_code, re.IGNORECASE);
		if(code_output=="Python" or code_output=="Py"):
			print draw_screen+".fill("+Print_Color(SmileBasic_Graphic_Palette(int(gcls_exp[0])))+");";
		if(code_output=="C"):
			print "  SDL_FillRect("+draw_screen+", NULL, SDL_MapRGB("+draw_screen+"->format, "+Print_C_Color(SmileBasic_Graphic_Palette(int(gcls_exp[0])))+"));";
			#print "  boxRGBA("+draw_screen+", 0, 0, 255, 383, "+Print_C_Color(SmileBasic_Graphic_Palette(int(gcls_exp[0])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GSPOIT\s*\(\s*([0-9]+)\s*,\s*([0-9]+)\s*\)", sb_code, re.IGNORECASE) and codedone==False):
		gspoit_exp = re.findall("^GSPOIT\s*\(\s*([0-9]+)\s*,\s*([0-9]+)\s*\)", sb_code, re.IGNORECASE);
		gspoit_exp = gspoit_exp[0];
		if(code_output=="Python" or code_output=="Py"):
			print "tuple("+draw_screen+".get_at(("+str(int(gspoit_exp[0]))+", "+str(int(gspoit_exp[0]))+")));";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GPAGE ([0-1])", sb_code, re.IGNORECASE) and codedone==False):
		gpage_exp = re.findall("^GPAGE ([0-1])", sb_code, re.IGNORECASE);
		if(int(gpage_exp[0])==0):
			use_screen = 0;
		if(int(gpage_exp[0])==1):
			use_screen = 1;
		codedone = True;
		drawupdate = False;
	if(re.findall("^GCOLOR ([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gcolor_exp = re.findall("^GCOLOR ([0-9]+)", sb_code, re.IGNORECASE);
		if(code_output=="Python" or code_output=="Py"):
			print "ptcolor = gcolor_exp[0];";
		codedone = True;
		drawupdate = False;
	if(re.findall("^GPAINT ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gpaint_exp = re.findall("^GPAINT ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gpaint_exp = gpaint_exp[0];
		if(code_output=="Python" or code_output=="Py"):
			print draw_screen+".fill("+Print_Color(SmileBasic_Graphic_Palette(int(gpaint_exp[0])))+");";
		if(code_output=="C"):
			print "  SDL_FillRect("+draw_screen+", NULL, SDL_MapRGB("+draw_screen+"->format, "+Print_C_Color(SmileBasic_Graphic_Palette(int(gpaint_exp[0])))+"));";
			#print "  boxRGBA("+draw_screen+", 0, 0, 255, 383, "+Print_C_Color(SmileBasic_Graphic_Palette(int(gpaint_exp[0])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GPAINT ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gpaint_exp = re.findall("^GPAINT ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gpaint_exp = gpaint_exp[0];
		if(code_output=="Python" or code_output=="Py"):
			print draw_screen+".fill("+Print_Color(SmileBasic_Graphic_Palette(int(gpaint_exp[2])))+");";
		if(code_output=="C"):
			print "  SDL_FillRect("+draw_screen+", NULL, SDL_MapRGB("+draw_screen+"->format, "+Print_C_Color(SmileBasic_Graphic_Palette(int(gpaint_exp[2])))+"));";
			#print "  boxRGBA("+draw_screen+", 0, 0, 255, 383, "+Print_C_Color(SmileBasic_Graphic_Palette(int(gpaint_exp[2])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GPAINT ([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gpaint_exp = re.findall("^GPAINT ([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gpaint_exp = gpaint_exp[0];
		if(code_output=="Python" or code_output=="Py"):
			print draw_screen+".fill("+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
		if(code_output=="C"):
			print "  SDL_FillRect("+draw_screen+", NULL, SDL_MapRGB("+draw_screen+"->format, "+Print_C_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+"));";
			#print "  boxRGBA("+draw_screen+", 0, 0, 255, 383, "+Print_C_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GSPOT ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gspot_exp = re.findall("^GSPOT ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gspot_exp = gspot_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.line("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(gcls_exp[2])))+", ("+str(int(gspot_exp[0]))+", "+str(int(gspot_exp[0]))+"), ("+str(int(gspot_exp[1]))+", "+str(int(gspot_exp[1]))+"));";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.pixel("+draw_screen+", "+str(int(gspot_exp[0]))+", "+str(int(gspot_exp[1]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gcls_exp[2])))+");";
		if(code_output=="C"):
			print "  pixelRGBA("+draw_screen+", "+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(gline_exp[4])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GSPOT ([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gspot_exp = re.findall("^GSPOT ([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gspot_exp = gspot_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.line("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", ("+str(int(gspot_exp[0]))+", "+str(int(gspot_exp[0]))+"), ("+str(int(gspot_exp[1]))+", "+str(int(gspot_exp[1]))+"));";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.pixel("+draw_screen+", "+str(int(gspot_exp[0]))+", "+str(int(gspot_exp[1]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
		if(code_output=="C"):
			print "  pixelRGBA("+draw_screen+", "+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GLINE ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gline_exp = re.findall("^GLINE ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gline_exp = gline_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.line("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(gline_exp[4])))+", ("+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+"), ("+str(int(gline_exp[2]))+", "+str(int(gline_exp[3]))+"));";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.line("+draw_screen+", "+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+", "+str(int(gline_exp[2]))+", "+str(int(gline_exp[3]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gline_exp[4])))+");";
		if(code_output=="C"):
			print "  lineRGBA("+draw_screen+", "+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+", "+str(int(gline_exp[2]))+", "+str(int(gline_exp[3]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(gline_exp[4])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GLINE ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gline_exp = re.findall("^GLINE ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gline_exp = gline_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.line("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", ("+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+"), ("+str(int(gline_exp[2]))+", "+str(int(gline_exp[3]))+"));";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.line("+draw_screen+", "+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+", "+str(int(gline_exp[2]))+", "+str(int(gline_exp[3]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
		if(code_output=="C"):
			print "  lineRGBA("+draw_screen+", "+str(int(gline_exp[0]))+", "+str(int(gline_exp[1]))+", "+str(int(gline_exp[2]))+", "+str(int(gline_exp[3]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GBOX ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gbox_exp = re.findall("^GBOX ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gbox_exp = gbox_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.lines("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(gbox_exp[4])))+", False, [("+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+"), ("+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[1]))+"), ("+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[3]))+"), ("+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[3]))+"), ("+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+")], True);";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.hline("+draw_screen+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[1]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gbox_exp[4])))+");";
				print "pygame.gfxdraw.vline("+draw_screen+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+", "+str(int(gbox_exp[3]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gbox_exp[4])))+");";
				print "pygame.gfxdraw.hline("+draw_screen+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[3]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gbox_exp[4])))+");";
				print "pygame.gfxdraw.vline("+draw_screen+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[3]))+", "+str(int(gbox_exp[1]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gbox_exp[4])))+");";
		if(code_output=="C"):
			print "  rectangleRGBA("+draw_screen+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[3]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(gbox_exp[4])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GBOX ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gbox_exp = re.findall("^GBOX ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gbox_exp = gbox_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.lines("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", False, [("+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+"), ("+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[1]))+"), ("+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[3]))+"), ("+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[3]))+"), ("+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+")], True);";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.hline("+draw_screen+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[1]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
				print "pygame.gfxdraw.vline("+draw_screen+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+", "+str(int(gbox_exp[3]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
				print "pygame.gfxdraw.hline("+draw_screen+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[3]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
				print "pygame.gfxdraw.vline("+draw_screen+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[3]))+", "+str(int(gbox_exp[1]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
		if(code_output=="C"):
			print "  rectangleRGBA("+draw_screen+", "+str(int(gbox_exp[0]))+", "+str(int(gbox_exp[1]))+", "+str(int(gbox_exp[2]))+", "+str(int(gbox_exp[3]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GFILL ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gfill_exp = re.findall("^GFILL ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gfill_exp = gfill_exp[0];
		'''
		https://github.com/klange/Python-Asteroids-Clone/blob/master/pscreen.py
		'''
		if(code_output=="Python" or code_output=="Py"):
			if int(gfill_exp[0]) < int(gfill_exp[2]):
				x_arg=int(gfill_exp[0])
			else:
				x_arg=int(gfill_exp[2])
			if int(gfill_exp[1]) < int(gfill_exp[3]):
				y_arg=int(gfill_exp[1])
			else:
				y_arg=int(gfill_exp[3])
			w_arg=abs(int(gfill_exp[2]) - int(gfill_exp[0])) + 1;
			h_arg=abs(int(gfill_exp[3]) - int(gfill_exp[1])) + 1;
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.rect("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(gfill_exp[4])))+", ("+str(int(x_arg))+", "+str(int(y_arg))+", "+str(int(w_arg))+", "+str(int(h_arg))+"));";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.box("+draw_screen+", ("+str(int(x_arg))+", "+str(int(y_arg))+", "+str(int(w_arg))+", "+str(int(h_arg))+"), "+Print_Color(SmileBasic_Graphic_Palette(int(gfill_exp[4])))+");";
		if(code_output=="C"):
			print "  boxRGBA("+draw_screen+", "+str(int(gfill_exp[0]))+", "+str(int(gfill_exp[1]))+", "+str(int(gfill_exp[2]))+", "+str(int(gfill_exp[3]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(gfill_exp[4])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GFILL ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gfill_exp = re.findall("^GFILL ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gfill_exp = gfill_exp[0];
		'''
		https://github.com/klange/Python-Asteroids-Clone/blob/master/pscreen.py
		'''
		if(code_output=="Python" or code_output=="Py"):
			if int(gfill_exp[0]) < int(gfill_exp[2]):
				x_arg=int(gfill_exp[0])
			else:
				x_arg=int(gfill_exp[2])
			if int(gfill_exp[1]) < int(gfill_exp[3]):
				y_arg=int(gfill_exp[1])
			else:
				y_arg=int(gfill_exp[3])
			w_arg=abs(int(gfill_exp[2]) - int(gfill_exp[0])) + 1;
			h_arg=abs(int(gfill_exp[3]) - int(gfill_exp[1])) + 1;
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.draw.rect("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", ("+str(int(x_arg))+", "+str(int(y_arg))+", "+str(int(w_arg))+", "+str(int(h_arg))+"));";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.box("+draw_screen+", ("+str(int(x_arg))+", "+str(int(y_arg))+", "+str(int(w_arg))+", "+str(int(h_arg))+"), "+Print_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+");";
		if(code_output=="C"):
			print "  boxRGBA("+draw_screen+", "+str(int(gfill_exp[0]))+", "+str(int(gfill_exp[1]))+", "+str(int(gfill_exp[2]))+", "+str(int(gfill_exp[3]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(ptcolor)))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^GCIRCLE ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE) and codedone==False):
		gcircle_exp = re.findall("^GCIRCLE ([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)\s*,\s*([0-9]+)", sb_code, re.IGNORECASE);
		gcircle_exp = gcircle_exp[0];
		if(usegfx==False):
			if(code_output=="Python" or code_output=="Py"):
				print "drawCircleArc("+draw_screen+", "+Print_Color(SmileBasic_Graphic_Palette(int(gcircle_exp[3])))+", ("+str(int(gcircle_exp[0]))+", "+str(int(gcircle_exp[1]))+"), "+str(int(gcircle_exp[2]))+", "+str(int(gcircle_exp[4]))+", "+str(int(gcircle_exp[5]))+", 1);";
		if(usegfx==True):
			if(code_output=="Python" or code_output=="Py"):
				print "pygame.gfxdraw.arc("+draw_screen+", ("+str(int(gcircle_exp[0]))+", "+str(int(gcircle_exp[1]))+"), "+str(int(gcircle_exp[2]))+", "+str(int(gcircle_exp[4]))+", "+str(int(gcircle_exp[5]))+", "+Print_Color(SmileBasic_Graphic_Palette(int(gcircle_exp[3])))+");";
		if(code_output=="C"):
			print "  arcRGBA("+draw_screen+", "+str(int(gcircle_exp[0]))+", "+str(int(gcircle_exp[1]))+", "+str(int(gcircle_exp[2]))+", "+str(int(gcircle_exp[4]))+", "+str(int(gcircle_exp[5]))+", "+Print_C_Color(SmileBasic_Graphic_Palette(int(gline_exp[4])))+", 255);";
		codedone = True;
		drawupdate = True;
	if(re.findall("^REBOOT", sb_code, re.IGNORECASE) and codedone==False):
		greboot_exp = re.findall("^REBOOT", sb_code, re.IGNORECASE);
		greboot_exp = greboot_exp[0];
		if(code_output=="Python" or code_output=="Py"):
			print "done = True;\n";
		codedone = True;
		drawupdate = False;
	if(drawupdate==True):
		if(use_screen==0):
			if(code_output=="Python" or code_output=="Py"):
				print screen+".blit("+draw_screen+", (0, 0));";
			if(code_output=="C"):
				print "  SDL_Flip("+draw_screen+");";
				print "  SDL_BlitSurface("+draw_screen+", NULL, "+screen+", &ds_top_screen_rect);";
		if(use_screen==1):
			if(code_output=="Python" or code_output=="Py"):
				print screen+".blit("+draw_screen+", (0, 192));";
			if(code_output=="C"):
				print "  SDL_Flip("+draw_screen+");";
				print "  SDL_BlitSurface("+draw_screen+", NULL, "+screen+", &ds_bottom_screen_rect);";
		if(code_output=="Python" or code_output=="Py"):
			print "pygame.display.update();\n";
		if(code_output=="C"):
			print "  SDL_Flip("+screen+");\n";
	return True;

sys.argv[1] = sys.argv[1].replace("\\", "/");
SB_File=open(sys.argv[1], "rbU");
SB_FileType = SB_File.read(2);
if(SB_FileType==binascii.unhexlify("1F8B")):
	SB_File.close();
	SB_File = gzip.open(sys.argv[1], "rb");
if(SB_FileType!=binascii.unhexlify("1F8B")):
	SB_File.seek(0);
	SB_FileType = SB_File.read(3);
	if(SB_FileType=="BZh"):
		SB_File.close();
		SB_File = bz2.BZ2File(sys.argv[1], "rb");
SB_File.seek(0);
SB_FileType = SB_File.read(4);
if(SB_FileType!="PX01"):
	if(code_output=="Python" or code_output=="Py"):
		print "pygame.display.set_caption(\"Petit Computer - "+os.path.splitext(os.path.basename(sys.argv[1]))[0]+"\");\n";
	if(code_output=="C"):
		print "  SDL_WM_SetCaption(\"Petit Computer - "+os.path.splitext(os.path.basename(sys.argv[1]))[0]+"\", \"Petit Computer - "+os.path.splitext(os.path.basename(sys.argv[1]))[0]+"\");\n";
	SB_File.seek(0);
if(SB_FileType=="PX01"):
	SB_File.seek(12);
	SB_FileTitle = SB_File.read(8).strip();
	if(code_output=="Python" or code_output=="Py"):
		print "pygame.display.set_caption(\"Petit Computer - "+SB_FileTitle+"\";\n";
	if(code_output=="C"):
		print "  SDL_WM_SetCaption(\"Petit Computer - "+SB_FileTitle+"\", \"Petit Computer - "+SB_FileTitle+"\");\n";
	SB_File.seek(60);
SB_Exp=SB_File.readlines();
SB_File.close();
SB_i=0;
SB_Num=len(SB_Exp);
while(SB_i<SB_Num):
	if(SB_Exp[SB_i]!=" "):
		Parse_SmileBasic(SB_Exp[SB_i].strip(), "ds_screen", enable_gfxdraw, code_output);
	SB_i = SB_i + 1;
if(code_output=="Python" or code_output=="Py"):
	print "tend = time.clock();";
	print "print \"execution time: %.2gs\" % (tend-tstart);";
	print "while not done:";
	print "	for event in pygame.event.get():";
	print "		if (event.type == pygame.KEYDOWN):";
	print "			if (event.key == pygame.K_ESCAPE):";
	print "				done = True;";
	print "		if (event.type == pygame.QUIT):";
	print "			done = True;\n";
	print "pygame.display.quit();";
	print "pygame.quit();";
	print "exit();\n";

if(code_output=="C"):
	print "  while(done==false) {";
	print "    if (SDL_PollEvent(&event)) {";
	print "      switch (event.type) {";
	print "        case SDL_QUIT:";
	print "          done = true;";
	print "          break;";
	print "        case SDL_KEYDOWN:";
	print "          switch (event.key.keysym.sym) {";
	print "            case SDLK_ESCAPE:";
	print "              done = true;";
	print "              break;";
	print "          }";
	print "          break;";
	print "      }";
	print "    }";
	print "  }";
	print "  SDL_Quit();";
	print "  return 0;\n}";

exit();
