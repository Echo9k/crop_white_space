from PIL import Image

def crop_whitespace(image):
    """
    Crop whitespace from an image.

    :param image: Image object
    :return: Cropped Image object
    """
    bbox = image.getbbox()
    if bbox:
        return image.crop(bbox)
    return image  # Return original if no whitespace detected

def process_image(image):
    """
    Process a single image (wrapper function for all processing steps).

    :param image: Image object
    :return: Processed Image object
    """
    return crop_whitespace(image)
