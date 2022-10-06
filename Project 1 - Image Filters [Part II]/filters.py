# Use this file to write your filter functions!
import copy
import math

def invert_colors(image_matrix):
    output_image_matrix = []
    for row_num in range(len(image_matrix)):
      row_matrix = []
      for col_num in range(len(image_matrix[row_num])):
        pixel = image_matrix[row_num][col_num]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        ir = 255 - red
        ig = 255 - green
        ib = 255 - blue
        inverted_pixel = [ir, ig, ib]
        row_matrix.append(inverted_pixel)
      output_image_matrix.append(row_matrix)
    return output_image_matrix

def flip(image_matrix):
  for i in range(len(image_matrix)):
    for j in range(len(image_matrix[i])):
      image_matrix[i][j] == 255
      output_image_matrix = image_matrix[::-1]
  return output_image_matrix

def sepia(image_matrix):
    output_image_matrix = []
    for row_num in range(len(image_matrix)):
      row_matrix = []
      for col_num in range(len(image_matrix[row_num])):
        pixel = image_matrix[row_num][col_num]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        sr = math.floor((red * .393) + (green * .769) + (blue * .189))
        sg = math.floor((red * .349) + (green * .686) + (blue * .168))
        sb = math.floor((red * .272) + (green * .534) + (blue * .131))
        if sr > 255:
          sr = 255
        if sg > 255:
          sg = 255
        if sb > 255:
          sb = 255
        sepia_pixel = [sr, sg, sb]
        row_matrix.append(sepia_pixel)
      output_image_matrix.append(row_matrix)
    return output_image_matrix