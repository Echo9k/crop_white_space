import argparse
import multiprocessing
from utils import find_images
from image_processing import process_image

# set up logging
import logging
logging.basicConfig(level=logging.INFO)

# log cwd
import os
logging.info(f"Current working directory: {os.getcwd()}")

# ---------------- Functions ----------------


def process_images(input_folder, output_folder, config_path, save_interim, num_processes):
    image_paths = find_images(input_folder)
    logging.info(f"Found {len(image_paths)} images in {input_folder}")
    for image_path in image_paths:
        # Add loggs
        print(f"Processing {image_path}")
        logging.info(f"Processing {image_path}")
        process_image(image_path, output_folder, config_path, save_interim)

# ---------------- Main ----------------


if __name__ == "__main__":
    # get config
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_folder", type=str, default="data/input")
    parser.add_argument("-o", "--output_folder", type=str, default="data/output")
    parser.add_argument("-c", "--config_path", type=str, default="config/config.yaml")
    parser.add_argument("-s", "--save_interim", type=bool, default=False)
    parser.add_argument("-n", "--num_processes", type=int, default=1)
    args = parser.parse_args()

    # assert the existence of input folder
    assert os.path.exists(args.input_folder), f"Input folder {args.input_folder} does not exist"

    # assert the existence of config file
    assert os.path.exists(args.config_path), f"Config file {args.config_path} does not exist"

    # assert the existence of output folder
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
        logging.info(f"Created output folder {args.output_folder}")

    # check the number of processes
    if args.num_processes < 1:
        logging.warning(f"Number of processes must be at least 1, got {args.num_processes}")
        args.num_processes = 1
    # validate that the environment has the required number of processes
    if args.num_processes > multiprocessing.cpu_count():
        logging.warning(f"Number of processes ({args.num_processes}) exceeds the number of CPU cores ({multiprocessing.cpu_count()})")
        args.num_processes = multiprocessing.cpu_count()

    process_images(input_folder=args.input_folder,
         output_folder=args.output_folder,
         config_path=args.config_path,
         save_interim=args.save_interim,
         num_processes=args.num_processes)