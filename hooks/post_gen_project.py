import subprocess
from pathlib import Path
from typing import List

# The list of packages that we should install by default.
_PACKAGES = []

# The list of development packages that we should install by default.
_DEV_PACKAGES = ["pytest-mock", "pytest-faker", "black", "pre-commit"]


def _run(command: List[str]) -> None:
    """
    Shortcut for running an external command with subprocess.
    :param command: The command to run.
    """
    subprocess.run(command, check=True)


def _venv_run(command: List[str]) -> None:
    """
    Runs a command in the generated venv.
    :param command: The command to run within the venv.
    """
    _run(["poetry", "run"] + command)


def _install_packages() -> None:
    """
    Installs necessary packages.
    """
    package_install_command = ["poetry", "add"]
    package_install_command.extend(_PACKAGES)
    dev_package_install_command = ["poetry", "add", "-D"]
    dev_package_install_command.extend(_DEV_PACKAGES)
    _run(package_install_command)
    _run(dev_package_install_command)


def _run_black() -> None:
    """
    Runs `black` on the results after generating. This is so we don't get any
    confusing black errors when we run the unit tests after generation.
    (Due to templating, we can't guarantee that black will like the raw
    generated code.)
    """
    _venv_run(["black", "."])


def _run_poetry_install() -> None:
    """
    Run `poetry install` command to update the package itself
    """
    _run(["poetry", "install"])


def main():
    _install_packages()
    _run_black()
    _run_poetry_install()


if __name__ == "__main__":
    main()
