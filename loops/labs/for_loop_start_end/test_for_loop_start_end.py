import pytest

class TestInput:
        
    def test_input_from_file(self):

        with open("actual.txt") as actual_output:
            actual = ''
            for line in actual_output:
                actual += line.strip() + '\n'

        with open("expected.txt") as expected_output:
            expected = ''
            for line in expected_output:
                expected += line.strip() + '\n'

        assert actual.strip() == expected.strip()            

