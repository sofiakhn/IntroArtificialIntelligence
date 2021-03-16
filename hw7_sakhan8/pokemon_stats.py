## Sofia Khan
import csv
import numpy as np
from scipy.spatial import distance


def load_data(filepath):
    with open('Pokemon.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        pokemon = {}
        for item in reader:
            pokemon[i] = {}
            pokemon[i]['Name'] = item['Name']
            pokemon[i]['Type 1'] = item['Type 1']
            pokemon[i]['Type 2'] = item['Type 2']
            pokemon[i]['Total'] = int(item['Total'])
            pokemon[i]['HP'] = int(item['HP'])
            pokemon[i]['Attack'] = int(item['Attack'])
            pokemon[i]['Defense'] = int(item['Defense'])
            pokemon[i]['Sp. Atk'] = int(item['Sp. Atk'])
            pokemon[i]['Sp. Def'] = int(item['Sp. Def'])
            pokemon[i]['Speed'] = int(item['Speed'])
            i += 1
            if (i > 19):
                break
    return pokemon


def calculate_x_y(stats):
    attack = stats['Attack']
    specialAttack = stats['Sp. Atk']
    speed = stats['Speed']
    defense = stats['Defense']
    specialDefense = stats['Sp. Def']
    hp = stats['HP']

    x = attack + specialAttack + speed
    y = defense + specialDefense + hp
    ret = (x, y)
    return ret

def find_closest_brute_force(array):
    result = {}
    result["p1"] = array[0]
    result["p2"] = array[1]
    result["distance"] = np.sqrt((array[0][1] - array[1][1]) ** 2
                                 + (array[0][2] - array[1][2]) ** 2)
    result["p1 number"] = 0
    result["p2 number"] = 0


    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            distance = np.sqrt((array[i][1] - array[j][1]) ** 2
                               + (array[i][2] - array[j][2]) ** 2)
            if distance < result["distance"]:
                result["p1"] = array[i]
                result["p2"] = array[j]
                result["distance"] = distance
                result["p1 number"] = i
                result["p2 number"] = j
    return result


def calculate_distance(p1, p2):
    d = distance.euclidean(p1, p2)
    return d ## return the euclidean distance.

def hac(array):
    forest = {}
    ## Number each of your starting data points from 0 to m-1. These are their original cluster numbers.
    s = (19, 4)
    final_matrix = np.zeros(s)

    forest = np.zeros((20, 3))
    for i in range(20):
        forest[i][0] = i  ####### original_cluster[i][0] will give you cluster number
        forest[i][1] = dataset[i][0]  #####cluster x value
        forest[i][2] = dataset[i][1]  ##### cluster y value
    z = 20
    # print("Forest:" )
    # print(forest)

    ## For each row,
    for z in range(19):
        result = find_closest_brute_force(forest)
        final_matrix[z][0] = result['p1 number']
        final_matrix[z][1] = result['p2 number']
        final_matrix[z][2] = result['distance'] + z
        final_matrix[z][3] = 2

        np.delete(forest, np.where(forest[z] == result['p1 number']))
        np.delete(forest, np.where(forest[z] == result['p2 number']))
        z += 1

    result = np.asamatrix(final_matrix)
    return result

##################################### TESTING ############################

pokeDict = load_data('Pokemon.csv')
#
# for i in range(0, 20):
#     print( i ) ## i is the cluster number.
#     print(calculate_x_y(pokeDict[i]))

dataset = []
for i in range(20):
    to_add = calculate_x_y(pokeDict[i])
    dataset.append(to_add)


x = hac(dataset)
print (x)

##################################### TESTING ############################

def hac1(dataset):
    ## Number each of your starting data points from 0 to m-1. These are their original cluster numbers.
    s = (20,4)
    final_matrix = np.zeros(s)

    forest = np.zeros((20,3))
    for i in range(20):
        forest[i][0] = i ####### original_cluster[i][0] will give you cluster number
        forest[i][1] = dataset[i][0] #####cluster x value
        forest[i][2] = dataset[i][1] ##### cluster y value
    z = 20
    # print("Forest:" )
    # print(forest)


    ## For each row,
    for z in range(20):
        result = find_closest_brute_force(forest)
        final_matrix[z][0] = result['p1 number']
        final_matrix[z][1] = result['p2 number']
        final_matrix[z][2] = result['distance']
        final_matrix[z][3] = 2

        np.delete(forest, np.where(forest[z] == result['p1 number']))
        np.delete(forest, np.where(forest[z] == result['p2 number']))

        np.append()
        z+= 1

    # print(final_matrix)
