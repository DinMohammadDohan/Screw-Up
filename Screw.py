import rotatescreen
import time
screen = rotatescreen.get_primary_display()
for x in range(13):
    time.sleep(1)
    screen.rotate_to(x*90%360)

