import numpy as np
import time
import cv2
import os
import machine_learning_model.Object_detection.color as color


def load_label(labelpath):
    # In this function, we are loading the COCO class lables the yolo model was trained on..
    labels = open(labelpath).read().strip().split("\n")
    
    # Here we are initialzing a list of colors to represent each class label
    np.random.seed(42)
    
    colors = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
    return labels, colors


def load_image(imagepath):
    image = cv2.imread(imagepath)
    return image


def load_model():
    # Loading our yolo object detector trained on the COCO dataset
    
    # Printing the information for debugging...
    print("[INFO] loading YOLO from disk...")
    
    net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "/Users/tamerjar/Desktop/Vision/Backend/AI/machine_learning_model/Object_detection/yolov3.weights")
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    print("Done")
    return net, ln


def detectObjectFromImage(image, net, ln):
    
    # Here we construct a blob from the image and perfrom a forward pass
    # of the object detector, which in turn gives us a bounding box and
    # the probabilty
    
    H, W = image.shape[:2]
    blob = cv2.dnn.blobFromImage(
        image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    
    boxes = []
    confidences = []
    classIDs = []
    centers = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.5:
                box = detection[0:4]*np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype('int')

                x = int(centerX - width/2)
                y = int(centerY - height/2)
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
                centers.append((centerX, centerY))
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)
    return idxs, boxes, confidences, centers, classIDs


def print_text(idxs, classids, labels):
    texts = []
    if len(idxs) > 0:
        for i in idxs.flatten():
            texts.append(labels[classids[i]])
    return texts

def bouding_box(idxs, image, boxes, colors, labels, classIDs, confiences):
    H, W = image.shape[:2]
    objectPropertyList = []
    if len(idxs) > 0:
        for i in idxs.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            colorr = [int(c) for c in colors[classIDs[i]]]
            cv2.rectangle(image, (x, y), (x + w, y + h), colorr, 2)
            text = labels[classIDs[i]]
            confience = confiences[i]
            im = image[y:y+h, x:x+w]
            c = color.get_color(im)
  
            objectPropertyList.append({
                "text": text,
                "confidence": confience,
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "color": c
            })

    return objectPropertyList


