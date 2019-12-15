from PIL import Image
import matplotlib.image as mpimg 
import cv2


def read_image(path, mode: int in [1,2,3]):
    """
        path: image in directory;
        mode: [1, 3], 1 read by cv2, 2 read by mpimg, 3 read by image of pillow;
        return numpy type
    """
    try: 
        with open(path) as f:
            if mode == 1:
                img = cv2.imread(path)
            elif mode == 2:
                img = mpimg.imread(path)
            elif mode == 3:
                img = Image.open(path)
    except EOFError as e:
        raise(e)
    return img


def write_image(path, mode: int in [1,2,3], img):
    """
        path: image in directory,
        mode: [1, 3], 1 write by cv2, 2 write by mpimg, 3 write by image of pillow
        return numpy type
    """
    try:
      if mode == 1:
        cv2.imwrite(path, img)
      elif mode == 2:
        mpimg.imsave(path, img)
      else:
        img.save(path)
    except EOFError as e:
      raise(e)

# Testing

if __name__ == "__main__":
    pass
#     img = read_image('../data/test.png', 1)
#     write_image('../data/test-1.png',1, img)
    
