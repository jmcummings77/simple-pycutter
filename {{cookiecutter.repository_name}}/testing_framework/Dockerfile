FROM python:{{cookiecutter.primary_python_version}}-slim

# Set environment variables.
#   TEST_DIRECTORY                  - Explicity set the directory where these build commands are being run.
#   PYTHONDONTWRITEBYTECODE         - Suppress the ouput of python byte code.
#   PIP_DISABLE_PIP_VERSION_CHECK   - Suppress pip's reminder to update its version.
#   POETRY_VIRTUALENVS_CREATE       - Set whether to install dependencies globally. Setting this to `false` or
#                                     the equivalent allows the tests to be run through Jenkins.
ENV \
  TEST_DIRECTORY=/src/              \
  PYTHONDONTWRITEBYTECODE='1'       \
  PIP_DISABLE_PIP_VERSION_CHECK=on  \
  POETRY_VIRTUALENVS_CREATE=false

# Dependencies for building packages with C-extensions.
RUN apt-get update --fix-missing && apt-get install -y build-essential

# Use pip to install poetry. Doing so in this manner is fine since this image is basically a virtual environment.
RUN pip install poetry==1.0.10

# Explicitly set the working directory and copy in the files needed to set up the work environment.
WORKDIR ${TEST_DIRECTORY}
COPY poetry.lock pyproject.toml ${TEST_DIRECTORY}
# Note: Any files added here are read only to test runner. You should not copy in files that are needed to run your tests.

RUN poetry install --no-interaction

# Allow poetry to be run by the test runner user.
RUN chmod -R 777 /root/
