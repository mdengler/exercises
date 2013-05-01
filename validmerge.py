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


def validmerge2(m, inputs):
    if m in inputs and not any(i for i in inputs if i != m):
        return True

    elif len(m) < 1 or not any(inputs):
        return False

    else:
      if m[0] in [i[0:1] for i in inputs]:
        possibilities = [p for p in inputs if p[0:1] == m[0]]
        for possibility in possibilities:
            other_inputs = inputs[:]
            other_inputs.remove(possibility)
            if validmerge2(m[1:], [possibility[1:]] + other_inputs):
                return True

    return False



def __test__():
    TESTS = [
        [["", ["", ""]], True],
        [["A", ["A", ""]], True],
        [["B", ["", "B"]], True],
        [["AA", ["AA", ""]], True],
        [["BB", ["", "BB"]], True],
        [["ABA", ["A", "BA"]], True],
        [["BB", ["", "BB"]], True],
        [["BB", ["B", "B"]], True],

        [["", ["F", ""]], False],
        [["", ["", "F"]], False],
        [["F", ["", ""]], False],
        [["FF", ["", "F"]], False],
        [["F", ["A", "B"]], False],

        [["EFGABCDEF", ["EGBDF", "FACE"]], True],
        [["DEADBEEF", ["DEAD", "BEEF"]], True],
        [["314159265", ["34525", "1196"]], True],

        ]

    passed = False
    for test_args, expected_result in TESTS:
        v1 = None
        v2 = None
        try:
            v1 = validmerge(test_args[0], *test_args[1])
        except Exception, msg:
            v1 = "failed: %s" % msg
        try:
            v2 = validmerge2(*test_args)
        except Exception, msg:
            v2 = "failed: %s" % msg

        if v1 != v2:
            print "FAIL: expected %s, but INCONSISTENT: %s vs %s" % (expected_result, v1, v2)
        elif v1 != expected_result:
            print "FAIL: expected %s, but got: %s / %s" % (expected_result, v1, v2)
        else:
            assert v1 == v2 == expected_result
            print "GOOD: '%s' %s a valid merge of %s" % (test_args[0], "is" if v1 else "is not", test_args[1])
            passed = True

    return passed



if __name__ == "__main__":
    args = sys.argv[1:]

    retval = 1
    if len(args) == 3:
        if validmerge(*args):
            retval = 0
    elif __test__():
        retval = 0

    sys.exit(retval)













