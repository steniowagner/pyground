import os
import subprocess


def clear_terminal():
    command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(command, check=False)


def show_header_message(message: str):
    print(f"\n\n------------------ {message.upper()} ------------------\n")
