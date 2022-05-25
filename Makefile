install:
	poetry install

run:
	poetry run gendiff --format json tests/fixtures/file1_complex.json tests/fixtures/file2_complex.json

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

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml