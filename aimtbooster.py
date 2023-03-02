import numpy as np
import cv2
import time
import random
import mss
import mouse

time.sleep(2)

X_OFFSET = 585
Y_OFFSET = 440

WIDTH = 750
HEIGHT = 525

sct = mss.mss()
mon = {"top": Y_OFFSET, "left": X_OFFSET, "width": WIDTH, "height": HEIGHT}

while True:

    #last_time = time.perf_counter()

    printscreen_np = np.asarray(sct.grab(mon))

    loc = np.argwhere(np.logical_and(printscreen_np[:,:,0] == 0,
                                     printscreen_np[:,:,1] == 255,
                                     printscreen_np[:,:,2] == 0))

    if len(loc) > 1: 
        target = random.randrange(len(loc))
        mouse.move(X_OFFSET + loc[target][1], Y_OFFSET + loc[target][0], absolute=True)
        
        mouse.click()


    #cv2.imshow("", printscreen_np[:,:,::])
    #print(f"{(time.perf_counter() - last_time) * 1000} ms")

    #if cv2.waitKey(25) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
        #break
