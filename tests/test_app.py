import pytest
from src.app import add, divide, run_command


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_run_command():
    output = run_command("echo hello")
    assert "hello" in output