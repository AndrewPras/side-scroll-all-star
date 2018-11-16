import numpy as np
import cv2
import time
import mss


def screen_record_efficient() -> int:
    # 600x480 windowed mode
    mon = {"top": 45, "left": 100, "width": 600, "height": 480}

    title = "[MSS] FPS benchmark"
    fps = 0
    sct = mss.mss()
    last_time = time.time()

    while time.time() - last_time < 125:
        img = np.asarray(sct.grab(mon))
        fps += 1

        # Our operations on the frame come here
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow(title, gray_img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps
