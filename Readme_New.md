pip freeze

python3 -m venv .pytest
py -m pip install -r requirements.txt

virtualenv venv
pip freeze > requirements.txt
pip install -r requirements.txt