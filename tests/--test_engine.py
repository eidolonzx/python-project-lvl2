from gendiff.generate_diff import generate_diff


def test_engine_with_simple_files():
    filepath1 = 'tests/fixtures/file1.json'
    filepath2 = 'tests/fixtures/file2.json'
    result = [
        {
            'key': 'follow',
            'status': 'removed',
            'value': False
        }, {
            'key': 'host',
            'status': 'not modified',
            'value': 'hexlet.io'
        }, {
            'key': 'proxy',
            'status': 'removed',
            'value': '123.234.53.22'
        }, {
            'key': 'timeout',
            'status': 'modified',
            'value': 20,
            'old value': 50
        }, {
            'key': 'verbose',
            'status': 'added',
            'value': True
        }
    ]

    assert generate_diff(filepath1, filepath2) == result


def test_engine_with_complex_files():
    filepath1 = 'tests/fixtures/file1_complex.json'
    filepath2 = 'tests/fixtures/file2_complex.json'
    result = [
        {
            'key': 'common',
            'status': 'parent modified',
            'value': [{
                'key': 'follow',
                'status': 'added',
                'value': False
            }, {
                'key': 'setting1',
                'status': 'not modified',
                'value': 'Value 1'
            }, {
                'key': 'setting2',
                'status': 'removed',
                'value': 200
            }, {
                'key': 'setting3',
                'status': 'modified',
                'value': None,
                'old value': True
            }, {
                'key': 'setting4',
                'status': 'added',
                'value': 'blah blah'
            }, {
                'key': 'setting5',
                'status': 'added',
                'value': [{
                    'key': 'key5',
                    'status': 'not modified',
                    'value': 'value5'
                }]
            }, {
                'key': 'setting6',
                'status': 'parent modified',
                'value': [{
                    'key': 'doge',
                    'status': 'parent modified',
                    'value': [{
                        'key': 'wow',
                        'status': 'modified',
                        'value': 'so much',
                        'old value': ''
                    }]
                }, {
                    'key': 'key',
                    'status': 'not modified',
                    'value': 'value'
                }, {
                    'key': 'ops',
                    'status': 'added',
                    'value': 'vops'
                }]
            }]
        }, {
            'key': 'group1',
            'status': 'parent modified',
            'value': [{
                'key': 'baz',
                'status': 'modified',
                'value': 'bars',
                'old value': 'bas'
            }, {
                'key': 'foo',
                'status': 'not modified',
                'value': 'bar'
            }, {
                'key': 'nest',
                'status': 'modified',
                'value': 'str',
                'old value': [{
                    'key': 'key',
                    'status': 'not modified',
                    'value': 'value'
                }]
            }]
        }, {
            'key': 'group2',
            'status': 'removed',
            'value': [{
                'key': 'abc',
                'status': 'not modified',
                'value': 12345
            }, {
                'key': 'deep',
                'status': 'not modified',
                'value': [{
                    'key': 'id',
                    'status': 'not modified',
                    'value': 45
                }]
            }]
        }, {
            'key': 'group3',
            'status': 'added',
            'value': [{
                'key': 'deep',
                'status': 'not modified',
                'value': [{
                    'key': 'id',
                    'status': 'not modified',
                    'value': [{
                        'key': 'number',
                        'status': 'not modified',
                        'value': 45
                    }]
                }]
            }, {
                'key': 'fee',
                'status': 'not modified',
                'value': 100500
            }]
        }
    ]

    assert generate_diff(filepath1, filepath2) == result
    