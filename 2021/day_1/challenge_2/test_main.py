import sys
from unittest.mock import patch

from main import main


def test_sum():
    numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    with open("test.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

    with patch.object(sys, "argv", ["main.py", "test.txt"]):
        count = main()
        assert count == 5
