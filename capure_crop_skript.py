import cv2
import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--video_path', required=True, metavar='',help='Path to target video')
args = parser.parse_args()

# extract video file folder path
(dirname, filename) = os.path.split(args.video_path)

image_output = os.path.join(dirname, 'croped_images')

# create output dir
if not os.path.exists(image_output):
    os.mkdir(image_output)
    print('folder has been created')


data_left = os.path.join(image_output, 'data_left')
data_right = os.path.join(image_output, 'data_right')


# create folders fro separated images
if not os.path.exists(data_left):
    os.mkdir(data_left)

if not os.path.exists(data_right):
    os.mkdir(data_right)


print('Script is working ...')
print(data_left)
print(data_right)


cam = cv2.VideoCapture(args.video_path)
currentframe = 0

while(True):
    # reading from frame

    ret, frame = cam.read()
    height, width, channels = frame.shape

    if ret:
        # writing the extracted images and crop
        if currentframe % 30 == 0:
            # capture the image
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_pillow = Image.fromarray(img)
            
            #define crop area 
            img_left_area = (0, 0, width/2, height)
            img_right_area = (width/2, 0, width, height)
            
            #crop image for two equal parts  
            img_left = image_pillow.crop(img_left_area)
            img_right = image_pillow.crop(img_right_area)
            
            #save images to directory
            img_left.save(data_left + '/leftimage' + str(currentframe) + '.jpg')
            img_right.save(data_right + '/rightimage' + str(currentframe) + '.jpg')

            print('Creating... ' + str(currentframe))
       
        currentframe += 1
    else:
        break

cv2.destroyAllWindows()