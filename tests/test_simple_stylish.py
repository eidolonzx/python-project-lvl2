from gendiff.generate_diff import generate_diff


def test_simple_json_to_stylish():
    filepath1 = 'tests/fixtures/file1.json'
    filepath2 = 'tests/fixtures/file2.json'
    result_file = open('tests/fixtures/result_stylish.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2, 'stylish')
    
    assert diff_result == result_output


def test_simple_yaml_to_stylish():
    filepath1 = 'tests/fixtures/file1.yaml'
    filepath2 = 'tests/fixtures/file2.yaml'
    result_file = open('tests/fixtures/result_stylish.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2, 'stylish')
    
    assert diff_result == result_output

def test_simple_yml_to_stylish():
    filepath1 = 'tests/fixtures/file1.yml'
    filepath2 = 'tests/fixtures/file2.yml'
    result_file = open('tests/fixtures/result_stylish.txt', 'r')
    result_output = result_file.read()

    diff_result = generate_diff(filepath1, filepath2, 'stylish')
    
    assert diff_result == result_output
