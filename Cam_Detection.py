import cv2
import pyautogui

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default (2).xml')

while True:
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), maxSize=(200, 200))

    # Face detection logic (if face detected)
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            face_center_x = x + w // 2
            face_center_y = y + h // 2

            if face_center_x < 200:
                pyautogui.press('left')
                print("Moving left")
            elif face_center_x > 440:
                pyautogui.press('right')
                print("Moving right")

    # Display the frame regardless of face detection
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()