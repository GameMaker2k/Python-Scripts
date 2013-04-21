REM switch to top screen
GPAGE 0
REM clear and color top screen
GCLS 11
REM draw a box on top screen
GBOX 0, 0, 255, 191, 4
REM draw a filled box on top screen
GFILL 63, 47, 192, 144, 4
REM draw another box on top screen
GBOX 65, 49, 190, 142, 11
REM switch to bottom screen
GPAGE 1
REM clear and color bottom screen
GCLS 4
REM draw a filled box on bottom screen
GBOX 0, 0, 255, 191, 11
REM draw a filled box on bottom screen
GFILL 63, 47, 192, 144, 11
REM draw another box on top screen
GBOX 65, 49, 190, 142, 4