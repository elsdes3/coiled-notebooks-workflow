#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Define utilities to Manage Coiled resources."""

# pylint: disable=invalid-name,dangerous-default-value
# pylint: disable=too-many-locals,unused-argument,unnecessary-lambda


import argparse
import json

import coiled

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--softw-env",
        type=str,
        dest="softw_env",
        default="create",
        help="whether to create or delete Coiled software environment",
    )
    args = parser.parse_args()

    coiled_se_name = "my-pip-env"

    c_envs = coiled.list_software_environments()

    if args.softw_env == "create":
        if coiled_se_name not in list(c_envs):
            cenv_out = coiled.create_software_environment(
                name=coiled_se_name,
                pip="files/requirements_coiled.txt",
            )
            print(cenv_out)
        else:
            print(json.dumps(c_envs))
    else:
        if c_envs and coiled_se_name in list(c_envs):
            cenv_out = coiled.delete_software_environment(name=coiled_se_name)
            print(cenv_out)  # 'Software environment deleted successfully.'
        else:
            print(json.dumps(c_envs))  # {} (dict with >=1 keys)
