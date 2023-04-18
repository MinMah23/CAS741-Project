# Define variables
PYTHON = python3
PIP = pip3
PROJECT_DIR = CAS741-Project/src

# Define targets
.PHONY: setup run test clean

# Install project dependencies
setup:
    $(PIP) install -r $(PROJECT_DIR)/requirements.txt

# Run the project
run:
    $(PYTHON) $(PROJECT_DIR)/mainM.py

# Run tests using pytest
test:
    $(PYTHON) -m pytest CAS741-Project/test/

# Clean up any temporary files
clean:
    rm -rf $CAS741-Project/__pycache__/
