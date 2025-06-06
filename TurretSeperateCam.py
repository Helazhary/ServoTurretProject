import serial
import time
import cv2

# --- Serial Setup ---
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

# --- Camera Setup ---
cam = cv2.VideoCapture(2) 
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# center_x = frame_width // 2
# center_y = frame_height // 2

# --- Face Detection ---
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#--- controls ---
sweep_direction = 1
pan_angle = 90
tilt_angle = 90

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=8, minSize=(40, 40)
    )

    print(faces)
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     middlex = (x+w)//2
    #     middley = (x+h)//2

    

    # print(middlex, middley)

    cv2.imshow("Face Tracking Turret", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # try:
    #     ser.write(f"{pan_angle},{tilt_angle}\n".encode())
    # except:
    #     pass

cam.release()
cv2.destroyAllWindows()
ser.close()