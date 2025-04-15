import fileinput
import os
import re
import sys

from constants import EMPTY_ARRAY, LEVEL_DEBUG


def is_correct_args(args: list[str | os.PathLike]) -> bool:
    if args:
        return all([os.path.exists(arg) for arg in args])
    return False

def is_diff_args(args: list[str | os.PathLike]) -> bool:
    return len(set(args)) == len(args)

def is_correct_report(correct_reports: tuple, report: str) -> bool:
    if report and len(report) == 1:
        return all([repo in correct_reports for repo in report])
    return False


def default_handler(data: [list[list]], headers: tuple[str]) -> None:
    max_widths: list = [len(head) for head in headers]

    for row in data:
        for idx in range(len(row)):
            max_widths[idx] = max(max_widths[idx], len(str(row[idx])))

    line = "+%s+" % "+".join("-"*(width+2) for width in max_widths)
    fmt_str = "| %s |" % " | ".join(f"{{:<{width}}}" for width in max_widths)
    fmt_str_total = "Total requests: {}"

    sys.stdout.write(fmt_str_total.format(sum(data[-1][1:])) + "\n")
    sys.stdout.write(line + "\n")
    sys.stdout.write(fmt_str.format(*headers) + "\n")
    sys.stdout.write(line + "\n")
    for elem in data:
        sys.stdout.write(fmt_str.format(*elem) + "\n")
    sys.stdout.write(line + "\n")

def analysis_logs(path_to_files, sample):
    sample: re.Pattern = re.compile(sample)
    result: dict = {}
    total: list = EMPTY_ARRAY[:]
    for line in fileinput.input(files=path_to_files):
        if re.search("django.request", line):
            temp: re.Pattern = sample.search(line)
            if temp.group("handler") not in result:
                result[temp.group("handler")]: list = EMPTY_ARRAY[:]
                result[temp.group("handler")][LEVEL_DEBUG[temp.group("level")]] = 1
            else:
                result[temp.group("handler")][LEVEL_DEBUG[temp.group("level")]] += 1
            total[LEVEL_DEBUG[temp.group("level")]] += 1
    result.update({"": total})
    return result
