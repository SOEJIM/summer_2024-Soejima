import cv2
import os

import_path = '/Users/soejimakengo/Desktop/UmamusuQuiz/images2'
export_path = '/Users/soejimakengo/Desktop/UmamusuQuiz/kiritori2'

for filename in os.listdir(import_path):
    file_path = os.path.join(import_path, filename)
    if os.path.isfile(file_path):
        img = cv2.imread(file_path)
        if img is None:
            print('Image file is not found.')
            continue

        imgCropped = img[100:200, 140:240]

        new_filename = filename.replace('.png','_kiritori.png')
        image_export_path = os.path.join(export_path, new_filename)
        cv2.imwrite(image_export_path, imgCropped)

