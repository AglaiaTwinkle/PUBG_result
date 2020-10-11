import cv2
import glob
import numpy as np
import os
from copy import copy
np.set_printoptions(threshold=np.inf)

class Image:
  def __init__(self, image, file_name):
    self.image = image
    self.file_name = file_name

  def convert2Gray(self):
    self.image = 0.299 * self.image[:, :, 2] + 0.587 * self.image[:, :, 1] + 0.114 * self.image[:, :, 0]

  def ajustGrayScale(self, border):
    self.image[self.image <= border] = 0
    self.image[self.image > border] = 255


def load_images(image_path = "result_image/"):
  images = []
  image_files_path = glob.glob(image_path+"*")
  for file_path in image_files_path:
    image = cv2.imread(file_path)
    file_name = os.path.basename(file_path)
    images.append(Image(image, file_name))
  return images

def convert2Gray(images):
  if type(images) == list:
    [image.convert2Gray() for image in images]
  elif type(images) == Image:
    images.convert2Gray()
  else:
    print("convert2Gray(): error")

def ajustGrayScale(images, border):
  if type(images) == list:
    [image.ajustGrayScale(border) for image in images]
  elif type(images) == Image:
    images.ajustGrayScale(border)
  else:
    print("ajustGrayScale(): error")

def outputImage(images, output_path = "output/"):
  if type(images) == list:
    for image in images:
      cv2.imwrite(output_path + image.file_name, image.image)
  elif type(images) == Image:
    cv2.imwrite(output_path + images.file_name, images.image)
  else:
    print("outputImage(): error")

def main():
  images = load_images()
  image_origin = images[0]
  for i in range(25):
    image = copy(image_origin)
    image.file_name = str(i) + ".png"
    convert2Gray(image)
    ajustGrayScale(image, i*10)
    outputImage(image)

main()