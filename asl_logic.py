import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

# Initialize the hand detector and classifier
detector = HandDetector(maxHands=1)  # Detect only one hand
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")  # Ensure the path is correct

# Constants for image resizing and processing
offset = 20
img_size = 300

# Labels for ASL gestures (ensure these match your model's output)
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
          "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "Del"]

def prediction(frame):
    # Copy the frame for output (optional, can remove if not needed)
    img_output = frame.copy()

    # Detect hands in the frame
    hands, img = detector.findHands(frame)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # Bounding box of the hand

        # Create a white background image to fit the hand gesture
        img_white = np.ones((img_size, img_size, 3), np.uint8) * 255
        img_crop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        # Determine aspect ratio of the cropped hand image
        aspect_ratio = h / w

        if aspect_ratio > 1:  # Height > Width
            k = img_size / h
            w_cal = math.ceil(k * w)
            img_resize = cv2.resize(img_crop, (w_cal, img_size))
            w_gap = math.ceil((img_size - w_cal) / 2)
            img_white[:, w_gap:w_cal + w_gap] = img_resize
        else:  # Width > Height
            k = img_size / w
            h_cal = math.ceil(k * h)
            img_resize = cv2.resize(img_crop, (img_size, h_cal))
            h_gap = math.ceil((img_size - h_cal) / 2)
            img_white[h_gap:h_cal + h_gap, :] = img_resize

        # Use the classifier to predict the ASL gesture from the processed image
        try:
            prediction, index = classifier.getPrediction(img_white, draw=False)
            print(f"Prediction: {prediction}, Index: {index}")  # Logging prediction
        except Exception as e:
            print(f"Error during prediction: {e}")
            return ""

        # Return the predicted alphabet based on the index
        return labels[index]

    # If no hands are detected, return an empty string
    return ""