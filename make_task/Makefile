
#creating virtual environment
create_venv:
	python3 -m venv myenv

#installing dependencies
install_deps: check_requires
	myenv/bin/pip install mypy
	myenv/bin/pip install -r requirements.txt

#launch the app
app:
	myenv/bin/python3 main.py

check_requires:
	myenv/bin/python3 check_deps.py

typecheck:
	myenv/bin/mypy calc.py