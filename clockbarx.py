import time
import unicornhat as uh
import colorsys as col


uh.set_layout(uh.HAT)
uh.rotation(0)
uh.brightness(0.5)

def png(x,y,h):
	r,g,b = [int(c*255) for c in col.hsv_to_rgb(h,1,1)]
	uh.set_pixel(x,y,r,g,b)

def clr():
     for x in range(8):
         for y in range(8):
             uh.set_pixel(x, y, 0, 0, 0)
     uh.show()
sat = 0.0

png(0,0,0.7)
time.sleep(10)

while True:
    tm = int(time.strftime("%S"))
    mm = int(time.strftime("%M"))
    hh = int(time.strftime("%H"))
    #sat = mm * 0.016
    #print(sat)
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

    if line < 4:
	sat = mm * 0.016
    else:
	sat = hh * 0.083     
    print(sat)
    if posx == -1:
        clr()
    else:
    	# if tm == 0:
    	#     clr()

    	#print str(posx) + " , " + str(line) + " , " + str(tm)
    	png(posx,line,sat)
	#uh.set_pixel(posx, line, 0, 255, 0)
    	uh.show()
    time.sleep(1)

