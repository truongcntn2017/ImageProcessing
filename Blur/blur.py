import numpy as np
import cv2
import os.path
import sys

DIR_PATH = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(DIR_PATH)

from utils.prepare_data import read_image, write_image
from Convolution.convolution import Convolution

def gauss2D(shape=(3,3),sigma= 3):
    """
    2D gaussian mask
    fspecial('gaussian',[shape],[sigma])
    """
    try:
      m, n = [(x - 1.) / 2. for x in shape]
      y, x = np.ogrid[-m:m+1,-n:n+1]

      height = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
      height[ height < np.finfo(height.dtype).eps*height.max() ] = 0

      sum_height = np.sum(height)
      if sum_height != 0:
        height /= sum_height

      return height
    except EOFError as e:
      raise(e)

class Blur:
  """
  Blur is class that can blur image
  Mean blur has parameters: mode = 1
  Gaussian blur has parameters: mode = 2
  """
  def makeKernel(self, mode: int):
    try:
      if mode == 1:
        kernel = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]) /9
      elif mode == 2:
        kernel = np.array(gauss2D())
      else:
        kernel = None

      return kernel
    except EOFError as e:
      raise(e)

  def __init__(self, image, mode: int in [1, 2]):
    """
      path: where is image in directory,
      mode: 1 (mean blur), 2 (gaussian blur)
    """
    self.kernel = self.makeKernel(mode)
    self.image = image
    self.items = Convolution(self.kernel, self.image).items

if __name__ == '__main__':
    print("Read image from path")
    image = read_image(os.path.join(DIR_PATH+'/data/lena.png'), 1)
    blur_image = Blur(image, 1).items
    print("Write blur image")
    write_image(os.path.join(DIR_PATH+'/data/blur-lena.png'), 1, blur_image)
    pass
    
