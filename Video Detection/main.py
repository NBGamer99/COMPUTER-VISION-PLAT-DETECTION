import cv2
import numpy as np
import os
thres = 0.45			# Threshold to detect object
nms_threshold = 0.2		# Threshold of non maximum supression

# we make the file working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# change this corresponding to your camera usually it's 0 for your main one
cap = cv2.VideoCapture(0)

# if you want to read only an image
# img = cv2.imread('./img.webp')
# cap.set(3,1280) # set parameters (window width)
# cap.set(4,720)  # (window height)
# cap.set(10,150) # (increase brightness)

# reading class name or name of objects to detect from a file
classNames= []
classFile = './coco.names'
with open(classFile,'rt') as f:
	classNames = f.read().rstrip('\n').split('\n')

# loading our data file models
"""
The . pb format is the protocol buffer (protobuf) format, and in Tensorflow, this
format is used to hold models. Protobufs are a general way to store data by Google
that is much nicer to transport, as it compacts the data more efficiently and enforces
a structure to the data.
"""
configPath = './ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = './frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
	success,img = cap.read()
	classIds, confs, bbox = net.detect(img,confThreshold=thres)
	bbox = list(bbox)
	confs = list(np.array(confs).reshape(1,-1)[0])
	confs = list(map(float,confs))

	"""
	Non Maximum Suppression (NMS) is a technique used in numerous
	computer vision tasks. It is a class of algorithms to select
	one entity (e.g., bounding boxes) out of many overlapping entities.
	We can choose the selection criteria to arrive at the desired results.
	"""
	indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
	# print("indices", indices)

	# iterating over every object detetcted and rendering a box with it's name
	for i in indices:
		box = bbox[i]
		x,y,w,h = box[0],box[1],box[2],box[3]
		cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)
		cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),
		cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
		cv2.putText(img,str(round(confs[i]*100,2)),(box[0]+200,box[1]+30),
		cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

	cv2.imshow("Output",img)
	cv2.waitKey(1)
