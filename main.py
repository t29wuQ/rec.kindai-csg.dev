import cv2
import base64
from flask import Flask, request, render_template
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
capture = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            ret, frame = capture.read()
            cv2.imwrite('latest.jpg', frame)
            result, encimg = cv2.imencode('.jpg', frame, encode_param)
            ws.send(base64.b64encode(encimg).decode('ascii'))

def main():
    app.debug = True
    server = pywsgi.WSGIServer(("", 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
