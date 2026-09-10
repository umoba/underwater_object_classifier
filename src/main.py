# import cv2 as cv

# from image_utils import (
#     resize_image,
#     adjust_brightness,
#     blur_image,
#     add_underwater_cast,
#     simulate_turbidity, 
#     random_augmentation
# )


# image_path = "data/raw/test1.jpg"

# image = cv.imread(image_path)

# if image is None:
#     raise FileNotFoundError(
#         f"Could not find image: {image_path}"
#     )


# print("Original shape:", image.shape)


# resized = resize_image(image)

# brighter = adjust_brightness(
#     resized,
#     value=40
# )

# blurred = blur_image(
#     resized,
#     kernel_size=7
# )

# underwater = add_underwater_cast(
#     resized
# )


# cv.imwrite(
#     "outputs/resized.jpg",
#     resized
# )

# cv.imwrite(
#     "outputs/brighter.jpg",
#     brighter
# )

# cv.imwrite(
#     "outputs/blurred.jpg",
#     blurred
# )

# cv.imwrite(
#     "outputs/underwater.jpg",
#     underwater
# )

# turbid = simulate_turbidity(
#     resized,
#     blur_amount=7,
#     haze_strength=0.15,
#     contrast=0.75,
# )

# cv.imwrite(
#     "outputs/turbid.jpg",
#     turbid
# )

# for i in range(5):
#     augmented = random_augmentation(resized)
#     output_path = f"outputs/augmented_{i}.jpg"

#     cv.imwrite(output_path, augmented)

#     print(f"Saved {output_path}")




# print("Finished processing images.")


# TEST CASE

import cv2

from dataset import ImageDataset
from image_utils import resize_image, random_augmentation


dataset = ImageDataset("data/raw")

print("Number of images:", len(dataset))


for index in range(len(dataset)):

    image = dataset[index]

    print(
        f"Image {index}: "
        f"shape={image.shape}"
    )

    resized = resize_image(image)

    augmented = random_augmentation(resized)

    output_path = (
        f"outputs/image_{index}_augmented.jpg"
    )

    cv2.imwrite(
        output_path,
        augmented
    )

    print(f"Saved: {output_path}")