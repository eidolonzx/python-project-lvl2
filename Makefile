install:
	poetry install

run:
	poetry run gendiff file1.json file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

renew:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl --force-reinstall

lint:
	poetry run flake8 gendiff