import cv2
import numpy as np

# Load the video
video_path = 'video.webm'
cap = cv2.VideoCapture(video_path)

# Define ASCII character set
# ascii_chars = list(" ⠈⠂⠄⠆⠇⠋⠙⠛⠿⡀⡄⣀⣄⣤⣶⣷⣿")
ascii_chars = [chr(i) for i in range(0x2800, 0x2900)]
x = 0
while(cap.isOpened()):
    x += 1
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame
    resized_frame = cv2.resize(frame, (40, 20)) # Adjust size as needed
    # resized_frame = cv2.resize(frame, (300,144)) # Adjust size as needed
    # Convert to grayscale
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Create ASCII art
    ascii_frame = ""
    for row in gray_frame:
        for pixel in row:
            brightness = pixel / 255  # Normalize brightness
            index = int(brightness * (len(ascii_chars) - 1))  # Map to character index
            ascii_frame += ascii_chars[index]
        ascii_frame += '\n'

    # Display or process ASCII frame (e.g., save to file)
    print(ascii_frame)
    frame = open(f"frames/frame{str(x).zfill(4)}.txt","w")
    frame.write(ascii_frame)
    frame.close()

cv2.destroyAllWindows()
