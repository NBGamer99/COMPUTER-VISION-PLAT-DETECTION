# importing Open-cv
import cv2
import numpy as np
from matplotlib import pyplot as plt
# imutils to make basic image processing functions such as translation, rotation, resizing
import imutils
import os

# we make the file working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Defining  Marr Hildreth edge detection
def edgesMarrHildreth(img, sigma):
	size = int(2*(np.ceil(3*sigma))+1)
	x, y = np.meshgrid(np.arange(-size/2+1, size/2+1), np.arange(-size/2+1, size/2+1))

	normal = 1 / (2.0 * np.pi * sigma**2)

	kernel = ((x**2 + y**2 - (2.0*sigma**2)) / sigma**4) * np.exp(-(x**2+y**2) / (2.0*sigma**2)) / normal  # LoG filter

	kern_size = kernel.shape[0]
	log = np.zeros_like(img, dtype=float)

	# applying filter
	for i in range(img.shape[0]-(kern_size-1)):
		for j in range(img.shape[1]-(kern_size-1)):
			window = img[i:i+kern_size, j:j+kern_size] * kernel
			log[i, j] = np.sum(window)

	log = log.astype(np.int64, copy=False)

	zero_crossing = np.zeros_like(log)

	# computing zero crossing
	for i in range(log.shape[0]-(kern_size-1)):
		for j in range(log.shape[1]-(kern_size-1)):
			if log[i][j] == 0:
				if (log[i][j-1] < 0 and log[i][j+1] > 0) or (log[i][j-1] < 0 and log[i][j+1] < 0) or (log[i-1][j] < 0 and log[i+1][j] > 0) or (log[i-1][j] > 0 and log[i+1][j] < 0):
					zero_crossing[i][j] = 255
			if log[i][j] < 0:
				if (log[i][j-1] > 0) or (log[i][j+1] > 0) or (log[i-1][j] > 0) or (log[i+1][j] > 0):
					zero_crossing[i][j] = 255
	return sigma*2, zero_crossing


# we pass our desired image to be processed
img = cv2.imread('./input/image3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction

# we test over all sigma values until we get the extracted plates
for i in np.arange(0.5, 3, 0.1): # use of np.arange for float stepping
	fg_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	gray2 = cv2.cvtColor(fg_rgb, cv2.COLOR_RGB2GRAY)
	edged2 = edgesMarrHildreth(gray2, i)
	log = edged2[1].astype(np.uint8)
	plt.imshow(cv2.cvtColor(edged2, cv2.COLOR_BGR2RGB))
	plt.imshow(edged2[1], cmap='gray')


	# find contours
	keypoints = cv2.findContours(log.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = imutils.grab_contours(keypoints)
	contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]


	location = None
	found = 0
	for contour in contours:
		# we try to find a polygone with 4 vertices (quadrilateral)
		approx = cv2.approxPolyDP(contour, 10, True)
		if len(approx) == 4:
			location = approx
			found = 1
			break

	if found == 0:
		pass
	else:
		#if found, we extract our image and store it in in the output folder
		mask = np.zeros(gray.shape, np.uint8)
		new_image = cv2.drawContours(mask, [location], 0,255, -1)
		new_image = cv2.bitwise_and(img, img, mask=mask)

		(x,y) = np.where(mask==255)
		(x1, y1) = (np.min(x), np.min(y))
		(x2, y2) = (np.max(x), np.max(y))
		cropped_image = gray[x1:x2+1, y1:y2+1]
		cv2.imwrite(f"output/img{i}.jpg",cropped_image)
