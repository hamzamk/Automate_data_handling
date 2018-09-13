import os
from PIL import Image
from os.path import basename

def main():
    folder_name = 'train'#name of the folder containing images
    path = '{}/{}'.format(os.getcwd(), folder_name)
    extension = 'xml' #extensions to be ignored

    def conversion(image):
        base = os.path.basename(image)
        image_file = Image.open('{}/{}'.format(path, image))
        image_file.convert('RGB').save('{}.jpg'.format(os.path.splitext(base)[0]))


    list_of_images = []
    for filename in os.listdir(path):
        if filename.endswith(extension):
            pass
        else:
            list_of_images.append(filename)
            conversion(filename)


if __name__ == '__main__':
    main()
