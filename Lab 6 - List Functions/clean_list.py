def clean_list(numbers):
    for i in range(len(numbers)):
        if 0 in numbers:
            numbers.remove(0)
    return numbers



if __name__ == '__main__':
    first = []
    while True:
        item = input().strip()
        if item == "":
            break
        item2 = int(item)
        first.append(item2)
    
    print(clean_list(first))


