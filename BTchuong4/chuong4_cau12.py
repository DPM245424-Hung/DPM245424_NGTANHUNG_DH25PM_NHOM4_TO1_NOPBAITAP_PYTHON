
def oscilate(x,y,z=1):
    if x < y:
        yield x
        yield -x
        if x+z <= y:
            yield from oscilate(x+z,y,z)
def main():
    for n in oscilate(-3,5):
        print(n, end=' ')
    print()
main()