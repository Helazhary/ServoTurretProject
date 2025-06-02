import serial
import time
import cv2

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

angle = 20
ser.write(f"{angle}\n".encode())
time.sleep(2)
angle = 160
ser.write(f"{angle}\n".encode())

ser.close()


# cam = cv2.VideoCapture(4)


# # Get the default frame width and height
# frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

# while True:
#     ret, frame = cam.read()

#     # Write the frame to the output file
#     out.write(frame)

#     # Display the captured frame
#     cv2.imshow('Camera', frame)

#     # Press 'q' to exit the loop
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the capture and writer objects
# cam.release()
# out.release()
# cv2.destroyAllWindows()