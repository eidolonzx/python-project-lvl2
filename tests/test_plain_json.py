from gendiff.engine import generate_diff
from gendiff.render import render_diff_result


def test_plain_json_comparison():
    filepath1 = 'tests/fixtures/file1.json'
    filepath2 = 'tests/fixtures/file2.json'
    result_file = open('tests/fixtures/result.txt', 'r')
    result_output = result_file.read()

    assert render_diff_result(generate_diff(filepath1, filepath2, 'json')) == result_output
    