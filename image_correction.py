#!/usr/bin/env python3
import os
from PIL import Image

proj_folder = os.getcwd() + '/supplier-data/images/'
pic_full_path, names, = [], []

for path in os.listdir(proj_folder):
    if '.tiff' in path:
        pic_full_path.append(proj_folder + path)
        names.append(path.replace('.tiff', '.jpeg'))


def imageProcess(pic_dir, path_tosave, name):
    pic = Image.open(pic_dir)
    pic = pic.resize((600, 400)).convert('RGB')
    pic.save(path_tosave + name)
    return


if __name__ == '__main__':
    for (pic_dir, name) in zip(pic_full_path, names):
        imageProcess(pic_dir, proj_folder, name)