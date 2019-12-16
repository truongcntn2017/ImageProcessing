
import numpy as np
import cv2
import matplotlib.pyplot as plt

class ColorTransformer:
    def calHistogram(self):
      try:
        image_shape = self.image.shape 
        hist = np.array([0]*256)

        for x in range(image_shape[0]):
          for y in range(image_shape[1]):
            if len(image_shape) == 3:
              hist[int(self.image[x,y,0])] += 1
            else:
              hist[int(self.image[x,y])] += 1

        return hist
      except EOFError as e:
        raise(e)

    def calCumsum(self):
        try:
            cumsum = np.array([0]*256)
            cumsum[0] = self.hist[0]
            for i in range(1,256):
                cumsum[i] = cumsum[i-1] + self.hist[i]

            return cumsum
        except EOFError as e:
            raise(e)

    def plotHistogram(self):
        try:
            x = np.array([0]*len(self.hist))
            figure = plt.plot(self.hist)
        except EOFError as e:
            raise(e)

    def increase_brightness(self, increasing_value= 10):#load rgb image
        try:
            hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            hue, saturation, value = cv2.split(hsv)

            lim = 255 - increasing_value
            value[value > lim] = 255
            value[value <= lim] += increasing_value

            final_hsv = cv2.merge((hue, saturation, value))
            image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
            return image
        except EOFError as e:
            raise(e)

    def increase_constrast(self):#load rgb image
        try:
            hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
            hue, saturation, value = cv2.split(hsv)

            k = int(255/np.max(value))
            value *= k

            final_hsv = cv2.merge((hue, saturation, value))
            image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
            return image
        except EOFError as e:
            raise(e)

    def max_min_normalize(self, cumsum):
        try:
            cumsum = (cumsum - cumsum.min())*255 / (cumsum.max() - cumsum.min())
            return cumsum.astype('uint8')
        except EOFError as e:
            raise(e)

    def histogram_equalization(self):
        self.hist = self.calHistogram()
        cumsum = self.calCumsum()
        cumsum = self.max_min_normalize(cumsum)

        return cumsum[image]

    def color_transform(self):
        try:
            if self.mode == 1:
                return self.increase_brightness()
            elif self.mode == 2:
                return self.increase_constrast()
            else:
                return self.histogram_equalization()
        except EOFError as e:
            raise(e)

    def __init__(self, image: np.ndarray, mode: int in [1, 2, 3]):
        """
        image: np.ndarray
        mode: type of color transformer 1-increase bright, 2-increase contrast, 3- histogram equalization
        """
        self.image = image
        self.mode = mode
        self.result = self.color_transform()







