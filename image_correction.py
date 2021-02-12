import os
from PIL import Image

proj_folder = os.getcwd() + '/images/'
pic_full_path, names, pic_num = [], [], 0

for path in os.listdir(proj_folder):
    if '48dp' in path:
        pic_num += 1
        pic_full_path.append(proj_folder + path)
        names.append(path)


def imageProcess(pic_dir, path_tosave, name):
    pic = Image.open(pic_dir)
    pic = pic.rotate(90).resize((128, 128)).convert('RGB')
    pic.save(path_tosave + name, 'jpeg')
    return


if __name__ == '__main__':
    for (pic_dir, name) in zip(pic_full_path, names):
        imageProcess(pic_dir, '/opt/icons/', name)