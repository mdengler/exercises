#!/usr/bin/env python
import sys

def validmerge(m, x, y):
    if ((m == x and len(y) < 1)
        or
        (m == y and len(x) < 1)):
        return True

    elif len(m) < 1 or len(y) < 1 or len(x) < 1:
        return False

    elif all(p == m[0] for p in (x[0], y[0])):
        return (validmerge(m[1:], x[1:], y)
                or
                validmerge(m[1:], x, y[1:]))

    elif m[0] == x[0]:
        return validmerge(m[1:], x[1:], y)

    elif m[0] == y[0]:
        return validmerge(m[1:], x, y[1:])

    else:
        return False


if __name__ == "__main__":
    sys.exit(0 if validmerge(*sys.argv[1:]) else 1)













