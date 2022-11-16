# stuff handler
import keyboard as key
import os
# video handler
import cv2
# music handler
from ffpyplayer.player import MediaPlayer

# useless but im keeping it becuese it makes my code look specal
site = [ "https://www.youtube.com/watch?v=32BY-Ram35M" ]

# file locator
pengus = os.path.dirname(os.path.abspath(__file__)) + str("\g")
path = pengus + "reen.mp4"

# the video part
def ded():
    video=cv2.VideoCapture(path)
    player = MediaPlayer(path)
    wub = "dog"
    
    while True:
    
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
    
        if not grabbed:
            print("errorish")
            break
      
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
     
        cv2.imshow(wub, frame)
        cv2.setWindowProperty(wub, cv2.WND_PROP_TOPMOST, 1)
        if val != 'eof' and audio_frame is not None:
            img, t = audio_frame
   
    video.release()
    cv2.destroyAllWindows()

key.add_hotkey('f12', lambda: ded())

key.wait('esc')


# just some code i wana keep in

# window_name = "image"
# img = np.zeros([480, 640, 1])
# cv2.imshow(window_name, img)
# cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)
# cv2.waitKey(0)


    # cap = cv2.VideoCapture(fileat +'reen.mp4')
    
    # if (cap.isOpened()== False):
    #     print("Error opening video file")
    

    # while(cap.isOpened()):
    #     ret, frame = cap.read()
    #     if ret == True:
    #         wub = "penis"
    #         cv2.imshow(wub, frame)
    #         cv2.setWindowProperty(wub, cv2.WND_PROP_TOPMOST, 1)

    #         if cv2.waitKey(25) & 0xFF == ord('q'):
    #             break

    #     else:
    #         break
    
    # cap.release()
    
    # cv2.destroyAllWindows()
 
