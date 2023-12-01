import sys

def part1(puzzle):
    values = []
    for line in puzzle:
        first, last = float("inf"), float("-inf")
        for i in range(len(line)):
            if line[i].isdigit():
                first, last = min(first, i), max(last, i)
        value = int(line[first] + line[last])
        values.append(value)
    print(sum(values))

if __name__ == "__main__":
    with open(sys.argv[1]) as puzzle:
        part1(puzzle)
