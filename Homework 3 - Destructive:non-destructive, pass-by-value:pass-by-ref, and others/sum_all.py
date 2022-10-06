def sum_all(lst):
    result = 0
    sum = 0
    for row in range(len(lst)):
        for col in lst[row]:
            sum += col
        if sum == 0:
            result = sum
    return sum

if __name__ == "__main__":
  lst = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
            ]
  print(sum_all(lst))