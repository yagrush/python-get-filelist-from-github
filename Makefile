venv-start:
	python -m venv .venv
	chmod 777 .venv/bin/activate
	source ./.venv/bin/activate

pip-install:
	pip install -r requirements.txt

run:
	python -m src

pip-freeze:
	pip freeze > requirements.txt
