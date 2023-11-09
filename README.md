# Coiled Notebooks Workflow

![CI](https://github.com/elsdes3/coiled-notebooks-workflow/workflows/CI/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/mit)
![OpenSource](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
![prs-welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)

## [About](#about)

Workflow to programmatically deploy a cloud-based [JupyterLab server](https://jupyterlab.readthedocs.io/en/latest/) using [Coiled notebooks](https://docs.coiled.io/user_guide/usage/notebooks/index.html).

## Links Used

### Ansible

1. [IAM managed policy](https://docs.ansible.com/ansible/latest/collections/community/aws/iam_managed_policy_module.html)

   - [`boto3` module](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/create_policy.html)
2. [IAM User with managed policy](https://docs.ansible.com/ansible/latest/collections/amazon/aws/iam_user_module.html)
3. [IAM role with managed policy](https://docs.ansible.com/ansible/latest/collections/community/aws/iam_role_module.html#parameters)

   - [`boto3` module](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam/client/attach_role_policy.html)
4. [Running a Python script](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/script_module.html)
5. [Defining `changed_when` when running ad-hoc scripts](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_error_handling.html#defining-changed)
6. [Attaching a managed policy to an IAM role or user](https://dev.to/aws-builders/chapter-5-iam-policy-cg1)

### Coiled

1. [Manual set up of AWS as cloud provider](https://docs.coiled.io/user_guide/setup/aws/manual.html)
2. [Manual set up of Coiled software environment](https://docs.coiled.io/user_guide/software/manual.html)
3. [Coiled notebooks](https://docs.coiled.io/user_guide/usage/notebooks/index.html)

### `tox`

1. How to interactively pass arguments to `tox` using `posargs`

   - [video](https://youtu.be/os_daySYRFs?si=l2jeojVjVGrW6BbA&t=866)
     - 14:26 - 14:44
   - [docs](https://tox.wiki/en/3.3.0/example/general.html#interactively-passing-positional-arguments)
