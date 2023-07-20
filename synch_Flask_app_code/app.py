import io
from PIL import Image
from ultralytics import YOLO
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the YOLOv8 model
model = YOLO("saved_weights/train14_3cl_340ep.pt")  # load a pretrained YOLOv8s weights

@app.route('/detect', methods=['POST'])
def detect():
    # Get the image from the POST request
    file = request.files['image'].read()

    # Load the image into a PIL Image object
    image = Image.open(io.BytesIO(file))

    # Run the image through the YOLOv8 model
    results = model.predict(source=image, classes=[0,2], conf=0.75)  # classes=[0,2], conf=0.75, stream=True, save=True
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

    # Return the result as a JSON-encoded string
    return jsonify(response)

if __name__ == '__main__':
    app.run()