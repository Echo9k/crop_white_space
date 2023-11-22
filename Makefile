.PHONY: setup run notebooks clean

# Define the default target
all: setup run

# Setup the project
setup:
	python -m venv venv
	@echo "Activating virtual environment..."
	source venv/bin/activate
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run the main script
run:
	@echo "Running the crop_white_space script..."
	python ./scripts/crop_white_space.py -i data/raw/ -o data/processed/ -c config/config.json

# Start Jupyter Notebook for experimenting
notebooks:
	@echo "Starting Jupyter Notebook..."
	jupyter notebook

# Clean up the environment
clean:
	@echo "Cleaning up..."
	rm -rf venv
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Help command
help:
	@echo "Available commands:"
	@echo "   setup      - Set up the project (create venv and install dependencies)"
	@echo "   run        - Run the main script"
	@echo "   notebooks  - Start Jupyter Notebook"
	@echo "   clean      - Clean up the project (remove venv and caches)"
	@echo "   help       - Show this help message"
