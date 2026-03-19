create-structure:
	mkdir src tests docs
	touch README.md setup.py requirments.txt
	touch docs/DOMAIN.md
	touch src/.gitkeep tests/.gitkeep


install-dep:
	pip install -r requirments.txt

install:
	pip install -e .

test-pytest:
	python3 -m pytest

test: install-dep install-e test-pytest