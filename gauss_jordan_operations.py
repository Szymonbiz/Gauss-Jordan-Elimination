from matrix import Matrix


class GaussJordan:
    """
    Gauss Jordan Operations
    """

    @staticmethod
    def adding_equation_n_to_m(obj: Matrix, n, m):
        for t in range(obj.cols):
            obj.matrix[m][t] += obj.matrix[n][t]
        return obj

    @staticmethod
    def interchange_equation_n_with_m(matrix: Matrix, n, m):
        y = 0
        for t in range(matrix.cols):
            (matrix.matrix[n][y], matrix.matrix[m][y]) = (matrix.matrix[m][y], matrix.matrix[n][y])
            y += 1
        return matrix

    @staticmethod
    def multiplying_row_n_by_c(matrix: Matrix, n, c):
        for b in range(matrix.cols):
            matrix.matrix[n][b] = matrix.matrix[n][b] * c
        return matrix

    @staticmethod
    def is_column_zero(matrix: Matrix, number_of_column):
        x = 0
        for a in range(matrix.rows):

            if matrix.matrix[a][number_of_column] == 0:
                x += 1
        if x == matrix.rows:
            return True
        return False

    @staticmethod
    def clean_column(matrix: Matrix, i, j, a):
        c = 1 / matrix.matrix[i][j]
        GaussJordan.multiplying_row_n_by_c(matrix, i, c)
        matrix.display(True)
        for x in range(matrix.rows):
            if x != i and matrix.matrix[x][j] != 0:
                z = -(matrix.matrix[x][a] / matrix.matrix[i][j])
                GaussJordan.multiplying_row_n_by_c(matrix, i, z)
                GaussJordan.adding_equation_n_to_m(matrix, i, x)
                c = 1 / matrix.matrix[i][j]
                GaussJordan.multiplying_row_n_by_c(matrix, i, c)
                print('')
                matrix.display(True)
            else:
                pass
