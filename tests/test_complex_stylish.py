from gendiff.generate_diff import generate_diff


def test_complex_json_to_stylish():
    filepath1 = 'tests/fixtures/file1_complex.json'
    filepath2 = 'tests/fixtures/file2_complex.json'
    result_file = open('tests/fixtures/result_stylish_complex.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2, 'stylish')

    assert diff_result == result_output


def test_complex_yaml_to_stylish():
    filepath1 = 'tests/fixtures/file1_complex.yaml'
    filepath2 = 'tests/fixtures/file2_complex.yaml'
    result_file = open('tests/fixtures/result_stylish_complex.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2, 'stylish')

    assert diff_result == result_output
