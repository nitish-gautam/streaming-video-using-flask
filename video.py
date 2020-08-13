# import libraries
import cv2

face_cascade = cv2.CascadeClassifier(
    "binaries\haarcascade_frontalface_default.xml")


class VideoCamera(object):
    ''' Start the Video Capture '''

    def __init__(self):
        self.video = cv2.VideoCapture(0)

    ''' Stop the Video Capture '''

    def __del__(self):
        self.video.release()

    ''' Detect the face using harcascade  '''

    def get_frame(self):
        # Read the frame
        _, frame = self.video.read()

        # My defualt webcam resolution is :width = 640 height = 480
        #print('Original Dimensions of frame : ', frame.shape)

        # Scaling can change the frame size regardless of camera's resolution which,
        # of course, could lead to poor results on upscaling as it will be too pixelated.
        scale_percent = 100  # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        #print('Resized Dimensions of frame : ', resized.shape)

        # Convert to grayscale
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        face_rects = face_cascade.detectMultiScale(gray, 1.5, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in face_rects:
       	    cv2.rectangle(resized, (x, y), (x+w, y+h), (255, 0, 0), 2)
       	    break

        # Encode the resized image
        ret, jpeg = cv2.imencode('.jpg', resized)
        return jpeg.tobytes()
