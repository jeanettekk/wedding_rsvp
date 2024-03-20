matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

def flip(matrix):

    items = len(matrix)
    half = round(items/2)
    max_index = items - 1
    max_numbers = list((0,) * items)

    for row_index, num_line in enumerate(matrix):

        for col_index, number in enumerate(num_line):

            if col_index == 0 and row_index < half:

                a = number

                for num in [num_line[max_index], matrix[max_index - row_index][col_index], matrix[max_index -
                                                                                                  row_index][max_index]]:

                    if num > a:

                        a = num

                max_numbers.append(a)

            elif col_index < half and row_index < half:

                b = number

                for x in [num_line[col_index + 1], matrix[max_index - row_index][col_index],
                                 matrix[max_index - row_index][col_index + 1]]:

                    if x > b:

                        b = x

                max_numbers.append(b)

    print(sum(max_numbers))

flip(matrix)