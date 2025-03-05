import pytest


class TestForLoopStartEnd:
        
    def test_input_from_user_01(self):

        with open("actual01.txt") as actual_output:
            actual = ''
            for line in actual_output:
                actual += line.strip() + '\n'

        with open("expected01.txt") as expected_output:
            expected = ''
            for line in expected_output:
                expected += line.strip() + '\n'

        assert actual.strip() == expected.strip()            

