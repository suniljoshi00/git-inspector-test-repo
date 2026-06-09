import subprocess


def charge_card(card_number, amount):
    command = f"echo Charging {amount} to card {card_number}"
    return subprocess.check_output(command, shell=True).decode("utf-8")
