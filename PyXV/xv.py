#!/usr/bin/python
import os, sys, pygame;

pygame.display.init();
pyicon=pygame.image.load("/mnt/utmp/upctest/old_icon.png");
pygame.display.set_icon(pyicon);
ppmimg=pygame.image.load(sys.argv[1]);
width, height = ppmimg.get_size();
screen = pygame.display.set_mode((width, height));
pygame.display.set_caption("PyXV - "+os.path.basename(sys.argv[1]));
pygame.display.get_active();
pygame.mouse.set_visible(0);

screen.blit(ppmimg, (0, 0));
pygame.display.flip();
done = False;
while not done:
 for event in pygame.event.get():
  if (event.type == pygame.QUIT):
   done = True;
  if (event.type == pygame.KEYDOWN):
   if (event.key == pygame.K_t) or (event.key == pygame.K_w):
    pygame.display.toggle_fullscreen();
   if (event.key == pygame.K_i) or (event.key == pygame.K_m):
    pygame.display.iconify();
   if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
    done = True;
pygame.display.quit();
pygame.quit();
exit();
