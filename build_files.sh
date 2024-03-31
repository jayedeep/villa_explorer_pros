#!/bin/bash
apt install libsqlite3-dev sqlite
# Check if pip is installed for Python 3.9
if ! command -v python3.9 &> /dev/null; then
    echo "Python 3.9 is not installed. Please install Python 3.9 and try again."
    exit 1
fi

if ! python3.9 -m pip --version &> /dev/null; then
    echo "Installing pip for Python 3.9..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.9 get-pip.py --user
fi

# Update PATH to include user's bin directory where pip installs packages
export PATH="$HOME/.local/bin:$PATH"

python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run collectstatic using Python 3.9
python3.9 manage.py collectstatic
