### Takes a video from webcam using python
### Can add filters later

from cv2 import cv2

vid = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# for more info on fourcc http://www.fourcc.org/codecs.php 
# fourcc is a code for video format
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
# Here 20.0 is the frames per second and the last argument is the size in the form of a tuple

while(vid.isOpened()):
    # isOpened condition checks whether the video file exists or not along the given path.
    success, frame = vid.read()
    if success == True:
        #####################gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        # cvtColor converts the color of the video in frame to the color given in the 2nd argument
        #####################print(vid.get(cv2.CAP_PROP_BRIGHTNESS))
        # the other properties can be found at https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        out.write(frame)
        # writes to the file 'out' in this case
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    else:
        break


out.release()
vid.release()
cv2.destroyAllWindows()
