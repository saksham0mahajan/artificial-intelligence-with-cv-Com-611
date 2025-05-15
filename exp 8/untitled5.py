import cv2
import numpy as np #for shapes
from google.colab.patches import cv2_imshow #for image display



def convert_to_grayscale(image_path):
  #load the image
  image = cv2.imread(image_path)

  #convert to grayscale
  grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  #display the original and grayscale
  print("Original Image:")
  cv2_imshow(image)

  print("Grayscale Image:")
  cv2_imshow(grayscale_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()




def convert_to_bgr(image_path, output_path):
  #load the image
  image = cv2.imread(image_path)

  #convert to BGR
  bgr_image = cv2.cvtColor(image, cv2.COLOR_BAYER_BGR2GRAY)

  #display the orig ans grayscale images
  print("Original Image:")
  cv2_imshow(image)

  print("BGR Image:")
  cv2_imshow(bgr_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  #save the bgr image
  cv2.imwrite(output_path, bgr_image)
  print("BGR image saved as", output_path)

def convert_bgr_to_rgb(output_path):
  #load the image
  image = cv2.imread(output_path)

  #convert to RGB
  rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  print("BGR Image:")
  cv2_imshow(image)

  print("RGB Image:")
  cv2_imshow(rgb_image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

image_path="OIP.jpeg"
output_path="output_bgr.jpg"

convert_to_grayscale(image_path)

convert_bgr_to_rgb("OIP.jpeg")



