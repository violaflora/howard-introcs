
def flip_transfer_list(lst1, lst2):
    for i in range(len(lst1) - 1, -1, -1):
      lst2.append(lst1[i])
    lst1.clear()
 
if __name__ == '__main__':
    first = []
    second = []
    while True:
        item = input().strip()
        if item == "":
            break
        first.append(item)
    
    flip_transfer_list(first, second)
    print(first)
    print(second)

