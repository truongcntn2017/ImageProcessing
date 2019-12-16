import numpy as np
import cv2
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.prepare_data import read_image
from Convolution.convolution import Convolution

DIR_PATH = os.path.join(os.path.dirname(__file__), '..')

def gauss2D(shape=(3,3),sigma= 3):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m, n = [(ss-1.)/2. for ss in shape]
    y, x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

class Blur:
  def makeKernel(self, mode: int in [1, 2]):
    if mode == 1:
      kernel = np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]) /9
    else:
      kernel = np.array(gauss2D())
    
    return kernel

  def __init__(self, path, mode: int in [1, 2]):
    """
      path: where is image in directory,
      mode: 1 (mean blur), 2 (gaussian blur)
    """
    self.kernel = self.makeKernel(mode)
    self.image = read_image(path, 1)
    self.blur_image = Convolution(self.kernel, self.image).image

if __name__ == '__main__':
    # image = Blur(os.path.join(DIR_PATH+'/data/lena.png'), 1)

    # cv2.imshow('blur_image',image.blur_image)
    # cv2.waitKey(0)
    pass
    
