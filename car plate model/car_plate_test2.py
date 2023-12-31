# -*- coding: utf-8 -*-
"""car plate test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gdam0u_gigit0C2mKLtYOZCy8t2Vokn1
"""

# Commented out IPython magic to ensure Python compatibility.
#clone YOLOv5 and
!git clone https://github.com/ultralytics/yolov5  # clone repo
# %cd yolov5
# %pip install -qr requirements.txt # install dependencies
# %pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

import torch

model = torch.hub.load('.', 'custom', path='/content/best.pt', source='local')
# Image
images = '/content/images/'
# Inference
for img in os.listdir(images):
    # check if the image ends with png
    results = model(images + img)
    results.show()
# Results, change the flowing to: results.show()
 # or .show(), .save(), .crop(), .pandas(), etc