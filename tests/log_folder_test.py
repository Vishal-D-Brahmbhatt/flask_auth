import os

from click.testing import CliRunner

from app import create_log_folder

runner = CliRunner()


def test_create_log_folder():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0