from gendiff.engine import generate_diff


def test_plain_yml_comparison():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    result_file = open('tests/fixtures/result.txt', 'r')
    result_output = result_file.read()

    assert generate_diff(filepath1, filepath2, 'yaml') == result_output


def test_plain_yaml_comparison():
    filepath1 = 'tests/fixtures/file1.yaml'
    filepath2 = 'tests/fixtures/file2.yaml'
    result_file = open('tests/fixtures/result.txt', 'r')
    result_output = result_file.read()

    assert generate_diff(filepath1, filepath2, 'yaml') == result_output