def greatest_row_sum(lst):
    result = 0
    for row in range(len(lst)):
        sum = 0
        for col in lst[row]:
            sum += col
        if result == 0 or result < sum:
            result = sum
    return result

if __name__ == "__main__":
    print(greatest_row_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 5, 2]]))