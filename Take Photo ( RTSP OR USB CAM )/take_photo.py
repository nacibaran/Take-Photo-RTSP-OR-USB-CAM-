import cv2

cap=cv2.VideoCapture("YOUR RTSP URL OR   JUST  0  ")

num=0

while cap.isOpened():

    succes1, img = cap.read()


    k = cv2.waitKey(1)

    if k == 27:
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('C:/Users/nacib/Desktop/PYQT/Foto' + str(num+1) + '.png', img)
        print("images saved!")
        num += 1

    cv2.imshow('Img 1',img)
