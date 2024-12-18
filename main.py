import cv2
import numpy as np
import time

# Start video capture
cap = cv2.VideoCapture(0)

# Allow the camera to warm up
time.sleep(2)

# Capture the background (use a static frame for better results)
ret, background = cap.read()
background = cv2.flip(background, 1)  # Flip the background

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip the frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert to HSV color space

    # Define the color range for dark teal/blue
    lower_teal = np.array([85, 40, 40])
    upper_teal = np.array([105, 255, 255])

    # Create mask for teal/blue
    mask = cv2.inRange(hsv, lower_teal, upper_teal)



    # Refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract the background where the cloak is present
    res1 = cv2.bitwise_and(background, background, mask=mask)

    # Extract the current frame where the cloak is not present
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine both results
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display the result
    cv2.imshow("Invisible Cloak", final_output)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
