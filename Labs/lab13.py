import sys
sys.setrecursionlimit(16385)

def similar_pixel(x, y, seed, t):
    '''
    Recursive functions that goes throught the pixels in an image looking for any similar pixel that fit the formula:
    |color(pixel) - color(seed)| <= t, then fills a similarity matrix that is used in operations in similar pixels.
    '''
    similar_matrix[y][x] = 1
    if x > 0 and y > 0 and abs(pmg_matrix[y - 1][x - 1] - seed) <= t and similar_matrix[y - 1][x - 1] == 0:
        similar_pixel(x - 1, y - 1, seed, t)
    if y > 0 and abs(pmg_matrix[y - 1][x] - seed) <= t and similar_matrix[y - 1][x] == 0:
        similar_pixel(x, y - 1, seed, t)
    if x < pmg_dimension[0] - 1 and y > 0 and abs(pmg_matrix[y - 1][x + 1] - seed) <= t and similar_matrix[y - 1][x + 1] == 0:
        similar_pixel(x + 1, y - 1, seed, t)
    if x < pmg_dimension[0] - 1 and abs(pmg_matrix[y][x + 1] - seed) <= t and similar_matrix[y][x + 1] == 0:
        similar_pixel(x + 1, y, seed, t)
    if x < pmg_dimension[0] - 1 and y < pmg_dimension[1] - 1 and abs(pmg_matrix[y + 1][x + 1] - seed) <= t and similar_matrix[y + 1][x + 1] == 0:
        similar_pixel(x + 1, y + 1, seed, t)
    if y < pmg_dimension[1] - 1 and abs(pmg_matrix[y + 1][x] - seed) <= t and similar_matrix[y + 1][x] == 0:
        similar_pixel(x, y + 1, seed, t)
    if x > 0 and y < pmg_dimension[1] - 1 and abs(pmg_matrix[y + 1][x - 1] - seed) <= t and similar_matrix[y + 1][x - 1] == 0:
        similar_pixel(x - 1, y + 1, seed, t)
    if x > 0 and abs(pmg_matrix[y][x - 1] - seed) <= t and similar_matrix[y][x - 1] == 0:
        similar_pixel(x - 1, y, seed, t)

def bucket(fill_color, t, x, y):
    '''
    Fills every similar pixel in the image with the choosen color.
    '''
    color = pmg_matrix[y][x]
    similar_pixel(x, y, color, t)
    for i in range(pmg_dimension[1]):
        for j in range(pmg_dimension[0]):
            if similar_matrix[i][j] == 1:
                pmg_matrix[i][j] = fill_color
                similar_matrix[i][j] = 0

def negative(t, x, y):
    '''
    Applies the negative effect to every similar pixel in the image.
    '''
    color = pmg_matrix[y][x]
    similar_pixel(x, y, color, t)
    for i in range(pmg_dimension[1]):
        for j in range(pmg_dimension[0]):
            if similar_matrix[i][j] == 1:
                pmg_matrix[i][j] = pmg_max - pmg_matrix[i][j]
                similar_matrix[i][j] = 0
    
def mask(t, x, y):
    '''
    Applies a mask to every similar pixel in the image.
    '''
    color = pmg_matrix[y][x]
    similar_pixel(x, y, color, t)
    for i in range(pmg_dimension[1]):
        for j in range(pmg_dimension[0]):
            if similar_matrix[i][j] == 1:
                pmg_matrix[i][j] = 0
                similar_matrix[i][j] = 0
            else:
                pmg_matrix[i][j] = 255

def save_file(save_path):
    '''
    Saves the edited image in a new file, compliyng with the P2 pmg standard.
    '''
    saved_file = open(save_path, "w")
    saved_file.write("P2\n")
    saved_file.write("# Imagem criada pelo lab13\n")
    saved_file.write(str(pmg_dimension[0]) + " " + str(pmg_dimension[1]) + "\n")
    saved_file.write(str(pmg_max))
    for x in range(pmg_dimension[1]):
        saved_file.write("\n")
        for y in range(pmg_dimension[0] - 1):
            saved_file.write(str(pmg_matrix[x][y]) + " ")
        saved_file.write(str(pmg_matrix[x][pmg_dimension[0] - 1]))
    saved_file.close()

def input_to_functions(input_string):
    '''
    Gets the input then calls the correspondent function.
    '''
    input_string = input_string.split()
    if input_string[0] == "bucket":
        bucket(int(input_string[1]), int(input_string[2]), int(input_string[3]), int(input_string[4]))
    elif input_string[0] == "negative":
        negative(int(input_string[1]), int(input_string[2]), int(input_string[3]))
    elif input_string[0] == "cmask":
        mask(int(input_string[1]), int(input_string[2]), int(input_string[3]))
    else:
        save_file(input_string[1])

if __name__ == "__main__":
    #Getting the image path and number of operations
    file_path = input()
    N_actions = int(input())

    #Getting info from PMG image
    with open(file_path, "r") as image:
        pmg_type = image.readline()
        pmg_header = image.readline()
        pmg_dimension = image.readline().split()
        pmg_dimension = [int(pmg_dimension[0]), int(pmg_dimension[1])]
        pmg_max = int(image.readline())
        pmg_matrix = []
        for i in range(pmg_dimension[1]):
            line = image.readline().split()
            x = []
            for j in range(pmg_dimension[0]):
                x.append(int(line[j]))
            pmg_matrix.append(x)
            
    #Setting matrixes for similarity analisys
    similar_matrix = []
    for i in range(pmg_dimension[1]):
        _ = []
        for j in range(pmg_dimension[0]):
            _.append(0)
        similar_matrix.append(_)

    #Running functions
    for i in range(N_actions):
        action = input()
        input_to_functions(action)
    image.close()
    print("P2")
    print("# Imagem criada pelo lab13")
    print(str(pmg_dimension[0]) + " " + str(pmg_dimension[1]))
    print(str(pmg_max))
    for x in range(pmg_dimension[1]):
        print(*pmg_matrix[x])
