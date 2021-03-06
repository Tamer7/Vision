import requests
import json
import cv2
import base64


address_url = 'http://192.168.1.6:5000'

test_url = address_url + '/v1/api/predict'
print(test_url)

# prepare headers for http request
content_type = 'application/json'
headers = {'content-type': content_type}
folderName = 'user_images/'
fileName = 'animal.jpg'
img = cv2.imread(folderName+fileName)

# Here we encode the image to a .jpg
_, img_buffer = cv2.imencode('.jpg', img)

img_as_string = base64.b64encode(img_buffer)

# send http request with image and receive response
payload = {
    "image" : (img_as_string).decode("utf-8"),  # Convert bytes to string
    "name" : fileName
}

payload = json.dumps(payload)
loaded_payload = json.loads(payload)

response = requests.post(test_url,'',json=loaded_payload)
print (response.json())

