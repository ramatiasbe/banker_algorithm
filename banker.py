from time import sleep
from random import randint, uniform


def need(max_matrix, allocation_matrix):
    need_line = []
    need_matrix = []

    for n in range(len(max_matrix)):
        for m in range(len(max_matrix[n])):
            need_line.append(max_matrix[n][m]-allocation_matrix[n][m])
        need_matrix.append(need_line)
        need_line = []

    return need_matrix


def total(allocation_matrix, available_matrix):
    total = []
    allocation_sum = []
    aux = 0

    for n in range(len(allocation_matrix[1])):
        for m in range(len(allocation_matrix)):
            aux += allocation_matrix[m][n]
        allocation_sum.append(aux)
        aux = 0

    for n in range(len(available_matrix)):
        total.append(allocation_sum[n] + available_matrix[n])

    return total


def fill_matrix(column_number, line_number):
    matrix = []
    matrix_line = []

    if line_number > 1:
        for n in range(line_number):
            for m in range(column_number):
                matrix_line.append(randint(0, 4))
            matrix.append(matrix_line)
            matrix_line = []
    else:
        for n in range(column_number):
            matrix.append(randint(0, 5))

    return matrix


def max_fill(allocation_matrix):
    matrix = []
    matrix_line = []

    for n in range(len(allocation_matrix)):
        for m in range(len(allocation_matrix[n])):
            matrix_line.append(round(allocation_matrix[n][m] * uniform(1, 2)))
        matrix.append(matrix_line)
        matrix_line = []

    return matrix


def print_update(allocation_matrix, max_matrix, available_resource, need_matrix):
    print("A matriz de alocação é:")
    print(allocation_matrix)
    print("\n")
    print("A matriz de alocação máxima é:")
    print(max_matrix)
    print("\n")
    print("A matriz de recursos é:")
    print(available_resource)
    print("\n")
    print("A matriz de necessidade é:")
    print(need_matrix)
    print("\n")
    total_resource = total(allocation_matrix, available_resource)
    print("A matriz de total de recusos é:")
    print(total_resource)
    print("\n")


def generate_process():
    process = []

    for n in range(6):
        process.append(randint(0, 5))

    return process


if __name__ == "__main__":
    process_numbers = 5
    resource_numbers = 6

    allocation_matrix = fill_matrix(resource_numbers, process_numbers)
    max_matrix = max_fill(allocation_matrix)

    available_resource = fill_matrix(6, 1)
    need_matrix = need(max_matrix, allocation_matrix)

    print_update(allocation_matrix, max_matrix, available_resource, need_matrix)

    process_flag = [0] * process_numbers
    order = [0] * process_numbers
    indice = 0

    for k in range(process_numbers):
        process_flag[k] = 0

    valid = True
    while(valid):
        for n in range(len(allocation_matrix)):
            if (process_flag[n] == 0):
                flag = 0

                for m in range(resource_numbers):
                    if (need_matrix[n][m] > available_resource[m]):
                        flag = 1
                        break

                if (flag == 0):
                    order[indice] = n
                    indice += 1
                    for i in range(resource_numbers):
                        available_resource[i] += allocation_matrix[n][i]
                    process_flag[n] = 1

                print('O próximo processo que poderia ser allocado é: P{0}\n'.format(indice))
                print('Atualmente temos a seguinte ordem: \n')

                for i in range(n - 1):
                    print(" P", order[i], " ->", sep="", end="")
                print(" P", order[n - 1], sep="")

        print_update(allocation_matrix, max_matrix, available_resource, need_matrix)
        valid = False

    #print("Situação de 'unsafe' atingida, deadlock encontrado!")