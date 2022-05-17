from gendiff.generate_diff import generate_diff
import os


def test_generate_diff_json():
    result = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    with open('./tests/fixtures/result.json') as f:
        assert result == f.read()

def test_generate_diff_yaml():
    result = generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yaml')
    with open('./tests/fixtures/result.yml') as f:
        assert result == f.read()