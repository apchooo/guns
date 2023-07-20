import io
from PIL import Image
from ultralytics import YOLO
from flask import Flask, request, jsonify

app = Flask(__name__)
model = YOLO("saved_weights/train14_3cl_340ep.pt")  # load a pretrained YOLOv8s weights

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image'].read()
    image = Image.open(io.BytesIO(file))
    results = model.predict(source=image, classes=[0,2], conf=0.75)
    humans = 0
    guns = 0
    for res in results:
        boxes = res.boxes
        for box in boxes:
            if int(box.cls[0]) == 0:
                humans += 1
            elif int(box.cls[0]) == 2:
                guns += 1
    response = {"guns": guns, "humans": humans}
    return jsonify(response)
