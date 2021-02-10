class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        bw = ""
        for el1 in self.matrix:
            # print(el1)
            w_wrd = ""
            for el2 in el1:
                if w_wrd == "":
                    w_wrd = str(el2)
                else:
                    w_wrd = w_wrd + " " + str(el2)
            if bw == "":
                bw = w_wrd
            else:
                bw = bw + "\n" + w_wrd
        return bw

    def __add__(self, other):
        r_matrix = []
        h_value = 0
        h_list = []
        for h_value in range(len(self.matrix)):
            n_list = []
            for n_value in range(len(self.matrix[h_value])):
                # n_list.append()
                n_list.append(self.matrix[h_value][n_value] + other.matrix[h_value][n_value])
            h_list.append(n_list)
        return Matrix(h_list)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix_1)
matrix_2 = Matrix([[11, 22], [33, 34], [55, 66]])
matrix_3 = Matrix([[11, 22], [33, 34], [55, 66]])
print(matrix_1 + matrix_2 + matrix_3)

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [3, 4], [5, 6]])
# print (matrix_1 + matrix_3)
