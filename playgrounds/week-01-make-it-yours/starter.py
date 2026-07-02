"""Tiny server-log analyzer.

Reads a log file in chunks (the way requests/CPython docs read streams),
then reports request counts, error rate, and average response time.

This version is deliberately naive:
- it crashes on missing files and malformed lines
- several spots are begging for the walrus operator :=

Log line format:
    2026-07-01 14:32:07 GET /api/users 200 123ms
"""

import sys

CHUNK_SIZE = 4096


def read_lines(path):
    """Yield lines from a file, reading it in fixed-size chunks."""
    buffer = ""
    f = open(path, "r")
    chunk = f.read(CHUNK_SIZE)
    while chunk != "":
        buffer += chunk
        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            yield line
        chunk = f.read(CHUNK_SIZE)
    f.close()
    if buffer:
        yield buffer


def parse_line(line):
    """Turn one log line into a dict."""
    date, time, method, path, status, duration = line.split(" ")
    return {
        "time": time,
        "method": method,
        "path": path,
        "status": int(status),
        "ms": int(duration.rstrip("ms")),
    }


def analyze(path):
    entries = []
    for line in read_lines(path):
        stripped = line.strip()
        if stripped == "":
            continue
        entries.append(parse_line(stripped))

    total = len(entries)
    errors = [e for e in entries if e["status"] >= 500]

    print(f"requests : {total}")
    print(f"errors   : {len(errors)} ({len(errors) / total:.0%})")

    avg = sum(e["ms"] for e in entries) / total
    print(f"avg time : {avg:.0f}ms")

    slow = [e["path"] for e in entries if e["ms"] > 500]
    if len(slow) > 0:
        print(f"slow     : {', '.join(slow)}")


if __name__ == "__main__":
    analyze(sys.argv[1])
