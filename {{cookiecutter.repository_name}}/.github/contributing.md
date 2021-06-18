# Contributing Guidelines

Welcome and thank you for considering to contribute to Data Dough!

Here you will find all the information you'll need to setup your development environment and start contributing.

## Table of Contents

* [Submitting Bug Reports](#Submitting Bug Reports)
* [Environment Setup](#Environment Setup)
* [Running Tests](#Running Tests)
* [Code Editing Guidelines](#Code Editing Guidelines)
* [Opening A PR](#Opening A Pull Request)

### Preface

Please read our [Contributor Code of Conduct](code_of_conduct.md) and our [Contributor License Agreement](.github/contributor_license_agreement.md). You will be asked to sign our CLA when you submit your first pull request.

## Submitting Bug Reports

Bug reports (and feature requests) are always appreciated and we will do our best to respond to any opened issues in a timely manner.

You can open an issue [here]({{cookiecutter.repository_root_url}}/issues/new/choose) by choosing the correct issue type and filling in the template. Please remember to be respectful to all users and developers and try to provide as much context as possible.

## Environment Setup

We use [poetry](https://python-poetry.org/) to both manage dependencies and publish this package. You can find information about installing this software [here](https://python-poetry.org/docs/).

This library supports Python versions `3.9` and above, so you must have a version of Python installed that meets those specifications in order to progress any further with setting up your environment. We use the excellent [pyenv](https://github.com/pyenv/pyenv) to manage our local Python installation, but an in-depth guide to using this is outside the scope of this document.

Once both `poetry` and a compliant version of Python are installed, you can use `poetry` to create your virtual environment for this project. The following command (run at the root of this project) will create a virtual environment within the `.venv` directory:

```bash
poetry install
```

You are able to fully interact with the virtual environment using `poetry` commands, but we find it easiest to "source" the virtual environment into your current terminal session. In most shells, this can be done with the following command (run from the root of this project):

```bash
. .venv/bin/activate
```

To leave this virtual environment at any time, you can run `deactivate`.

Finally, we use to [pre-commit](https://pre-commit.com) package to run useful hooks to maintain code quality and enforce style guides. The full list of hooks can be found within the [.pre-commit-config.yaml](.pre-commit-config.yaml) file. To install these hooks, run the following command from within the virtual environment:

```bash
pre-commit install
```

Now the linters, formatters, and type checkers will be run automatically with every commit, making PRs easier to review and removing distractions from the contributing process.

To run these commands independently from the `git commit` command, you can run the following command:

```bash
pre-commit run --all
```

**NOTE**: The `mypy` type checker is included with these commits, meaning if the type annotations are not correct the pre-commit hooks will fail and by default your commit command will also fail. **This was an intentional choice**. However, sometimes you _need_ to commit before the code is correct, and you can accomplish this with the `-n/--no-verfify` flags to the `git commit` command.

## Running Tests

The easiest way to run tests is by running the `run_tests.sh` bash script from within the virtual environment in the root directory of the project.

```bash
./run_tests.sh
```

The reason for using this script, rather than automatically running tests via the `pytest` test runner, is because the `pytest-cov` plugin for `pytest` does not play nicely with packages that are `pytest` plugins. Therefore, the `coverage` package must be interfaced with separately.

## Code Editing Guidelines

### Comments & Documentation

Please leave helpful comments that will assist users, code reviewers, and future contributors in understanding the code you wrote. If you spend time deciding between two implementations, briefly jot down your reasoning. If you implement something using external documentation or resources, add a link. Doing so improves the contributing experience for everyone involved.

### Black

This package uses the [black](https://github.com/psf/black) package to enforce opinionated code formatting. However, this package does not (currently) enforce line length for docstring and comments. Please be cognizant of this fact and try to adhere to a 92 character limit.

### MyPy

This package uses the [mypy](https://github.com/python/mypy) package to perform static type checking. Static type checking is enforced on _*all*_ library code (not including tests). Types are annotated following the [PEP 484](https://www.python.org/dev/peps/pep-0484/) and [PEP 3107](https://www.python.org/dev/peps/pep-3107/) conventions.

## Opening A Pull Request

To contribute, first [fork the repository]({{cookiecutter.repository_root_url}}).

### Which Branch to Use?

The `primary` branch is the "master" branch for the repository where releases occur. **You cannot develop on this branch.** The `develop` branch is where development occurs, i.e. new features are added or bugs are fixed. This is the "staging area" before being merged into and released from the `primary` branch. If you plan on adding a new feature to the codebase, make sure to branch off of the `develop` branch, and once merged it will be included in the next release.

Ready to push upstream? Open a pull request [here]({{cookiecutter.repository_root_url}}/compare). Make sure to fill out the PR template fully to help the code reviewers understand your contributions.
