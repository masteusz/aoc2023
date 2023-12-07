FNAME = "/home/mst/projects/mine/aoc2023/1/in.txt"

TEST = ["1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet", ]


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def parse_line(ln: str) -> int:
    first, second = "", ""
    for char in ln:
        if char.isdigit():
            first = char
            break
    for char in reversed(ln):
        if char.isdigit():
            second = char
            break
    return int(first + second)


if __name__ == '__main__':
    s = 0
    for line in open(FNAME):
        parsed = parse_line(line)
        s += parsed
    print(s)
