Crop White Space Project
==============================

This project focuses on processing images to automatically crop white spaces. It provides a convenient way to batch process images with parallel execution capabilities.

Project Organization
------------

    ├──.idea               <- IDE-specific configurations and inspection profiles.
    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │    ├── interim        <- Intermediate data that has been transformed.
    │    ├── processed      <- The final, canonical data sets for modeling.
    │    └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-expl    oration`.
    │
    ├── references         <- Manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── config.py      <- Configuration settings and parameters.
    │   ├── image_processing.py  <- Functions for image processing.
    │   ├── crop_white_space.py        <- Main script to run the project.
    │   └── parallel_execution.py  <- Module for parallel execution.
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Setup

Before you begin, ensure you have Python installed on your system. This project is developed and tested with Python 3.8+. You can download and install Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/your-username/crop-white-space.git
cd crop-white-space
```

### Install Dependencies

It's recommended to create a virtual environment before installing dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

Modify the `src/config.py` to set the parameters for image processing as per your requirement. This includes setting thresholds, kernel sizes, and other image processing related configurations.

## Usage

### Running the Script

To process images, navigate to the `src/scripts/` directory and execute the `crop_white_space.py` script. Use the following command:

```bash
python crop_white_space.py -i ../data/raw/ -o ../data/ -c ../config.json
```

Replace the paths as needed:
- `-i`: Path to the input folder containing raw images.
- `-o`: Path to the output folder where processed images will be saved.
- `-c`: Path to the configuration file.

### Experimenting with Notebooks

The `notebooks/` directory contains Jupyter notebooks for experimental and exploratory analysis. To use these notebooks:

1. Ensure Jupyter is installed:

   ```bash
   pip install jupyter
   ```

2. Start the Jupyter Notebook server:

   ```bash
   jupyter notebook
   ```

3. Navigate to the `notebooks/` directory in the Jupyter Notebook interface in your browser.

4. Open a notebook and run the cells to experiment.

## Contributing

Contributions to this project are welcome. Please feel free to submit issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE.txt).