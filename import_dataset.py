import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("paultimothymooney/chest-xray-pneumonia")
print(path)