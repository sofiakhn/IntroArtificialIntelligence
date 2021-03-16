#Sofia Khan
# CS 540 Fall 2020

def manhattan_distance(data_point1, data_point2):
    # return the Manhattan distance between two dictionary data points from the data set.
    x = abs(data_point1['PRCP'] - data_point2['PRCP'])
    y = abs(data_point1['TMAX'] - data_point2['TMAX'])
    z = abs(data_point1['TMIN'] - data_point2['TMIN'])
    distance = z + y + x
    return distance


def read_dataset(filename):
    #   return a list of data point dictionaries read from the specified file.
    data = list()
    count = 0
    with open(filename, "r") as f:
        for line in f:
            info = line.split()
            date = info[0]
            prcp = info[1]
            tmax = info[2]
            tmin = info[3]
            rain = info[4]
            dict = {"DATE": date, "TMAX": tmax, 'PRCP': prcp, 'TMIN': tmin, 'RAIN': rain}
            data.append(dict)
    return data

def majority_vote(nearest_neighbors):
    #   return a prediction of whether it is raining or not based on a majority vote of the list of neighbors.
    yes_count = 0
    no_count = 0
    for index in range(len(nearest_neighbors)):
        if(nearest_neighbors[index]['RAIN'] == 'TRUE'):
            yes_count += 1
        else:
            no_count += 1

    if(yes_count >= no_count):
        return 'TRUE'
    else:
        return 'FALSE'

def k_nearest_neighbors(filename, test_point, k, year_interval):
#   using the above functions, return the majority vote prediction for whether it's raining or not on the provided test point.
#   print data[0]['DATE'][:4] how to access just the year of a point

    data = read_dataset(filename)
    neighbors = list()
    year = int(test_point['DATE'][:4])
    lower = year - year_interval
    upper = year + year_interval

    # all points in the year range added into neighbors
    for index in range(len(data)):
        curr_year = int(data[index]['DATE'][:4])
        if curr_year < upper and curr_year > lower :
            #print curr_year
            neighbors.append(data[index])

    neighbors_sorted = sorted(neighbors)
    closest = neighbors_sorted[:k]
    print closest
    return majority_vote(closest)


#   Print statements for testing

# print manhattan_distance({'DATE': '1951-05-19', 'TMAX': 66.0, 'PRCP': 0.0, 'TMIN': 43.0, 'RAIN': 'FALSE'}, {'DATE': '1951-01-27', 'TMAX': 33.0, 'PRCP': 0.0, 'TMIN': 19.0, 'RAIN': 'FALSE'})

# read_dataset("rain.txt")

# print majority_vote([{'DATE': '2015-08-12', 'TMAX': 83.0, 'PRCP': 0.3, 'TMIN': 62.0, 'RAIN': 'TRUE'},
# {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'},
# {'DATE': '2014-12-05', 'TMAX': 55.0, 'PRCP': 0.12, 'TMIN': 44.0, 'RAIN': 'FALSE'},
# {'DATE': '1954-09-08', 'TMAX': 71.0, 'PRCP': 0.02, 'TMIN': 55.0, 'RAIN': 'TRUE'},
# {'DATE': '2014-08-27', 'TMAX': 84.0, 'PRCP': 0.0, 'TMIN': 61.0, 'RAIN': 'FALSE'},
# {'DATE': '2014-08-27', 'TMAX': 84.0, 'PRCP': 0.0, 'TMIN': 61.0, 'RAIN': 'TRUE'}])

# print k_nearest_neighbors("rain.txt", {'DATE': '2014-05-19', 'TMAX': 70.0, 'PRCP': 0.0, 'TMIN': 50.0, 'RAIN': 'FALSE'}, 3, 5 )