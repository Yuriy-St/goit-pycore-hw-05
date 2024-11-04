import sys
from collections import Counter
from pathlib import Path


def read_lines(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.split()
    return {"date": date, "time": time, "level": level, "message": " ".join(message)}


def load_logs(file_path: Path) -> list:
    """
    Returns list of log lines
    """
    return [line for line in read_lines(file_path)]


def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]


def count_logs_by_level(logs: list) -> dict:
    levels_count = Counter(log["level"] for log in logs)

    return levels_count


def display_log_counts(levels: dict):
    # Table settings
    col_width = [15, 10]
    table_width = 0
    for col in col_width:
        table_width += col
    headers = ["Log level", "Count"]

    # Table printing
    print("\n" + "-" * table_width)
    print(f" {headers[0]: <{col_width[0]}}| {headers[1]: <{col_width[1]}}")
    print("-" * table_width)
    for level in levels.keys():
        print(f" {level: <{col_width[0]}}| {levels[level]: <{col_width[1]}}")
    print("-" * table_width + "\n")


def display_log_levels(logs: list):
    print(f"Details of the '{logs[0]["level"]}' level logs:")
    for log in logs:
        date, time, level, message = log.values()
        print(f"{date} {time} {level} - {message}")


def main():
    argv_length = len(sys.argv)
    if argv_length < 2:
        print(f"Incorrect number of arguments")
        sys.exit(1)
    try:
        log_path = Path(sys.argv[1])
        log_lines = load_logs(log_path)

        # List of log dicts {"date", "time", "level", "message"}
        logs = [parse_log_line(log) for log in log_lines]

        # dictionary of counted levels {<level>: <count>}
        levels_count = count_logs_by_level(logs)
        display_log_counts(levels_count)

        if argv_length > 2:
            level = sys.argv[2]
            levels = [l.lower() for l in levels_count.keys()]
            if level.lower() not in levels:
                raise ValueError(f"Unknown level value '{level}'")
            level_logs = filter_logs_by_level(logs, level)
            display_log_levels(level_logs)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
