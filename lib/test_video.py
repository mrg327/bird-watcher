import cv2

"""
This is an example file taken from GeeksForGeeks.com to demo
streaming in the camera feed.
"""

# Open the default camera
CAM = cv2.VideoCapture(0)


def preview_video():
    # Get the default frame width and height
    frame_width = int(CAM.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(CAM.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (frame_width, frame_height))

    while True:
        ret, frame = CAM.read()

        # Write the frame to the output file
        out.write(frame)

        # Display the captured frame
        cv2.imshow("Camera", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord("q"):
            break

    # Release the capture and writer objects
    CAM.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    preview_video()
