import time
import unicornhat as uh
import colorsys as col


uh.set_layout(uh.HAT)
uh.rotation(0)
uh.brightness(0.5)

def clr():
     for x in range(8):
         for y in range(8):
             uh.set_pixel(x, y, 0, 0, 0)
     uh.show()


while True:
    tm = int(time.strftime("%S"))
    # print (tm)
    line = 0
    posx = 0
    if tm < 9:
        line = 0
    elif 9 <= tm <= 16:
        line = 1
    elif 17 <= tm <= 24:
        line = 2
    elif 25 <= tm <= 32:
        line = 3
    elif 33 <= tm <= 40:
        line = 4
    elif 41 <= tm <= 48:
        line = 5
    elif 49 <= tm <= 56:
        line = 6
    elif 57 <= tm <= 59:
        line = 7

    posx = tm - 8 * line - 1
    if posx == -1:
        clr()
    else:
    	# if tm == 0:
    	#     clr()

    	#print str(posx) + " , " + str(line) + " , " + str(tm)
    	uh.set_pixel(posx, line, 255, 255, 255)
    	uh.show()
    time.sleep(1)

