import numpy as np 

class Convolution:
  def convolution_point(self, x: int, y: int, z: int):
    """
    """
    kernel_shape = self.kernel.shape
    result = 0.0

    for x_kernel in range(kernel_shape[0]):
      for y_kernel in range(kernel_shape[1]):
        result += self.kernel[x_kernel,y_kernel]*self.image[x + x_kernel,y + y_kernel,z]
  
    return result

  def convolution(self):
    kernel_shape = self.kernel.shape
    image_shape = self.image.shape
    result = []

    for x in range(image_shape[0] - kernel_shape[0]):
      for y in range(image_shape[1] - kernel_shape[1]):
        for z in range(image_shape[2]):
          result.append(self.convolution_point(x,y,z))

    length = kernel_shape[0]*kernel_shape[1]
    result = np.array(result)
    result = result.reshape(image_shape[0] - kernel_shape[0], image_shape[1] - kernel_shape[1], image_shape[2])

    return result

  def __init__(self, kernel: np.ndarray, image: np.ndarray):
    self.kernel = kernel
    self.image = image
    self.items = self.convolution()

if __name__ == '__main__':
  pass