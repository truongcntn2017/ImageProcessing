from PIL import Image
import matplotlib.image as mpimg 
import cv2


def read_image(path, mode: int):
    """
        This function is read image from path
        Read by cv2 has parameters: path, mode = 1
        Read by matplotlib has parameters: path, mode = 2
        Read by pillow has parameters: path, mode = 3
    """
    try: 
        with open(path) as f:
            if mode == 1:
                img = cv2.imread(path)
            elif mode == 2:
                img = mpimg.imread(path)
            elif mode == 3:
                img = Image.open(path)
            else:
                img = None
        return img
    except EOFError as e:
        raise(e)


def write_image(path, mode: int, img):
    """
        This function is read image from path
        Read by cv2 has parameters: path, mode = 1
        Read by matplotlib has parameters: path, mode = 2
        Read by pillow has parameters: path, mode = 3
    """
    try:
      if mode == 1:
        cv2.imwrite(path, img)
      elif mode == 2:
        mpimg.imsave(path, img)
      elif mode == 3:
        img.save(path)
      else:
         pass
    except EOFError as e:
      raise(e)

# Testing
if __name__ == "__main__":
    # print("Read image from data directory")
    # img = read_image('../data/test.png', 1)
    # print("Write image into data directory")
    # write_image('../data/test-1.png',1, img)
    pass
    
