from flask import Flask, render_template, Response
from video import VideoCamera

app = Flask(__name__)


@app.route('/')
# Render to html file
def index():
    return render_template('index.html')

# Function to convert the encoded image back


def gen(video):
    while True:
        frame = video.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/live_video_feed')
# Route the LIVE video feed to http response for webpage
def live_video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
