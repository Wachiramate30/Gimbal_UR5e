import cv2
import paho.mqtt.client as mqtt
import base64

# MQTT broker settings
broker_address = "mqtt-dashboard.com"  # Change this to your MQTT broker's address
topic = "webcam_feed"

# Capture webcam feed
# cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
cap = cv2.VideoCapture(1)

# MQTT client setup
client = mqtt.Client()
client.connect(broker_address)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading webcam feed")
        break
    frame = cv2.resize(frame,(640,480))
    # frame = frame[0:320,:]

    # Convert frame to base64 string
    _, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')

    # Publish frame to MQTT topic
    client.publish(topic, jpg_as_text)

# Release resources
cap.release()
client.disconnect()
