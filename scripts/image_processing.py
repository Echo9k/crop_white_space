import cv2
import numpy as np
import os
from pathlib import Path
from utils import show_or_save_image
from config import read_config


def otsus_thresholding(gray_image, min_threshold=0, max_threshold=255, **kwargs):
    _, thresholded = cv2.threshold(gray_image, min_threshold, max_threshold, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded


def canny_edge_detection(image, threshold1=100, threshold2=200, **kwargs):
    return cv2.Canny(image, threshold1, threshold2)


def find_contour_bounds(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        combined_contour = np.vstack(contours).squeeze()
        x, y, w, h = cv2.boundingRect(combined_contour)
        return x, y, x+w, y+h
    return None


def morphological_operations(image, kernel_size=5, **kwargs):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)


def process_image(image_path, output_folder, config_path, save_interim):
    config = read_config(config_path)

    # Extract parameters from config
    otsu_params = config.get('otsu', {})
    canny_params = config.get('canny', {})
    morph_params = config.get('morphological_operations', {})

    path_interim = str(Path(output_folder).joinpath("interim"))
    path_processed = str(Path(output_folder).joinpath("processed"))
    Path(path_interim).mkdir(parents=True, exist_ok=True)
    Path(path_processed).mkdir(parents=True, exist_ok=True)
    interim_filename = f"{Path(image_path).stem}_interim.png"
    processed_filename = f"{Path(image_path).stem}_processed.png"

    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding
    otsu_thresh = otsus_thresholding(gray, **otsu_params)
    if save_interim:
        show_or_save_image(otsu_thresh, "Otsu Threshold", path=path_interim, filename=interim_filename)

    # Optionally apply morphological operations
    morphed = morphological_operations(otsu_thresh, **morph_params)
    if save_interim:
        show_or_save_image(morphed, "Morphological Operations", path=path_interim, filename=interim_filename)

    # Canny edge detection
    edges = canny_edge_detection(morphed, **canny_params)
    if save_interim:
        show_or_save_image(edges, "Canny Edges", path=path_interim, filename=interim_filename)

    if contour_bounds := find_contour_bounds(edges):
        x1, y1, x2, y2 = contour_bounds
        cropped_image = image[y1:y2, x1:x2]
        if save_interim:
            show_or_save_image(cropped_image, "Cropped Image", path=path_interim, filename=interim_filename)

        # Save the final cropped image
        cv2.imwrite(os.path.join(path_processed, processed_filename), cropped_image)
    else:
        print(f"No significant contours found in {image_path}.")
