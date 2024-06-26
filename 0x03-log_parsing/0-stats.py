#!/usr/bin/python3
"""log parsing"""
import sys
import re
import signal


def validate_line(line):
    """validate our ip address"""
    pattern = (
        r"(\d+\.\d+\.\d+\.\d+) - \[.*\] \"GET /projects/260 HTTP/1\.1\" "
        r"(\d+) (\d+)"
    )
    matching = re.match(pattern, line)
    if matching:
        status_code = matching.group(2)
        file_size = int(matching.group(3))
        return [status_code, file_size]
    return None


def print_metrics(status, f_size):
    """print outpout"""
    for key, value in status.items():
        if value > 0:
            print(f"{key}: {value}")


def signal_handler(sig, frame):
    """signalling when ctrl+c"""
    # print_metrics(status_codes, total_file_size)
    sys.exit(0)


def main():
    """opening function"""
    line_done = 0
    global status_codes, total_file_size
    status_codes = {
        "200": 0, "301": 0, "400": 0,
        "401": 0, "403": 0, "404": 0,
        "405": 0, "500": 0
        }
    total_file_size = 0
    signal.signal(signal.SIGINT, signal_handler)
    try:
        for line in sys.stdin:
            result = validate_line(line)
            total_file_size += result[1]
            status_codes[result[0]] += 1
            line_done += 1
            if line_done % 10 == 0:
                print(f"File size: {total_file_size}")
                print_metrics(status_codes, total_file_size)
    except KeyboardInterrupt:
        print_metrics(status_codes, total_file_size)


if __name__ == "__main__":
    main()
