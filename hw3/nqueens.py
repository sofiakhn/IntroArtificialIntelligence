# Sofia Khan :-)
# CS 540 Fall 2020

import copy
import random
import sys


############################################## HELPER/DISCARD METHODS ##############################################
def succ_attempt_1(state, static_x, static_y):

    n = len(state) #min = 0 and max = n
    successors = []  #This function should return a list of lists, containing all valid successor states of the given
    # current state.

    #the static state is located at state[static_x][static_y]

    #first check if there's a queen on the valid state
    if(state[static_x] != static_y):
        #successors =[] (empty list)
        return successors

    # state = [0,1,2,4,3]
    for i in range(n):
        if(state[i] >= 0 ):
            if(state[i] == static_x and state[static_x] == static_y): #check we're not on static point
                continue
            else:
                new_state = copy.deepcopy(state)
                new_state[i] = new_state[i] - 1
                successors.append(new_state)

    for i in range(n):
        if(state[i] < n-1):
            if (state[i] == static_x and state[static_x] == static_y): #check we're not on static point
                continue
            else:
                new_state = copy.deepcopy(state)
                new_state[i] = new_state[i] + 1
                successors.append(new_state)

    return successors

############################################## REQUIRED METHODS ##############################################
# We WILL allow multiple queens to occupy the same row or the same diagonal line, but not the same column
# We WILL NOT allow moving the queen on the static point.
# If there is not a queen on the static point in the input state, return an empty list
# The returned states should be sorted by the ascending order

def succ(state, x, y):
    return_successors = []
    length = len(state)
    max = length
    i = 0
    if (state[x] != y):
        return_successors = []
    else:
        while i < length:
            if (state[i] == y and x==i):
                i += 1;
                continue;
            else:
                # move to the next index over
                if (state[i] + 1 < max):
                    succ_2 = copy.deepcopy(state)
                    succ_2[i] = state[i] + 1
                    return_successors.append(succ_2)
                if (state[i] - 1 >= 0):
                    succ_3 = copy.deepcopy(state)
                    succ_3[i] = state[i] - 1
                    return_successors.append(succ_3)
                i += 1
    return_successors = sorted(return_successors)
    return return_successors

def f(state):
    attacked = 0
    n = len(state)

    for big_pointer in range(n):  #big POINTER
        row_A = state[big_pointer]

        for small_pointer in range(n): #check for queens in same row and same diagonal
            if(big_pointer==small_pointer):
                continue
            row_B = state[small_pointer]

            if row_A == row_B : ## queens in same row
                attacked += 1
                break
            elif abs(row_A-row_B) == abs(big_pointer-small_pointer):
                attacked += 1
                break

    return attacked


#given the current state, use succ() to generate the successors and return the selected next state
def choose_next(state, x, y):
    if succ(state, x, y) == []: return None ##return none if given bad static point
    candidates = succ(state, x, y)
    candidates.append(state) ## add staying this way to the candidate list
    candidates = sorted(candidates) ## sort the candidates list in ascending order
    chosen = state
    chosen_f_score = 1000
    for i in range(len(candidates)):
        current_f_score = f(candidates[i])
        if current_f_score < chosen_f_score:
            chosen_f_score = current_f_score
            chosen = candidates[i]
    return chosen

def n_queens(state, x, y, print_path=True):
    curr_f = f(state)
    past_f = 0
    while(curr_f!=0):

        strang = str(state) + " - f=" + str(f(state))
        print(strang)
        #print (state ,"-f=",str(f(state)))

        past_f = f(state)
        state = choose_next(state,x,y) #get the next state
        curr_f = f(state)

        if(curr_f == 0):
            str2 = str(state) + " - f=" + str(f(state))
            print(str2)
            break

        if(curr_f == past_f): ## check for reaching a local minimum
            # print(state, "-f=",str(f(state)))
            str3 = str(state) + " - f=" + str(f(state))
            print(str3)
            break

    return state #returning the minimum state in green

#n_queens_restart(n, k, static_x, static_y) -- run the hill-climbing algorithm on an n*n board with random restarts
def n_queens_restart(n,k,static_x,static_y):
    #try up to k times
    random.seed(1)
    random_int_1 = random.randint(0, n-1) ## coordindate value aka when i equals this, set value to...
    random_int_2 = random.randint(0, n-1) ## value at coordinate point
    possible_successors =  []

    counter = 0

    while(counter<k):
        state = [0] * n
        for i in range(n):
            if (i == static_x):
                state[i] = static_y
            else:
                state[i] = random.randint(0, n-1)

        given_state = n_queens(state, static_x, static_y)

        if(f(given_state))==0:
            print_line = str(given_state)+ 'f='+ str(f(given_state))
            print (print_line)
            return

        elif(f(given_state)!= 0):
            possible_successors.append([f(given_state), given_state])

        counter += 1

    possible_successors = sorted(possible_successors, reverse=True)

    for i in range(len(possible_successors)):
        x = possible_successors[i][1]
        y = possible_successors[i][0]
        print (x, '- f=', y)

############################################## TESTING METHODS ##############################################
#
# print 'hi'
# print n_queens([0, 7, 3, 4, 7, 1, 2, 2], 0, 0)