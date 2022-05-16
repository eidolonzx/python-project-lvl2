from gendiff.engine import generate_diff
from gendiff.render import render_diff_result


def test_complex_json_comparison():
    filepath1 = 'tests/fixtures/file1_complex.json'
    filepath2 = 'tests/fixtures/file2_complex.json'
    result_file = open('tests/fixtures/result_complex.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2, 'json')
    print(diff_result)
    assert render_diff_result(diff_result) == result_output
    