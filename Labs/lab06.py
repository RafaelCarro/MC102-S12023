def igualar_tamanhos(vector1: list[int], vector2: list[int],
                     numero_to_add: int) -> None:
    ''' Transforms the smaller list into the size of the bigger one, adding a
    desired number

    Parameters:
    vector1 -- list
    vector2 -- list
    number_to_add - int
    '''
    if (len(vector1) > len(vector2)):
        for i in range(len(vector1) - len(vector2)):
            vector2.append(numero_to_add)
    elif (len(vector1) < len(vector2)):
        for i in range(len(vector2) - len(vector1)):
            vector1.append(numero_to_add)


def soma_vetores(vector1: list[int], vector2: list[int]) -> list[int]:
    ''' Outputs the list of the sum of the elements of vector1 and vector2

    Parameters:
    vector1 -- list
    vector2 -- list
    '''
    igualar_tamanhos(vector1, vector2, 0)
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i] + vector2[i])
    return vector_result


def subtrai_vetores(vector1: list[int], vector2: list[int]) -> list[int]:
    ''' Outputs the list of the subtraction of the elements of vector1
    by the vector2.

    Parameters:
    vector1 -- list
    vector2 -- list
    '''
    igualar_tamanhos(vector1, vector2, 0)
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i] - vector2[i])
    return vector_result


def multiplica_vetores(vector1: list[int], vector2: list[int]) -> list[int]:
    ''' Outputs the list of the product of the elements of vector1
    by the vector2.

    Parameters:
    vector1 -- list
    vector2 -- list
    '''
    igualar_tamanhos(vector1, vector2, 1)
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i] * vector2[i])
    return vector_result


def divide_vetores(vector1: list[int], vector2: list[int]) -> list[int]:
    ''' Outputs the list of the division of the elements of vector1
    by the vector2.

    Parameters:
    vector1 -- list
    vector2 -- list
    '''
    if (len(vector1) > len(vector2)):
        for i in range(len(vector1) - len(vector2)):
            vector2.append(1)
    elif (len(vector1) < len(vector2)):
        for i in range(len(vector2) - len(vector1)):
            vector1.append(0)
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i] // vector2[i])
    return vector_result


def multiplicacao_escalar(vector1: list[int], escalar: int) -> list[int]:
    ''' Outputs the list of the multiplication of vector1 by an escalar.

    Parameters:
    vector1 -- list
    escalar -- int
    '''
    vector_result = []
    for i in range(len(vector1)):
        vector_result.append(vector1[i] * escalar)
    return vector_result


def n_duplicacao(vector1: list[int], escalar: int) -> list[int]:
    ''' Outputs the list that is the repetition of the vector1
    by escalar times.

    Parameters:
    vector1 -- list
    escalar -- int
    '''
    vector_result = []
    for i in range(escalar):
        for j in range(len(vector1)):
            vector_result.append(vector1[j])
    return vector_result


def soma_elementos(vector1: list[int]) -> int:
    ''' Outputs the unitary list of the sum of all elements of vector1.

    Parameters:
    vector1 -- list
    '''
    result = 0
    for i in range(len(vector1)):
        result += int(vector1[i])
    return result


def produto_interno(vector1: list[int], vector2: list[int]) -> int:
    ''' Outputs the unitary list of the sum of all elements of vector1
    by all elements of vector2.

    Parameters:
    vector1 -- list
    vector2 -- list
    '''
    result = 0
    igualar_tamanhos(vector1, vector2, 1)
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


def multiplica_todos(vector1: list[int], vector2: list[int]) -> list[int]:
    ''' Outputs the list of the product of the elements of vector1
    by all elements of vector2.

    Parameters:
    vector1 -- list
    vector2 -- list
    '''
    vector_result = []
    for i in range(len(vector1)):
        result = 0
        for j in range(len(vector2)):
            result += vector1[i] * vector2[j]
        vector_result.append(result)
    return vector_result


def correlacao_cruzada(vector1: list[int], mascara: list[int]) -> list[int]:
    ''' Outputs a cross correlation of the vector1 by a mascara.

    Parameters:
    vector1 -- list
    mascara -- list
    '''
    vector_result = []
    for i in range(len(vector1) - len(mascara) + 1):
        k = i
        result = 0
        for j in range(len(mascara)):
            result += vector1[k] * mascara[j]
            k += 1
        vector_result.append(result)
    return vector_result


if __name__ == "__main__":
    vector1 = list(map(int, input().split(",")))
    command = input()
    while (command != "fim"):
        if (command == "soma_vetores"):
            vector2 = list(map(int, input().split(",")))
            vector1 = soma_vetores(vector1, vector2)
            print(vector1)
        elif (command == "subtrai_vetores"):
            vector2 = list(map(int, input().split(",")))
            vector1 = subtrai_vetores(vector1, vector2)
            print(vector1)
        elif (command == "multiplica_vetores"):
            vector2 = list(map(int, input().split(",")))
            vector1 = multiplica_vetores(vector1, vector2)
            print(vector1)
        elif (command == "divide_vetores"):
            vector2 = list(map(int, input().split(",")))
            vector1 = divide_vetores(vector1, vector2)
            print(vector1)
        elif (command == "multiplicacao_escalar"):
            escalar = int(input())
            vector1 = multiplicacao_escalar(vector1, escalar)
            print(vector1)
        elif (command == "n_duplicacao"):
            escalar = int(input())
            vector1 = n_duplicacao(vector1, escalar)
            print(vector1)
        elif (command == "soma_elementos"):
            vector_result = []
            vector_result.append(soma_elementos(vector1))
            vector1 = vector_result
            print(vector_result)
        elif (command == "produto_interno"):
            vector2 = list(map(int, input().split(",")))
            vector_result = []
            vector_result.append(produto_interno(vector1, vector2))
            vector1 = vector_result
            print(vector_result)
        elif (command == "multiplica_todos"):
            vector2 = list(map(int, input().split(",")))
            vector1 = multiplica_todos(vector1, vector2)
            print(vector1)
        elif (command == "correlacao_cruzada"):
            mascara = list(map(int, input().split(",")))
            vector1 = correlacao_cruzada(vector1, mascara)
            print(vector1)
        command = input()
