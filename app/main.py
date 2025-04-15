import sys
from argparse import ArgumentParser, Namespace

from constants import (
    HEADERS,
    REPORTS,
    RESPONSE_ERR,
    SAMPLE,
)
from function import (
    analysis_logs,
    default_handler,
    is_correct_args,
    is_correct_report,
    is_diff_args,
)


def main():
    parser: ArgumentParser = ArgumentParser(
        description="CLI for analysis log django app",
    )
    parser.add_argument(
        "path",
        nargs="*",
        type=str,
        help="One or more arguments CLI",
    )
    parser.add_argument(
        "--report",
        nargs="+",
        help="Special log processing",
    )

    args: Namespace = parser.parse_args()

    if not all((
        is_diff_args(args.path),
        is_correct_args(args.path),
        is_correct_report(REPORTS, args.report),
    )):
        sys.exit(RESPONSE_ERR.format(
            " ".join(f"{k}: {v}\n" for k, v in args.__dict__.items())
        ))

    result = analysis_logs(args.path, SAMPLE)
    result: list = sorted(
        [[k] + v for k, v in result.items()],
        key=lambda x: (x[0] == "", x[0]),
    )

    match args.report:
        case ["handlers"]:
            default_handler(result, HEADERS)

if __name__ == "__main__":
    main()
