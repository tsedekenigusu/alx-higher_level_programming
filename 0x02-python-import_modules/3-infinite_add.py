#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if (len(sys.argv)) <= 1:
        print(0)
else:
    sum = 0
    for x in range(1, (len(sys.argv))):
        sum += int(sys.argv[x])
    print("{:d}".format(sum))
