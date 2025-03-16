
import cv2
import random

# Path to the video file
video_path = 'firstFlight.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Set the video to the first frame
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Read the frame
ret, frame = cap.read()

if ret:
    # Display the frame
    cv2.imshow('First Frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to retrieve frame")

# Release the video capture object
cap.release()
# %%
