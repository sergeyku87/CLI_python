import os
import app.function
import app.main
import pytest
import sys

from app.constants import REPORTS, SAMPLE, HEADERS
from app.function import (
    is_correct_args,
    is_diff_args,
    is_correct_report,
    analysis_logs,
    default_handler,
)


@pytest.mark.parametrize(
    "args, expectation",
    (   
        ((sys.path[0],), True),
        ((sys.path[0], sys.path[1]), True),
        ((os.path.join(sys.path[0], "some_dir")), False),
        ((sys.path[0], os.path.join(sys.path[0], "some_dir")), False),
        ((), False),
    )
)
def test_is_correct_args(args, expectation):
    assert is_correct_args(args) == expectation

@pytest.mark.parametrize(
    "args, expectation",
    (
        (("a", "b"), True),
        (("a", "a"), False),
        (("a", "b", "a"), False),
    )
)
def test_is_diff_args(args, expectation):
    assert is_diff_args(args) == expectation

@pytest.mark.parametrize(
    "report, expectation",
    (
        ("some_report", False),
        ([REPORTS[0]], True),
        (None, False),
        ([REPORTS[0], "some_report"], False),
    )
)
def test_is_correct_report(report, expectation):
    assert is_correct_report(REPORTS, report) == expectation

def test_analysis_logs(log_file):
    expected = {
        "/api/v1/reviews/": [2, 0, 0, 0, 0],
        "/admin/dashboard/": [1, 0, 0, 0, 0],
        "": [3, 0, 0, 0, 0],
    }
    assert analysis_logs(log_file, SAMPLE) == expected

def test_default_handler(data, output, capsys):
    default_handler(data, HEADERS)
    captured = capsys.readouterr()
    assert captured.out == output

def test_m(mocker, log_file, capsys, main_output):
    mocker.patch.object(sys, "argv", ['main.py', str(log_file), '--report', 'handlers'])
    m = mocker.patch.object(os.path, "exists")
    m.return_value = True
    app.main.main()
    captured = capsys.readouterr()
    assert captured.out == main_output
    