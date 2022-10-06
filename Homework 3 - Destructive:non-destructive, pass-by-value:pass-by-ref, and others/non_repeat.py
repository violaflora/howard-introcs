def non_repeat(items):
    for num in items:
        if items.count(num) == 1:
            return num

if __name__ == "__main__":
    print(non_repeat([-1, 2, -1, 3, 2, 2]))
    print(non_repeat([-1, 3, 2, -1, 3, 2, 2]))