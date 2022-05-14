install:
	poetry install

run:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

renew:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl