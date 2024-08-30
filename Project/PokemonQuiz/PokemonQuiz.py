import sys
import random
import glob
import os
import json
import matplotlib.pyplot as plt
import cv2

rand = random.randint(1,151)

try:
    with open('name.json','r') as f:
        jsn = json.load(f)

    with open('answer.json','r') as f1:
        jsn2 = json.load(f1)
except FileNotFoundError:
    print('File not found.')
    sys.exit(1)


try:
    image_file = jsn[str(rand)]['image']
except KeyError:
    print('Key not found.')
    sys.exit(1)

img_path = os.path.join('/Users/soejimakengo/Desktop/PokemonQuiz/kiritori/',image_file)
img = cv2.imread(img_path)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)

question = input("誰かわかりますか？:")

try:
    image_file2 = jsn2[str(rand)]['image2']
except KeyError:
    print('Key not found.')
    sys.exit(1)

img2_path = os.path.join('/Users/soejimakengo/Desktop/PokemonQuiz/images/',image_file2)
img2 = cv2.imread(img2_path)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)

if question == jsn[str(rand)]['name']:
    print('正解です！')


else:
    print('不正解です！')
    print('正解は', jsn[str(rand)]['name'], 'です。')
   
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image2', img2)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break