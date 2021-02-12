import os
import datetime
import reportlab

proj_folder = os.getcwd() + '/supplier-data/images/'


def generate_report(path):
    files = os.listdir(path)
    pdf = ''
    for file in files:
        if file.endswith('.txt'):
            with open(path + file, 'r') as f:
                text = f.read().splitlines()
        pdf += 'name: ' + text[0] + '<br/>' + 'weight: ' + text[1] + '<br/><br/>'
    return pdf
