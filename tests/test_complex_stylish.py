from gendiff.engine import generate_diff
from gendiff.render import render_diff_result


def test_complex_json_comparison():
    filepath1 = 'tests/fixtures/file1_complex.json'
    filepath2 = 'tests/fixtures/file2_complex.json'
    result_file = open('tests/fixtures/result_stylish_complex.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2)
    assert render_diff_result(diff_result, 'stylish') == result_output

def test_complex_yaml_comparison():
    filepath1 = 'tests/fixtures/file1_complex.yaml'
    filepath2 = 'tests/fixtures/file2_complex.yaml'
    result_file = open('tests/fixtures/result_stylish_complex.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2)
    assert render_diff_result(diff_result, 'stylish') == result_output

# def test_plain_json_comparison():
#    filepath1 = 'tests/fixtures/file1_complex.json'
#    filepath2 = 'tests/fixtures/file2_complex.json'
#    result_file = open('tests/fixtures/result_plain_complex.txt', 'r')
#    result_output = result_file.read()
#
#    diff_result = generate_diff(filepath1, filepath2)
#    assert render_diff_result(diff_result, 'plain') == result_output