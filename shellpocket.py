#!/usr/bin/env python3
import os
import re
import fcntl
import termios
import argparse

import yaml
from simple_term_menu import TerminalMenu

DEFAULT_URL = "127.0.0.1"
DEFAULT_PORT = 1337


def parse_args():
    parser = argparse.ArgumentParser(
        prog=__package__, description="Your own shell pocket"
    )
    parser.add_argument(
        "-i",
        "--ip",
        help=f"IP to use when generating a shell (default: {DEFAULT_URL})",
        default=DEFAULT_URL,
        type=str,
    )
    parser.add_argument(
        "-p",
        "--port",
        help=f"Port to use when generating a shell (default: {DEFAULT_PORT})",
        default=DEFAULT_PORT,
        type=int,
    )
    return parser.parse_args()


def load_file() -> list:
    with open("shells.yml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def pick_a_shell(shells: list) -> str:
    pretty_shells = []
    for category in shells:
        for shell in category["shells"]:
            pretty = f"[{category['category']}] {shell}"
            pretty_shells.append(pretty)

    terminal_menu = TerminalMenu(pretty_shells)
    choice_index = terminal_menu.show()
    if type(choice_index) != int: return

    choice = pretty_shells[choice_index]
    chosen_shell = re.findall("\].*", choice)[0].strip("] ").replace("\\", "")
    return chosen_shell


def replace_conn_info(shells: list, ip: str, port: int):
    for category in shells:
        for idx, shell in enumerate(category["shells"]):
            new_shell = shell.replace("{{ip}}", ip).replace("{{port}}", str(port))
            category["shells"][idx] = new_shell
    return shells


def send_to_stdin(string: str) -> None:
    tty_path = "/proc/{}/fd/0".format(os.getpid())
    with open(tty_path, "w") as tty_fd:
        for char in string:
            fcntl.ioctl(tty_fd, termios.TIOCSTI, char)


if __name__ == "__main__":
    args = parse_args()
    shells = load_file()
    shells = replace_conn_info(shells, args.ip, args.port)
    shell = pick_a_shell(shells)
    if shell: send_to_stdin(shell)
