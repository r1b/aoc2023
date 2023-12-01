import sys

NUMBER_TRIE = {
    "o": {"n":{"e": "1"}},
    "t": {
        "w": {"o": "2"},
        "h": {"r": {"e": {"e": "3"}}},
    },
    "f": {
        "o": {"u": {"r": "4"}},
        "i": {"v": {"e": "5"}},
    },
    "s": {
        "i": {"x": "6"},
        "e": {"v": {"e": {"n": "7"}}}
    },
    "e": {"i": {"g": {"h": {"t": "8"}}}},
    "n": {"i": {"n": {"e": "9"}}}
} 

def part2(puzzle):
    values = []
    for line in puzzle:
        cur = NUMBER_TRIE
        first, last = "", ""
        depth, i = 0, 0

        while i < len(line):
            c = line[i]
            if c.isdigit():
                # e.g:
                # - one1two
                #      ^
                first, last = (c, c) if not first else (first, c)
                cur = NUMBER_TRIE
                i += 1
                depth = 0
            elif c not in cur:
                # e.g:
                # - vszthree
                #     ^
                cur = NUMBER_TRIE
                i -= depth
                i += 1
                depth = 0
            elif isinstance(cur[c], str):
                # e.g:
                # - one7
                #     ^
                first, last = (cur[c], cur[c]) if not first else (first, cur[c])
                cur = NUMBER_TRIE
                if c not in cur:
                    # XXX: Some numbers end in valid prefixes of other numbers
                    # e.g:
                    # - oneight
                    i += 1
                depth = 0
            else:
                # e.g:
                # - zdone4
                #     ^
                cur = cur[c]
                i += 1
                depth += 1

        value = int(first + last)
        values.append(value)
    print(sum(values))

if __name__ == "__main__":
    with open(sys.argv[1]) as puzzle:
        part2(puzzle)
