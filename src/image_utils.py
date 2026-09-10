import cv2 as cv
import numpy as np

def resize_image(image, width=128, height=128):
    return cv.resize(image, (width, height))


def adjust_brightness(image, value=40):
    result = image.astype(np.int16)

    result = result + value

    result = np.clip(result, 0, 255)

    return result.astype(np.uint8)


def blur_image(image, kernel_size=7):
    return cv.GaussianBlur(
        image,
        (kernel_size, kernel_size),
        0
    )


def add_underwater_cast(image):
    result = image.astype(np.float32)

    # OpenCV stores color channels as BGR
    result[:, :, 0] *= 1.50
    result[:, :, 1] *= 1.10
    result[:, :, 2] *= 0.3

    result = np.clip(result, 0, 255)

    return result.astype(np.uint8)

def simulate_turbidity(
    image,
    blur_amount=7,
    haze_strength=0.20,
    contrast=0.80,
):
    """
    Simulate reduced underwater visibility.

    Parameters:
        image: OpenCV BGR image
        blur_amount: Gaussian blur kernel size
        haze_strength: strength of blue-green haze
        contrast: contrast multiplier
    """

    # Work with floating point numbers while doing arithmetic
    result = image.astype(np.float32)

    # 1. Reduce contrast
    mean = np.mean(result, axis=(0, 1), keepdims=True)

    result = mean + contrast * (result - mean)

    # 2. Add blue-green underwater haze
    haze_color = np.array(
        [170, 150, 80],       # BGR
        dtype=np.float32
    )

    result = (
        (1.0 - haze_strength) * result
        + haze_strength * haze_color
    )

    # 3. Keep pixel values valid
    result = np.clip(result, 0, 255)

    result = result.astype(np.uint8)

    # 4. Slightly blur the image
    result = cv.GaussianBlur(
        result,
        (blur_amount, blur_amount),
        0
    )

    return result


def random_augmentation(image):
    """
    Apply randomized underwater-style augmentation.
    """

    # Random brightness change
    brightness = np.random.randint(-30, 31)

    # Random blur: must be an odd number
    blur_amount = int(np.random.choice([3, 5, 7, 9]))

    # Random haze strength
    haze_strength = np.random.uniform(0.05, 0.35)

    # Random contrast
    contrast = np.random.uniform(0.65, 1.0)

    result = adjust_brightness(
        image,
        value=brightness
    )

    result = simulate_turbidity(
        result,
        blur_amount=blur_amount,
        haze_strength=haze_strength,
        contrast=contrast
    )

    return result