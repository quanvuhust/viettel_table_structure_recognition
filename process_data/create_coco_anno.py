import json, cv2, numpy as np, itertools, random, pandas as pd
from skimage import io
import matplotlib.pyplot as plt
from pathlib import Path
from tqdm.auto import tqdm
from sklearn import model_selection
from copy import deepcopy
import cv2
import os
import json


coco_data = {"info": {}, "licenses": [], "categories": [], "images": [], "annotations": []}

categories = ["cell"]
coco_data["categories"].append({"id": 0, "name": "cell"})
index = 0
for root, dirs, files in os.walk("train"):
    for file in files:
        if ".json" in file:
            file_path = os.path.join(root, file)
            image_id = file.replace(".json", "")
            f = open(file_path)
            data = json.load(f)
            image = cv2.imread(os.path.join("train", image_id + ".jpg"))
            h, w, _ = image.shape
            for cell in data:
                class_id = 0
                class_name = "cell"
                bbox = cell["coordinate"]
                x_min,y_min,x_max,y_max = bbox[0], bbox[1], bbox[2], bbox[3]
                image_info = {"id": image_id, "file_name": image_id + ".jpg", "height": h, "width": w}
                
                coco_data["images"].append(image_info)
                annotation_info = {
                    "id": index,
                    "image_id": image_id,
                    "category_id": class_id,
                    "bbox": [int(x_min), int(y_min), int(x_max - x_min), int(y_max - y_min)],
                    "bbox_mode": 1,
                    "iscrowd": 0,
                    "area": int(x_max - x_min)*int(y_max - y_min),
                }
                index += 1
                coco_data["annotations"].append(annotation_info)
            f.close()

output_file_path = "train.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    json.dump(coco_data, output_file, ensure_ascii=True, indent=4)