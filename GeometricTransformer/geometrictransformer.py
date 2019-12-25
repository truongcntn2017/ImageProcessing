import matplotlib.pyplot as plt
import numpy as np
import string
import cv2
import os.path
import sys

DIR_PATH = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(DIR_PATH)

from utils.prepare_data import read_image, write_image

class GeometricMatrix:
  """
   Geometric matrix is class that can make rotation matrix, translation matrix, scale matrix
   Rotation matrix has parameters: mode = 1, angle = ?
   Translation matrix has parameters: mode = 2, x = ?, y = ?
   Scale matrix matrix has parameters: mode = 3, scale = ?
   Result: items properties 
  """
  def get_rotation(self, angle):
    try:
      angle = np.radians(angle)
      return np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    except EOFError as e:
      raise(e)

  def get_translation(self, dx, dy):
    try:
      return np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
    except EOFError as e:
      raise(e)

  def get_scale(self, scale):
    try:
      return np.array([[scale, 0, 0], [0, scale, 0], [0, 0, 1]])
    except EOFError as e:
      raise(e)

  def get_matrix(self):
    try:
      if self.mode == 1:
        return self.get_rotation(self.args[0])
      elif self.mode == 2:
        return self.get_translation(self.args[0], self.args[1])
      elif self.mode == 3:
        return self.get_scale(self.args[0])
      else:
        return None
    except EOFError as e:
      raise(e)


  def __init__(self, mode: int, **kwargs):
    self.mode = mode
    self.args = [x for x in kwargs.values()]
    self.items = self.get_matrix()

  def __repr__(self):
    strings = str(self.items)
    return strings

  def __eq__(self, other):
    return self.items == other.items

  def __gt__(self, other):
    return self.items < other.items

  def __ge__(self, other):
    return self.items >= other.items


class GeometricTransformation:
  """
  Geometric transformation is class that can transform by a matrix
  Transform has parameters: image, matrix
  Result: items properties
  """
  def init_shape(self):
    shape = np.zeros(3,dtype=int)
    matrix = abs(self.matrix)

    shape[0] = int(matrix[0][0]*self.image.shape[0]) if matrix[0][0] > matrix[0][1] else int(matrix[0][1]*self.image.shape[1])
    shape[1] = int(matrix[1][1]*self.image.shape[1]) if matrix[1][1] > matrix[1][0] else int(matrix[1][0]*self.image.shape[0])
    shape[2] = self.image.shape[2]

    return shape

  def nearest_neighbors(self, i, j):
    try:
      x_max, y_max = self.image.shape[0] - 1, self.image.shape[1] - 1
      x, y, _ = self.inv_matrix @ np.array([i, j, 1])
      x = int(np.floor(x))
      y = int(np.floor(y))

      if x == x_max:
        x -= 1
    
      if y == y_max:
        y -= 1

      return (self.image[x, y,:]/4 + self.image[x + 1, y, :]/4 + self.image[x, y + 1,:]/4 + self.image[x + 1, y + 1,:]/4)
    except EOFError as e:
      raise(e)

  def transform(self):
    try:
      shape = self.init_shape()
      self.items = np.zeros(shape, dtype='float32')

      for i, row in enumerate(self.items):
        for j, col in enumerate(row):
          self.items[i, j, :] = self.nearest_neighbors(i, j)

      return self.items
    except EOFError as e:
      raise(e)

  def __init__(self, image, matrix):
    self.image = image
    self.matrix = matrix
    self.inv_matrix = np.linalg.inv(self.matrix)
    self.items = self.transform()

  def __repr__(self):
    strings = str(self.items)
    return strings

if __name__ == '__main__':
    print('Read image from data direcstory')
    image = read_image(os.path.join(DIR_PATH+'/data/lena.png'), 1)

    print('Rotation angle = 90')
    image_tranformed = GeometricTransformation(image, GeometricMatrix(1, angle=90).items).items
    write_image(os.path.join(DIR_PATH+'/data/rotation-90.png'), 1, image_tranformed)

    print('Scale x2')
    image_tranformed = GeometricTransformation(image, GeometricMatrix(3, scale = 2).items).items
    write_image(os.path.join(DIR_PATH+'/data/scale-2.png'), 1, image_tranformed)

    pass
