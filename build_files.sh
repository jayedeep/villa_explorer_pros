#!/bin/bash

# Install pip (if needed)
if ! command -v pip &> /dev/null; then
  # Replace 'python3' with the appropriate command for your Python version
  get-pip.py https://pypi.org/project/pip/
fi

pip install -r requirements.txt
python3.9 manage.py collectstatic