def reverter(genome, i, j):
    """
    Revert function: 
    Verifies if the parameters are in range then creates a list with the original elements that are in range, then reverses it.

    Parameters:
    genome - list
    i - positive integer less than len(genome) and j
    j - positive integer less than len(genome)
    """
    genome_slice = []
    if i > len(genome) - 1:
        return None
    if j > len(genome) - 1:
        j = len(genome) - 1
    for x in range(i, j + 1):
        genome_slice.append(genome[x])
    genome_slice.reverse()
    for x in range(i, j + 1):
        genome[x] = genome_slice[x - i]


def transpor(genome, i, j, k):
    '''
    Transpose function: 
    Verifies the parameters, them create two lists with the elements in the range of the transposition them change their place in the original list.

    Parameters:
    genome - list
    i - positive integer less than len(genome), j and k
    j - positive integer less than len(genome) and k
    k - positive integer less than len(genome)
    '''
    if j > len(genome) - 1:
        return None
    if k > len(genome) - 1:
        k = len(genome) - 1
    genome_slice_1 = []
    for x in range(i, j + 1):
        genome_slice_1.append(genome[x])
    genome_slice_2 = []
    for x in range(j + 1, k + 1):
        genome_slice_2.append(genome[x])
    for x in genome_slice_2:
        genome[i] = x
        i += 1
    for x in genome_slice_1:
        genome[i] = x
        i += 1


def combinar(genome, new_genome, i):
    '''
    Combine function: 
    Gets the new genome, and them insert the elements at the desired postion.

    Parameters:
    genome - list
    new_genome - list
    i - positive integer less than len(genome)
    '''
    new_genome = list(new_genome)
    for x in new_genome:
        genome.insert(i, x)
        i += 1


def concatenar(genome, new_genome):
    '''
    Concatenate function: 
    Gets the new genome, and them appends it at the end.

    Parameters:
    genome - list
    new_genome - list
    '''
    new_genome = list(new_genome)
    for x in new_genome:
        genome.append(x)


def remover(genome, i, j):
    '''
    Remove function: 
    Verifies the parameters, and them removes the elements of the desired range.

    Parameters:
    genome - list
    i - positive integer less than len(genome) and j
    j - positive integer less than len(genome)
    '''
    if i > len(genome) - 1:
        return None
    if j > len(genome) - 1:
        j = len(genome) - 1
    while j >= i:
        del genome[i]
        j -= 1


def transpor_e_reverter(genome, i, j, k):
    '''
    Transpose and revert function: 
    It combines two function(revert and combine) to get the desired result.

    Parameters:
    genome - list
    i - positive integer less than len(genome), j and k
    j - positive integer less than len(genome) and k
    k - positive integer less than len(genome)
    '''
    if j > len(genome) - 1:
        return None
    if k > len(genome) - 1:
        k = len(genome) - 1
    transpor(genome, i, j, k)
    reverter(genome, i, k)

def buscar(genome, search):
    '''
    Search function: 
    Gets the search term, them iterates through the list of the genome, if it finds a match, skips the elements of 
    the search term, otherwise, returns to the last + 1 element.

    Parameters:
    genome - list
    search - list
    '''
    search_size = len(search)
    count = 0
    x = 0
    while x in range(len(genome)):
        temp_count = 0
        if search[0] == genome[x]:
            #print("search[0] =", x)
            temp_count += 1
            for y in range(1, search_size):
                if x + y < len(genome):
                    if search[y] == genome[x + y]:
                        #print("search[", y,"] =", x + y)
                        temp_count += 1
                    else:
                        break
            if temp_count == search_size:
                count += 1
                x = x + search_size - 1
        x += 1
    return count


def buscar_bidirecional(genome, search):
    '''
    Bidirectional search funtion: 
    Uses two search functions, one with the original genome, and one inverted.

    Parameters:
    genome - list
    search - list
    '''
    genome_reversed = genome.copy()
    genome_reversed.reverse()
    return buscar(genome, search) + buscar(genome_reversed, search)    


'''gets the genome input, them transforms it into a list'''
genome = input()
genome = list(genome)
'''while loop that checks the desired function and its parameters untill "sair" is in the input.'''
command = input().split()
while (command[0] != "sair"):
    if command[0] == "reverter":
        reverter(genome, int(command[1]), int(command[2]))
    elif command[0] == "transpor":
        transpor(genome, int(command[1]), int(command[2]), int(command[3]))
    elif command[0] == "combinar":
        combinar(genome, command[1] ,int(command[2]))
    elif command[0] == "concatenar":
        concatenar(genome, command[1])
    elif command[0] == "remover":
        remover(genome, int(command[1]), int(command[2]))
    elif command[0] == "transpor_e_reverter":
        transpor_e_reverter(genome, int(command[1]), int(command[2]), int(command[3]))
    elif command[0] == "buscar":
        print(buscar(genome, command[1]))
    elif command[0] == "buscar_bidirecional":
        print(buscar_bidirecional(genome, command[1]))
    elif command[0] == "mostrar":
        output = "".join(genome)
        print(output)
    command = input().split()