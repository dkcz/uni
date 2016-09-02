import colorsys as col
import unicornhat as uh
import time

uh.set_layout(uh.HAT)
uh.brightness(1.0)
uh.rotation(0)

def png(x,y,h,s,v):
	r,g,b = [int(c*255) for c in col.hsv_to_rgb(h,s,v)]
	uh.set_pixel(x,y,r,g,b)
	
def clear():
	for x in range(8):
		for y in range(8):
			uh.set_pixel(x,y,0,0,0)
	uh.show()

sat = 0.35


while True:
	for x in range(8):
		png(x,0,sat,1,1)
		uh.show()
		sat = sat - 0.05
		if sat <= 0:
			sat=0.35
		time.sleep(0.03)
	for x in range(8,-1,-1):
		uh.set_pixel(x,0,0,0,0)
		uh.show()
		time.sleep(0.05)
	
