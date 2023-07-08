import mediapipe as mp
import cv2
import pyautogui
import time
WIDTH = 1920
HEIGHT = 1080
cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4, 2)
i = 0
previous_click_time = 0
click_delay = 2
while True:
    success, image = cap.read()
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks
    if multiLandMarks:
        handList = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(image, handLms, mp_Hands.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                # map co-ordinates to the screen size
                cx, cy = WIDTH - lm.x*WIDTH, lm.y*HEIGHT
                handList.append((cx, cy))
            if (handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]):
                print(handList[8][0], handList[8][1])
                pyautogui.moveTo(handList[8][0], handList[8][1])
            elif (abs(handList[8][1] - handList[4][1]) < 15):
                current_time = time.time()
                if current_time - previous_click_time >= click_delay:
                    print('yay')
                    pyautogui.click()
                    previous_click_time = current_time
        cv2.imshow("whatever", image)
        cv2.waitKey(1)

#            for coordinate in finger_Coord:
#                print(coordinate)
#                if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
#                    upCount += 1
#            if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
#                upCount += 1
