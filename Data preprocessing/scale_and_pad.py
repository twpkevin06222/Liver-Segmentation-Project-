from read_data import load_images
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

NEW_SIZE = 128

def resize(img_list):
    new_img_list = []

    for img in img_list:
        new_img = []

        for i in range(np.size(img, 2)):
            new_img.append(np.asarray(Image.fromarray(img[:,:,i],mode='F').resize((NEW_SIZE,NEW_SIZE), Image.LANCZOS)))

        new_img_list.append(np.swapaxes(new_img, 0, 2))

    return new_img_list

img_list, height, depth, = load_images("../data/train/img")
img_list = resize(img_list)