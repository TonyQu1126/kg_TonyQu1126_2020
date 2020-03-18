import sys
def main(argv):
    # unpack two arguments
    s, t = argv
    # if they have different length
    # it is not possible to get one to one mapping
    if len(s) != len(t):
        print("false")
        return
    # create a dictionary to record the mapping
    map = dict()
    # iterate the characters in the strings
    for i in range(len(s)):
        # get ith character from first string
        a = s[i]
        # get ith character from second string
        b = t[i]
        # if a is present as a key in dictionary
        if a in map:
            # if a is a key and the mapping is not correct
            if map[a] != b:
                print("false")
                return
        # is a is not a key
        # add this mapping into dictionary
        else:
            map[a] = b
    print("true")
    return

if __name__ == "__main__":
    main(sys.argv[1:])
