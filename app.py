from matrix import Matrix
from solution_analizer import As
from gauss_jordan_operations import GaussJordan
from matrix_multiplier import Dmr


class App:
    def __init__(self):
        pass

    def mainloop(self):
        print("\033[1mTHIS APP IS MADE TO HELP YOU SOLVE MATRIX EQUATION.\033[0m")

        set_ = ['solve system of equation', 'multiply matrices', 'add matrices', 'subtract matrices']

        def display_choice(List):
            i = 1
            for n in List:
                print(i, " - ", n)
                i += 1
            x = input("Select option or click enter to exit:")
            return x

        while True:
            print("\n")
            choice = display_choice(set_)
            if not choice:
                print("Process finished")
                break
            else:
                try:
                    choice = int(choice)
                    if choice in [i for i in range(1, len(set_) + 1)]:
                        if choice == 1:
                            print('\n')
                            self.main()
                        elif choice in [2, 3, 4]:
                            m = "\n \033[1mA * B\033[0m \n" if choice == 2 else "\n \033[1mA + B\033[0m \n" if choice == 3 else "\n \033[1mA - B\033[0m \n"
                            print(m)
                            (rows1, columns1) = Dmr.dimensions_entry("A")
                            (rows2, columns2) = Dmr.dimensions_entry("B")
                            print(f"\ninsert data in rows for Matrix A as in example (a b c d ...).")
                            A = Dmr.create_matrix(rows1, columns1)
                            print(f"\ninsert data in rows for Matrix B as in example (a b c d ...).")
                            B = Dmr.create_matrix(rows2, columns2)
                            result = A*B if choice == 2 else B + A if choice == 3 else A - B
                            print("\n")
                            result.display()
                            App.matrix_loop(result)

                    else:
                        print("\n Invalid option \n")
                except ValueError:
                    print("\n you must enter an integer \n")
                except Exception as e:
                    print(e)

    def main(self):
        rows, columns = self.data_entry()
        A = Matrix.create_matrix(rows, columns)
        print('\n' * 50)
        Matrix.display_matrix_equation(A)
        print('\n')
        Matrix.display_system_of_equation(A)
        print('\n')
        print('Augmented matrix of the system: ')
        A.display(True)
        print('\n' * 2)
        input('Press any key to continue...')

        self.Gauss_Jordan_Elimination(A)

        Zero_matrix = Matrix(A.matrix.copy())
        As.deleting_zero_rows(A)
        if A.matrix:
            print('')
            Matrix.display_system_of_equation(A)
            print('')
            Matrix.display_matrix_equation(A)

            if As.is_system_of_equations_inconsistent(A):
                print('THE SYSTEM OF EQUATIONS IS INCONSISTENT!')
            else:
                print('\n')
                # As.display_system_of_equation_after_elimination(A)
                As.display_system_of_equation_after_elimination(A)
                As.display_system_of_equation_after_elimination(A, float)
        else:
            print("\n" * 4, "The matrix is zero: ")
            Zero_matrix.display(True)

    @staticmethod
    def matrix_loop(result: Matrix):
        set_ = ['solve system for this matrix', 'multiply matrix', 'add matrix', 'subtract matrix']

        def display_choice(List):
            i = 1
            for n in List:
                print(i, " - ", n)
                i += 1
            x = input("Select option or click enter to exit:")
            return x

        while True:
            print("\n")
            choice = display_choice(set_)
            if not choice:
                print("Process finished")
                break
            else:
                try:
                    choice = int(choice)
                    if choice in [i for i in range(1, len(set_) + 1)]:
                        if choice == 1:
                            App.Gauss_Jordan_Elimination(result)
                            print('-'*37)
                            break
                        elif choice == 2:
                            print('A:')
                            result.display()
                            print("\n \033[1mA * B\033[0m \n")
                            (rows1, columns1) = Dmr.dimensions_entry("B")
                            print(f"\ninsert data in rows for Matrix B as in example (a b c d ...).")
                            B = Dmr.create_matrix(rows1, columns1)
                            result = result * B
                            result.display()
                        elif choice == 3:
                            print('A:')
                            result.display()
                            print("\n \033[1mA + B\033[0m \n")
                            print(f"\ninsert data in rows for Matrix B as in example (a b c d ...).")
                            B = Dmr.create_matrix(result.rows, result.cols)
                            result = result + B
                            result.display()
                        elif choice == 4:
                            print('A:')
                            result.display()
                            print("\n \033[1mA - B\033[0m \n")
                            print(f"\ninsert data in rows for Matrix B as in example (a b c d ...).")
                            B = Dmr.create_matrix(result.rows, result.cols)
                            result = result - B
                            result.display()
                    else:
                        print("\n Invalid option \n")
                except ValueError:
                    print("\n you must enter an integer \n")
                except Exception as e:
                    print(e)

    @staticmethod
    def Gauss_Jordan_Elimination(matrix: Matrix):
        k = 0
        l = 0

        for a in range(matrix.cols - 1):
            if l < matrix.cols - 1 and k < matrix.rows:
                print(f'\n>>>>> [{k}]\n')
                if GaussJordan.is_column_zero(matrix, k):
                    print(f'Column {k + 1} is all zeroes, moving to next')
                    pass
                elif matrix.matrix[k][l] == 0 and k + 1 < matrix.rows:
                    for x in range(matrix.rows - k - 1):
                        if matrix.matrix[k + x + 1][l] != 0:
                            z = k + x + 1
                            GaussJordan.interchange_equation_n_with_m(matrix, k, z)
                            print(f'Swapping equation number {k + 1} with equation number {z + 1} > {k + 1}')
                            matrix.display()
                            break
                        elif x == matrix.rows - k - 2:
                            print('\nNo rows with a non-zero coefficient, moving to the next')
                            pass
                    if matrix.matrix[k][l] == 0:
                        pass
                    else:
                        GaussJordan.clean_column(matrix, k, l, a)
                elif matrix.matrix[k][l] == 0 and k + 1 >= matrix.rows:
                    break
                else:
                    GaussJordan.clean_column(matrix, k, l, a)
                k += 1
                l += 1
            else:
                break

    @staticmethod
    def data_entry():
        message_input = "\033[31mYou must provide a positive integer.\033[0m"
        while True:
            try:
                rows = int(input("Enter the number of equations: "))
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
                columns = int(input("Enter the number of unknowns: ")) + 1
            except ValueError:
                print(message_input)
                pass
            else:
                if columns > 1:
                    break
                else:
                    print(message_input)
        return rows, columns