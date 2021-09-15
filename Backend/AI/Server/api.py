efrom flask import Flask, request, Response, send_file
import machine_learning_model.Object_detection.yoloModel as yoloModel
import jsonpickle
import numpy as np
import cv2
import base64
import json
import ast
import requests
app = Flask(__name__)


url_base = 'http://192.168.1.6:5000'
predict_image_api = '/v1/api/predict'
bounding_box_API = '/v1/resoures/predict_images/'


# Load YOLO model
labels, colors = yoloModel.load_label("coco.names")
net, ln = yoloModel.load_model()


# route http posts to this method
@app.route(predict_image_api, methods=['GET', 'POST'])
def predict():
    loaded_body = parse_json_from_request(request)
    
    # Conversion of base64 image back to its binary
    img_original = base64.b64decode(loaded_body['image'])

    # Conversion of image data to unit8
    jpg_as_np = np.frombuffer(img_original, dtype=np.uint8)
    
    # Decoding the image
    image = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)

    idxs, boxes, confiences, centers, classIDs = yoloModel.detectObjectFromImage(image, net, ln)

    objectProperty = yoloModel.bouding_box(idxs, image, boxes, colors, labels, classIDs, confiences)

    response = {
        'objectProperty':''
    }
    response['objectProperty'] = objectProperty
    print(response)
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)



    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route(bounding_box_API+'<name>', methods=['GET'])
def get_image(name):
    filename = 'predict_images/output_resize_%s.jpg' % name
    print(filename)
    return send_file(filename, mimetype='image/gif')


def parse_json_from_request(request):
    body_dict = request.json
    body_str = json.dumps(body_dict)
    loaded_body = ast.literal_eval(body_str)
    return loaded_body

if __name__ == "__main__":
    # start flask app
    app.run()
