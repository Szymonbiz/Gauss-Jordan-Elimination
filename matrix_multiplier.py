from fractions import Fraction

from matrix import Matrix
import re


class Dmr:

    @staticmethod
    def dimensions_entry(A):

        message_input = "\033[31mYou must provide a positive integer.\033[0m"
        while True:
            try:
                rows = int(input(f"Enter number of colmuns of matrix {A}: "))
            except ValueError:
                print(message_input)
                pass
            else:
                if rows > 0:
                    break
                else:
                    print(message_input)

        while True:
            try:
                columns = int(input(f"Enter number of rows of matrix {A}: "))
            except ValueError:
                print(message_input)
                pass
            else:
                if columns > 0:
                    break
                else:
                    print(message_input)
        return rows, columns

    @staticmethod
    def create_matrix(rows, columns):
        A = []
        for i in range(rows):
            while True:
                row_i = input(f"[{columns}] insert data in row {i+1}: ")
                row_i = row_i.strip(" ")
                if not all(x in set("./0123456789 -") for x in row_i):
                    print("Invalid input")
                elif not row_i[0] in set("0123456789-"):
                    print("Invalid input")
                elif not row_i[-1]  in set("0123456789"):
                    print("Invalid input")
                elif len(row_i.split(" ")) != columns:
                    print("Invalid input")
                else:
                    row_i = row_i.split(" ")
                    data = [Fraction(x) for x in row_i]
                    A.append(data)
                    break
        return Matrix(A)




