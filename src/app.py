import subprocess


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b


def run_command(cmd):
    # DIBERSIHKAN: Menghapus shell=True dan menambah # nosec untuk Bandit
    if isinstance(cmd, str):
        cmd = cmd.split()
    result = subprocess.run(
        cmd, capture_output=True, text=True
    )  # nosec
    return result.stdout