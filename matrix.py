from fractions import Fraction


class Matrix:
    unknown = ['x', 'y', 'z', 's', 't', 'u', 'w', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


    def __init__(self, list_input: list):
        if not all(isinstance(i, list) for i in list_input):
            raise Exception("All values must be nested in a list")
        if not list_input[0]:
            raise Exception("input can not be empty.")
        if not all(len(list_input[0]) == len(i) for i in list_input):
            raise Exception("This is not Matrix. Rows length must be equal.")

        self.matrix = list_input
        self.cols = len(list_input[0])

    @property
    def rows(self):
        return len(self.matrix)


    def display(self, unknownBool=False):
        if self.cols <= 1:
            unknownBool = False

        length = [0 for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                length[j] = len(str(self.matrix[i][j])) if length[j] <= len(str(self.matrix[i][j])) else length[j]

        for t in range(len(self.matrix)):
            row_i = '\033[1m[\033[0m' if len(self.matrix) == 1 else '\033[1m⎡\033[0m' if t == 0 else '\033[1m⎣\033[0m' if t == len(self.matrix) - 1 else '\033[1m⎢\033[0m'
            for b in range(len(self.matrix[0])):
                row_i += '{:^{}}'.format(str(self.matrix[t][b]), length[b])
                row_i += '  ' if b < self.cols-1 else ''
            row_i += '\033[1m]\033[0m' if len(self.matrix) == 1 else '\033[1m⎤\033[0m' if t == 0 else '\033[1m⎦\033[0m' if t == len(self.matrix) - 1 else '\033[1m⎢\033[0m'
            print(row_i)

        message_unknown = ' '
        if unknownBool:
            for t in range(len(self.matrix[0])-1):
                message_unknown += '\033[1m{:^{}}\033[0m  '.format(Matrix.unknown[t], length[t])
        print(message_unknown)

    def display_matrix_equation(self):
        if self.cols <= 1:
            return
        if len(self.matrix) != len(self.matrix[0])-1:
            return

        print('Matrix equation (A * x = B): ')
        A = []
        for i in range(len(self.matrix)):
            A.append(self.matrix[i][0:-1])
        B = []
        for i in range(len(self.matrix)):
            B.append(self.matrix[i][-1])
        X = [Matrix.unknown[i] for i in range(len(self.matrix[0]))]

        length = [0 for _ in range(len(A[0]))]
        for i in range(len(A)):
            for j in range(len(A[i])):
                length[j] = len(str(A[i][j])) if length[j] <= len(str(A[i][j])) else length[j]

        Message = ['' for _ in range(len(A))]
        for t in range(len(Message)):
            Message[t] += '\033[1m[\033[0m' if len(A) == 1 else '\033[1m⎡\033[0m' if t == 0 else '\033[1m⎣\033[0m' if t == len(A) - 1 else '\033[1m⎢\033[0m'
            for b in range(len(A[0])):
                Message[t] += '{:^{}}'.format(str(A[t][b]), length[b])
                Message[t] += ' ' if b < len(A) - 1 else ''
            Message[t] += '\033[1m]\033[0m' if len(A) == 1 else '\033[1m⎤\033[0m' if t == 0 else '\033[1m⎦\033[0m' if t == len(A) - 1 else '\033[1m⎢\033[0m'

        for t in range(len(A)):
            Message[t] += ' * ' if t == int(len(A) / 2) else '   '

        for t in range(len(Message)):
            Message[t] += '\033[1m[\033[0m' if len(B) == 1 else '\033[1m⎡\033[0m' if t == 0 else '\033[1m⎣\033[0m' if t == len(B) - 1 else '\033[1m⎢\033[0m'
            Message[t] += X[t]
            Message[t] += '\033[1m]\033[0m' if len(B) == 1 else '\033[1m⎤\033[0m' if t == 0 else '\033[1m⎦\033[0m' if t == len(B) - 1 else '\033[1m⎢\033[0m'

        for t in range(len(A)):
            Message[t] += ' = ' if t == int(len(A) / 2) else '   '

        length = 1
        for i in range(len(B)):
            length = len(str(B[i])) if length <= len(str(B[i])) else length

        for t in range(len(A)):
            Message[t] += '\033[1m[\033[0m' if len(B) == 1 else '\033[1m⎡\033[0m' if t == 0 else '\033[1m⎣\033[0m' if t == len(B) - 1 else '\033[1m⎢\033[0m'
            Message[t] += '{:^{}}'.format(str(B[t]), length)
            Message[t] += '\033[1m]\033[0m' if len(B) == 1 else '\033[1m⎤\033[0m' if t == 0 else '\033[1m⎦\033[0m' if t == len(B) - 1 else '\033[1m⎢\033[0m'

        for line in Message:
            print(line)

    def display_system_of_equation(self):
        if self.cols <= 1:
            return

        n = 0
        tem = len(self.matrix[0]) - 1
        print("Resulting system of equations:")
        for vector in self.matrix:
            equation = ""

            if len(self.matrix) == 1:
                equation += '\033[1m{\033[0m'
            elif n == 0:
                equation += '\033[1m⎡\033[0m'
            elif n == len(self.matrix)-1:
                equation += '\033[1m⎣\033[0m'
            elif n == int(len(self.matrix) / 2 - 1 / 3):
                equation += '\033[1m⎨\033[0m'
            else:
                equation += '\033[1m⎢\033[0m'

            for var in range(len(vector) - 1):
                tem = var
                if self.matrix[n][var] > 0 and self.matrix[n][var] != 1:
                    equation += " +{0}{1}".format(self.matrix[n][var], Matrix.unknown[var])
                elif self.matrix[n][var] == 0:
                    equation += " +0{0}".format(Matrix.unknown[var]) if var == 0 else ""
                elif self.matrix[n][var] == 1:
                    equation += " +{0}".format(Matrix.unknown[var])
                elif self.matrix[n][var] == -1:
                    equation += " -{0}".format(Matrix.unknown[var])
                else:
                    equation += " {0}{1}".format(self.matrix[n][var], Matrix.unknown[var])

            equation += " = {0}".format(self.matrix[n][tem + 1])
            print(equation)
            n += 1

    def __add__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise Exception('Dimensions of the Matrices must be equal.')
        new_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(new_matrix)

    def __sub__(self, other):
        if self.cols != other.cols or self.rows != other.rows:
            raise Exception('Dimensions of the Matrices must be equal.')
        new_matrix = [[self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(new_matrix)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception("You cant multiply Matrices this sizes.")
        new_matrix = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)]
            for i in range(self.rows)]
        return Matrix(new_matrix)

    @ classmethod
    def create_matrix(cls, rows, columns):
        matrix = []
        print("Enter the elements of the system of equations:")

        for i in range(rows):
            print(f'Equation number ({i+1})')
            equation = []
            a = 0
            for j in range(columns - 1):
                message = f'Enter the coefficient for {Matrix.unknown[a]}: '
                while True:
                    try:
                        value = Fraction(input(message))
                    except ValueError:
                        print("\033[31mYou must enter a number.\033[0m")
                        pass
                    else:
                        break
                element = value
                equation.append(element)
                a += 1
            while True:
                try:
                    free_value = Fraction(input("Enter the free term of the equation:  "))
                except ValueError:
                    print("\033[31mYou must enter a number.\033[0m")
                    pass
                else:
                    break
            equation.append(free_value)
            matrix.append(equation)
        return cls(matrix)



