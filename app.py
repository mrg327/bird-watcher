from flask import Flask, render_template, Response
import cv2
import time
import threading

app = Flask(__name__)

class Camera:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Lock to synchronize frame access among multiple threads
        self.frame_lock = threading.Lock()
        self.current_frame = None

        # Start a background thread to update frames
        self.is_running = True
        self.thread = threading.Thread(target=self.update_frames, daemon=True)
        self.thread.start()

    def update_frames(self):
        """Read frames from the camera in a loop and store them in memory."""
        while self.is_running:
            ret, frame = self.cap.read()
            if not ret:
                continue
            # Safely update current_frame
            with self.frame_lock:
                self.current_frame = frame
            
            # A small sleep can help reduce CPU usage
            time.sleep(0.01)

    def get_frame(self):
        """Return the current frame."""
        with self.frame_lock:
            frame_copy = self.current_frame.copy() if self.current_frame is not None else None
        return frame_copy

    def stop(self):
        self.is_running = False
        self.thread.join()
        self.cap.release()

# Create a global Camera object (one-time camera initialization)
camera = Camera(camera_index=0)

def gen_frames():
    while True:
        frame = camera.get_frame()

        # It's possible that the first few reads might be None if the camera isn't ready
        if frame is None:
            time.sleep(0.1)
            continue
        
        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        # Yield as multipart/x-mixed-replace response (MJPEG)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')



# camera = cv2.VideoCapture(0)
# def generate_frames():
#     # TODO: Only one user can use this at a time rn.
#     # we must decouple the rendering of the video from the accessing
#     # of the webpage.
#     while True:
#
#         ## read the camera frame
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode(".jpg", frame)
#             frame = buffer.tobytes()
#
#         yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video")
def video():
    return Response(
        gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True)
