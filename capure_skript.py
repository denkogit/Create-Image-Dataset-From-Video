import cv2
import os
from PIL import Image
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--video_path', required=True, metavar='',help='Path to target video')
args = parser.parse_args()


(dirname, filename) = os.path.split(args.video_path)

IMAGE_OUTPUT = os.path.join(dirname, 'output_images')


if not os.path.exists(IMAGE_OUTPUT):
    os.mkdir(IMAGE_OUTPUT)
    print('folder has been created')



print('Script is working ... '+ IMAGE_OUTPUT)

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
            
            image_pillow.save(IMAGE_OUTPUT + '/image' + str(currentframe) + '.jpg')

            print('Creating... ' + str(currentframe))
       
        currentframe += 1
    else:
        break

cv2.destroyAllWindows()