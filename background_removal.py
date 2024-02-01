# import cv2 to capture videofeed
import cv2
import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(1)

# setting framewidth and frameheight as 640 X 480
camera.set(3, 640)
camera.set(4, 480)

# loading the mountain image
mountain = cv2.imread('mount_everest.jpg')  # Make sure the image file name is correct
mountain = cv2.resize(mountain, (640, 480))  # Resize the mountain image to match the camera resolution

while True:
    # read a frame from the attached camera
    status, frame = camera.read()

    # if we got the frame successfully
    if status:
        # flip it
        frame = cv2.flip(frame, 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # creating thresholds (replace lower_bound and upper_bound with your actual threshold values)
        lower_bound = np.array([100, 100, 100])
        upper_bound = np.array([255, 255, 255])

        # thresholding image
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)

        # inverting the mask
        inverted_mask = cv2.bitwise_not(mask)

        # bitwise and operation to extract foreground / person
        person = cv2.bitwise_and(frame, frame, mask=inverted_mask)

        # final image (replace person with mountain image or combine them based on your requirement)
        final_image = cv2.add(person, mountain)

        # show it
        cv2.imshow('frame', final_image)

        # wait for 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code == 32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
