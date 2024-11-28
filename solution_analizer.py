from matrix import Matrix
from fractions import Fraction


class As:

    def __init__(self):
        pass

    """
    Solution Analyzer class
    """

    @staticmethod
    def deleting_zero_rows(matrix: Matrix):

        for a in range(len(matrix.matrix)):
            o = 0
            if a <= len(matrix.matrix) - 1:
                for b in range(matrix.cols):
                    if matrix.matrix[a][b] == Fraction(0, 1):
                        o += 1
                    else:
                        pass
                if o == matrix.cols:
                    matrix.matrix.pop(a)
                    As.deleting_zero_rows(matrix)
            else:
                break


    @staticmethod
    def display_system_of_equation_after_elimination(obj: Matrix, convert = lambda a: a):
        number_of_coefficients_equal_to_one = 0
        x = 0
        print("ALTERNATIVE SOLUTION:")
        equation = ""
        for a in obj.matrix:
            y = 0
            for t in range(len(a) - 1):
                if obj.matrix[x][y] > 0 and obj.matrix[x][y] != 1:
                    equation += " +{0}{1}".format(convert(obj.matrix[x][y]), Matrix.unknown[y])
                    y += 1
                elif obj.matrix[x][y] == 0:
                    y += 1
                    pass
                elif obj.matrix[x][y] == 1:
                    if number_of_coefficients_equal_to_one == 0:
                        equation += " {0}".format(Matrix.unknown[y])
                        number_of_coefficients_equal_to_one += 1
                        y += 1
                    else:
                        equation += " +{0}".format(Matrix.unknown[y])
                        y += 1
                else:
                    equation += " {0}{1}".format(convert(obj.matrix[x][y]), Matrix.unknown[y])
                    y += 1
            number_of_coefficients_equal_to_one = 0

            equation += " = {0}".format(convert(obj.matrix[x][y]))
            print(equation)
            equation = ''
            x += 1

    @staticmethod
    def is_system_of_equations_inconsistent(matrix: Matrix):
        for a in range(matrix.rows):
            zeros_count = 0
            for b in range(matrix.cols - 1):
                if matrix.matrix[a][b] == 0:
                    zeros_count += 1
                    continue
                else:
                    break

            if zeros_count == matrix.cols - 1 and matrix.matrix[a][matrix.cols - 1] != 0:
                print(f'\nEquation number {a + 1} has no solutions.')
                return True

        return False