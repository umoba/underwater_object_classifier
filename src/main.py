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