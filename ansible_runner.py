#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Ansible playbook runner which loads environment variables."""

# pylint: disable=invalid-name


import argparse
import os
import shlex
import subprocess

from dotenv import load_dotenv


def run_cmd(cmd: str) -> None:
    """Run a shell command using Python."""
    print(cmd)
    process = subprocess.Popen(
        shlex.split(cmd), shell=False, stdout=subprocess.PIPE
    )
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            print(str(output.strip(), "utf-8"))
    _ = process.poll()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--action",
        type=str,
        dest="action",
        default="create",
        help="whether to create or delete project resources",
    )
    args = parser.parse_args()

    PROJ_ROOT = os.path.join(os.getcwd())
    env_file_dir = os.path.join(PROJ_ROOT, ".env")
    # print(os.path.abspath(env_file_dir))

    load_dotenv(env_file_dir, verbose=True)

    nb = "01_create.yml" if args.action == "create" else "02_delete.yml"
    run_cmd(
        "ansible-playbook " f"-i inventories/production {nb} " "-t aws,coiled"
    )
