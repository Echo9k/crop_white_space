from PIL import Image
import os


def load_images(directory):
    """
    Load all images from the specified directory.

    :param directory: str, path to the directory containing images
    :return: list of Image objects
    """
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(directory, filename)
            try:
                images.append(Image.open(img_path))
            except IOError as e:
                print(f"Error loading image {filename}: {e}")
    return images


def save_image(image, directory, filename):
    """
    Save an image to the specified directory with the given filename.

    :param image: Image object
    :param directory: str, path to the save directory
    :param filename: str, name to save the file as
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    save_path = os.path.join(directory, filename)
    image.save(save_path)
