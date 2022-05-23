from gendiff.engine import generate_diff
from gendiff.render import render_diff_result


def test_plain_yml_comparison():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    result_file = open('tests/fixtures/result_stylish.txt', 'r')
    result_output = result_file.read()

    assert render_diff_result(generate_diff(filepath1, filepath2), 'stylish') == result_output


def test_plain_yaml_comparison():
    filepath1 = 'tests/fixtures/file1.yaml'
    filepath2 = 'tests/fixtures/file2.yaml'
    result_file = open('tests/fixtures/result_stylish.txt', 'r')
    result_output = result_file.read()

    assert render_diff_result(generate_diff(filepath1, filepath2), 'stylish') == result_output