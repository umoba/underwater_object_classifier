import cv2 as cv
import numpy as np

print ("Hello World")
print ("OpenCV version:", cv.__version__)
print ("Numpy version:", np.__version__)

image_path = "data/raw/test.jpg"

output_path = "outputs/resized.jpg"

image = cv.imread(image_path)

if image is None: 
  raise FileNotFoundError(f"Could not found image: {image_path}")

print("Original Shape:", image.shape)
print("Data Type:", image.dtype)


# Resize iamge
resized = cv.resize(image, (128, 128))

print("Resized shape:", resized.shape)


# Output
success = cv.imwrite(output_path, resized)

if not success:
    raise RuntimeError(f"Could not save image: {output_path}")

print(f"Saved resized image to: {output_path}")




