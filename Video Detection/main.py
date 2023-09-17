import cv2
import numpy as np
import os
import pyautogui
import sys
import time

thres = 0.45			# Threshold to detect object
nms_threshold = 0.2		# Threshold of non maximum supression

camera_input = False
screen_input = False
files_input = False

# we make the file working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))



# ANSI escape codes for text formatting and colors
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
CLEAR_LINE = "\033[K"

def list_files_in_folder(folder_path):
	files = os.listdir(folder_path)
	return files

def display_file_list(files):
	print(f"{BOLD}{WHITE}\nFiles in the folder:{RESET}\n")
	for i, file_name in enumerate(files, start=1):
		print(f"{BOLD}{CYAN}{i}. {file_name}{RESET}")

def read_file_content(file_path):
	with open(file_path, 'r') as file:
		return file.read()


def select_file_from_list(files):
	while True:
		try:
			choice = int(input(f"{BOLD}{YELLOW}\nEnter the number of the file you want to use (0 to go back): {RESET}"))
			if choice == 0:
				return None
			elif 1 <= choice <= len(files):
				selected_file = files[choice - 1]
				print(f"\nYou selected: {BOLD}{GREEN}{selected_file}{RESET}")
				return selected_file
			else:
				print(f"{RED}Invalid choice. Please enter a valid number.{RESET}")
		except ValueError:
			print(f"{RED}Invalid input. Please enter a valid file number.{RESET}")


def cleanUp():
	# Specify the directory where you want to delete the files
	directory_path = './'  # Replace with your directory path

	# List all files in the directory
	files_in_directory = os.listdir(directory_path)
	for filename in files_in_directory:
			if filename.startswith('.screen'):
				file_path = os.path.join(directory_path, filename)
				try:
					os.remove(file_path)
				except OSError as e:
					print(f"Error deleting file {file_path}: {e}")



while True:
	os.system('clear')

	print("""
   █████████                                                 █████
  ███░░░░░███                                               ░░███
 ███     ░░░   ██████  █████████████   ████████  █████ ████ ███████    ██████  ████████
░███          ███░░███░░███░░███░░███ ░░███░░███░░███ ░███ ░░░███░    ███░░███░░███░░███
░███         ░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███   ░███    ░███████  ░███ ░░░
░░███     ███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███   ░███ ███░███░░░   ░███
 ░░█████████ ░░██████  █████░███ █████ ░███████  ░░████████  ░░█████ ░░██████  █████
  ░░░░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░███░░░    ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░
                                       ░███
                                       █████
                                      ░░░░░
 █████   █████  ███           ███
░░███   ░░███  ░░░           ░░░
 ░███    ░███  ████   █████  ████   ██████  ████████
 ░███    ░███ ░░███  ███░░  ░░███  ███░░███░░███░░███
 ░░███   ███   ░███ ░░█████  ░███ ░███ ░███ ░███ ░███
  ░░░█████░    ░███  ░░░░███ ░███ ░███ ░███ ░███ ░███
    ░░███      █████ ██████  █████░░██████  ████ █████
     ░░░      ░░░░░ ░░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░
      """)

	print(f"{BOLD}{YELLOW}Select data source:")
	print("1. Input File")
	print("2. Camera Capture")
	print("3. Screen Capture")
	print(f"0. Exit{RESET}")

	try:
		choice = int(input(f"\n{BOLD}{WHITE}Enter your choice: "))
		if choice == 0:
			print(f"\n{BOLD}{WHITE}Exiting...")
			sys.exit()
		elif choice == 1:
			folder_path = "./Input"  # Replace with the actual path to your folder
			files = list_files_in_folder(folder_path)
			display_file_list(files)
			selected_file = select_file_from_list(files)
			time.sleep(2)
			files_input = True
			break
		elif choice == 2:
			camera_input = True
			break
		elif choice == 3:
			screen_input = True
			break
		else:
			print(f"{RED}Invalid choice. Please enter a valid number.{RESET}")
	except ValueError:
		os.system('clear')
		print(f"{RED}Invalid input. Please enter a valid choice.{RESET}")
		time.sleep(1)



# Create a named window with the desired dimensions
window_name = "Object Detection"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)  # WINDOW_NORMAL allows resizing

# Set the desired window dimensions (width, height)
output_width = 1600
output_height = 900
cv2.resizeWindow(window_name, output_width, output_height)

# Set the desired window position (x, y)
window_x = 100
window_y = 100
cv2.moveWindow(window_name, window_x, window_y)


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

if camera_input:
	# Create a VideoCapture object with screen dimensions
	cap = cv2.VideoCapture(0)
elif files_input:
	# Reads a video file
	cap = cv2.VideoCapture('./Input/'+selected_file)


while True:
	if screen_input:
		# Initialize the screen dimensions
		screen_width, screen_height = pyautogui.size()
		# Capture a screenshot of the entire screen
		screenshot = pyautogui.screenshot()
		img = np.array(screenshot)
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	else:
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

	# iterating over every object detetcted and rendering a box with it's name
	for i in indices:
		box = bbox[i]
		x,y,w,h = box[0],box[1],box[2],box[3]
		cv2.rectangle(img, (x,y),(x+w,h+y), color=(0, 255, 0), thickness=2)
		cv2.putText(img,classNames[classIds[i]-1].upper(),(box[0]+10,box[1]+30),
		cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
		cv2.putText(img,str(round(confs[i]*100,2)),(box[0]+200,box[1]+30),
		cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

	cv2.imshow(window_name,img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

if not screen_input:
	cap.release()
cleanUp()
cv2.destroyAllWindows()
