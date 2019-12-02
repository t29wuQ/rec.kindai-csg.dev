import cv2
import base64
import threading
from flask import Flask, request, render_template
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from record import recording_save_img

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
            with open('./latest.jpg', 'rb') as f:
                ws.send(base64.b64encode(f.read()).decode('ascii'))

def main():
    record_thread = threading.Thread(target=recording_save_img, args=(capture,))
    record_thread.start()
    app.debug = True
    server = pywsgi.WSGIServer(("", 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
    


if __name__ == '__main__':
    main()
