FNAME = "/home/mst/projects/mine/aoc2023/1/in.txt"

TEST = ["two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
        ]

lut = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def replace_digits(_line: str) -> str:
    replacements = dict()
    for digit in lut:
        if _line.find(digit) != -1:
            replacements[digit] = _line.find(digit)
    repl = sorted(replacements, key=replacements.get)
    for r in repl:
        _line = _line.replace(r, str(lut[r]), 1)
    return _line


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
        new = line
        while True:
            replaced = replace_digits(new)
            if replaced == new:
                break
            new = replaced
        parsed = parse_line(new)
        l = line.strip("\n")
        r = replaced.strip("\n")
        if l != r:
            print(l, r, parsed)
        s += parsed
    print(s)
