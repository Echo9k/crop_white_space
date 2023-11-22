import logging
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

from utils import find_images
from image_processing import process_image


def process_image_wrapper(args):
    return process_image(*args)


def process_images(input_folder, output_folder, config_path, save_interim, num_processes):
    image_paths = find_images(input_folder)
    logging.info(f"Found {len(image_paths)} images in {input_folder}")

    # Prepare arguments for each image processing task
    tasks = [(image_path, output_folder, config_path, save_interim) for image_path in image_paths]

    # Process images in parallel
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Using tqdm for progress bar
        results = list(tqdm(executor.map(process_image_wrapper, tasks), total=len(tasks)))