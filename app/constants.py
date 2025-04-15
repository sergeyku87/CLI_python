EMPTY_ARRAY = [0, 0, 0, 0, 0]
LEVEL_DEBUG: dict = {
    "INFO": 0,
    "DEBUG": 1,
    "WARNING": 2,
    "ERROR": 3,
    "CRITICAL": 4
}
HEADERS: tuple[str] = (
    "HANDLER",
    "INFO",
    "DEBUG",
    "WARNING",
    "ERROR",
    "CRITICAL",
)
REPORTS: tuple[str] = ("handlers",)
RESPONSE_ERR: str = "Not correct:\n {}"
REGEX: dict = {
    "date": "(?P<date>\d{4}-\d{2}-\d{2})",
    "time": "(?P<time>\d{2}:\d{2}:[\d|\W]+)",
    "level": "(?P<level>\S*)",
    "handler": "(?P<handler>/\S+/)",
}
SAMPLE: str = "{date} {time} {level}.*?{handler}".format(**REGEX)
