from flask import Flask, render_template, Response, jsonify
import cv2  # OpenCV for camera input
import asl_logic  # Your ASL detection logic module

app = Flask(__name__)

# Initialize camera
camera = cv2.VideoCapture(0)

# Global variable to hold the current predicted alphabet
current_prediction = ""

def generate_frames():
    global current_prediction
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Process the frame for gesture detection
        current_prediction = asl_logic.prediction(frame)  # Ensure this returns a string

        # Convert frame to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/predict', methods=['GET'])
def predict():
    global current_prediction  # Ensure you are referencing the global variable
    return jsonify({"prediction": current_prediction})



@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)  # Change host and port as needed
    finally:
        camera.release()  # Release the camera when done