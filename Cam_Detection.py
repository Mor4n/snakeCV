import cv2
import pyautogui

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default (2).xml')

while True:
    ret, frame = cap.read()

    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), maxSize=(200, 200))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    face_center_x = x + w // 2
    face_center_y = y + h // 2

    if face_center_x < 200:
        pyautogui.press('left')
        print("Moviendo hacia la izquierda")
    elif face_center_x > 440:
        pyautogui.press('right')
        print("Moviendo hacia la derecha")
    elif face_center_y > 440:
        pyautogui.press('right')
        print("Moviendo hacia la derecha")
    elif face_center_y > 440:
        pyautogui.press('right')
        print("Moviendo hacia la derecha")

    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
