from gendiff.generate_diff import generate_diff
import os


def test_generate_diff():
    result = generate_diff('./files/file1.json', './files/file2.json')
    with open('./tests/fixtures/result.json') as f:
        assert result == f.read()
