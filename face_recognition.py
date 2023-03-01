
import cv2
import dlib 

img = cv2.imread("face_blackpink.jpg")

# show the image
cv2.imshow(winname="face recognition app", mat=img)

# wait for key press exit
cv2.waitkey(delay=0)

cv2.destroyAllWindows()