install:
	python3 -m pip install --upgrade pip &&\
		python3 -m pip install -r src/subtitle_renamer/requirements.txt

format:
	black src/subtitle_renamer/*.py

test:
	python3 -m pytest -v src/subtitle_renamer/tests/tests.py

lint:

build:
	python3 -m build

all:
	make install test lint