import glob
import os
import json

os.chdir('/Users/soejimakengo/Desktop/UmamusuQuiz/kiritori2/')

index = 0
file_list = sorted(glob.glob('*.png'))
data = {}
for i in range(len(file_list)):
    data[i+1] = {
        "image": file_list[i],
        "name": ""
    }

os.chdir('/Users/soejimakengo/Desktop/UmamusuQuiz/')
name_json = open('name2.json', 'w')
json.dump(data, name_json, indent=2)
