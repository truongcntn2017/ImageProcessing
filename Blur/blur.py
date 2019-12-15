import numpy as np
import cv2

from Convolution import convolution
from utils import prepare_data

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
    self.blur_image = Convolution(self.kernel, self.image)

if __name__ == '__main__':
    temp = Blur('../data/lena.png', 2)
    cv2.show(temp)
    
