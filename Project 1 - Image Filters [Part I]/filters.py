
# Use this file to write your filter functions!
def grayscale(image_matrix):
    output_image_matrix = []
    for row_num in range(len(image_matrix)):
      row_matrix = []
      for col_num in range(len(image_matrix[row_num])):
        pixel = image_matrix[row_num][col_num]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        average = (red + green + blue) // 3
        gray_pixel = [average, average, average]
        row_matrix.append(gray_pixel)
      output_image_matrix.append(row_matrix)
    return output_image_matrix

def red_stripes(image_matrix):
    for row_num in range(len(image_matrix)):
        if row_num % 100 < 50:
          for i in range(len(image_matrix[0])):
            image_matrix[row_num][i][0] = 255
    return image_matrix