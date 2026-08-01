import os
import subprocess


def clear_terminal() -> None:
    command = ["cmd", "/c", "cls"] if os.name == "nt" else ["clear"]
    subprocess.run(command, check=False)


def show_header_message(message: str) -> None:
    print(f"\n\n------------------ {message.upper()} ------------------\n")
