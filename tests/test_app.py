import pytest
from src.app import add, divide, run_command

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

def test_run_command_tidak_bisa_injection():
    # Karakter ';' diperlakukan sebagai string murni, bukan perintah shell baru
    output = run_command("echo aman; echo BERBAHAYA")
    assert output.strip() == "aman; echo BERBAHAYA"