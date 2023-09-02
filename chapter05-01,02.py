#top of hanoi/number of moves
def move(n, start, destination):
    print("Move discs {} from {} to {}".format(n, start, destination))


def hanoi(n, start = 'A', destination = 'C', via = 'B'):
    
    # Move from start column to arrival column at once when there is one disc
    if n <= 1:
        move(1, start, destination)
        return 1

    count = 0
    # Move n-1 discs from start column to auxiliary column
    count += hanoi(n - 1, start, via, destination)

    # Move the largest disk from the start column to the arrival column
    count += 1
    move(n, start, destination)

    # Move n-1 discs from auxiliary column to arrival column
    count += hanoi(n - 1, via, destination, start)

    return count
    
a = int(input("enter the number of discs : "))

hanoi(a)
print(f"number of moves is {2**a-1}")
