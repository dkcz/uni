import time

print()

while True:
    tm = int(time.strftime("%S"))
    #print (tm)
    line = 0
    posx = 0
    if tm < 8:
        line = 0
    elif 8 <= tm <= 16:
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
    elif 57 <= tm <= 60:
        line = 7

    posx = tm - 8 * line - 1
    if posx == -1:
        posx = 0
    print str(posx) + " , " + str(line) + " , " + str(tm)

    time.sleep(1)

