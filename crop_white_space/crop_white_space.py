import argparse
from src.utils import find_images
from src.parallel_executor import execute_in_parallel
from src.image_processing import process_image


def main(input_folder, output_folder, config_path, save_interim, num_processes):
    image_paths = find_images(input_folder)
    tasks = [(path, output_folder, config_path, save_interim) for path in image_paths]
    execute_in_parallel(lambda args: process_image(*args), tasks, num_processes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process images in a folder")
    parser.add_argument('input_folder', type=str, help="Input folder containing images")
    parser.add_argument('output_folder', type=str, help="Output folder for processed images")
    parser.add_argument('config_path', type=str, help="Path to the configuration file")
    parser.add_argument('--save_interim', action='store_true', help="Flag to save interim images")
    parser.add_argument('--processes', type=int, default=None, help="Number of processes to use")

    args = parser.parse_args()
    main(args.input_folder, args.output_folder, args.config_path, args.save_interim, args.processes)

# python process_images.py /path/to/input /path/to/output /path/to/config.json --save_interim --processes 4
