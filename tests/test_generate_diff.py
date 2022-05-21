from gendiff.generate_diff import generate_diff
import os


def test_generate_diff_json():
    result = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    with open('./tests/fixtures/result.txt') as f:
        assert result == f.read()

def test_generate_diff_yaml():
    result = generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.yaml')
    with open('./tests/fixtures/result.txt') as f:
        assert result == f.read()

def test_generate_diff_unsopported():
    result = generate_diff('./tests/fixtures/file1.yml', './tests/fixtures/file2.json')
    assert result == 'File extension is not supported'

def test_generate_diff_json_tree():
    result = generate_diff('./tests/fixtures/file1-v2.json', './tests/fixtures/file2-v2.json')
    with open('./tests/fixtures/result2.txt') as f:
        assert result == f.read()

def test_generate_diff_yaml_tree():
    result = generate_diff('./tests/fixtures/file1-v2.yml', './tests/fixtures/file2-v2.yaml')
    with open('./tests/fixtures/result2.txt') as f:
        assert result == f.read()