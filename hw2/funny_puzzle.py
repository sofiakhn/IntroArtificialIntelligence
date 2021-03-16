## Sofia Khan
## CS 540 Fall 2020
import heapq
from copy import deepcopy
import numpy as np

################################################## Helper Methods ######################################################


def to2d(array):
    # Helper method which converts a 1d array to 2d array using numpy.
    newarray = np.reshape(array, (3, 3))
    np.shape(newarray)
    return newarray


# Converts numpy array to list
def to_list(state):
    return list(state.reshape(1, 9)[0])


def manhattan (isat, shouldbe):
    x1 = isat[0]
    y1 = isat[1]
    x2 = shouldbe[0]
    y2 = shouldbe[1]
    dist = abs(x1-x2) + abs(y1-y2)
    return dist;


def find_hs(current_board): ## returns the heuristic h which represents manhattan dist to goal
    current_board = to2d(current_board)
    distance = 0
    for i in range(len(current_board)):
        for j in range(len(current_board[i])):
            if(current_board[i][j] == 0):
                continue
            else:
                if(current_board[i][j] == 1): aim = [0,0]
                elif(current_board[i][j] == 2): aim = [0,1]
                elif(current_board[i][j] == 3): aim = [0,2]
                elif(current_board[i][j] == 4): aim = [1,0]
                elif(current_board[i][j] == 5): aim = [1,1]
                elif(current_board[i][j] == 6): aim = [1,2]
                elif(current_board[i][j] == 7): aim = [2,0]
                elif(current_board[i][j] == 8): aim = [2,1]
                elif(current_board[i][j] == 9): aim = [2,2]
                toAdd = manhattan([i,j], aim )
                distance = distance + toAdd
    return distance

def to1d(two_dimensional):
    arr = []
    for i in range(len(two_dimensional)):
        for j in range(len(two_dimensional)):
            arr.append(two_dimensional[i][j])
    return arr


def get_neighbors(state, coordinate):
    x = coordinate[0]
    y = coordinate[1]
    neighbors = [(x+a[0], y+a[1]) for a in
                    [(-1,0), (1,0), (0,-1), (0,1)]
                    if ( (0 <= x+a[0] < len(state)) and (0 <= y+a[1] < len(state)))]
    # print 'printing neighbors:'
    # print neighbors
    return neighbors ## this returns a list of coordinates (list of 2index lists)


def generate_succ(input):
    successors = []
    for i in range(3):
        for j in range(3):
            if input[i][j] == 0:######################### find the empty tile! #############
                zero_x = i
                zero_y = j

    #print 'zero was at', zero_x, ',', zero_y
    neighbor_coords = get_neighbors(input, [zero_x, zero_y])
    num_neighbors = len(neighbor_coords)

    for q in range(num_neighbors):
        copy = deepcopy(input)
        print 'Zero neighbor coords:',neighbor_coords[q]
        neighbor_x = neighbor_coords[q][0]
        neighbor_y = neighbor_coords[q][1]
        value_to_swap = copy[neighbor_x][neighbor_y]
        zero_to_swap = copy[zero_x][zero_y]
        copy[zero_x][zero_y] = value_to_swap
        copy[neighbor_x][neighbor_y] = zero_to_swap
        # value_to_swap, copy[zero_x][zero_y] = copy[zero_x][zero_y], value_to_swap
        copy = to2d(copy)
        print 'here is the successor:'
        print copy
        successors.append(copy)
        copy = input

    print 'zero was at', zero_x, ' ', zero_y

    return successors


# possible successor states
def succ(state):
    state_copy = deepcopy(state)
    state_copy = np.array([state_copy])
    state_copy = state_copy.reshape(3, 3)

    final_arr = []
    # final_arr.append(state)

    goal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])
    goal = goal.reshape(3, 3)
    state2 = deepcopy(state)
    state2 = np.array([state2])
    state2 = state2.reshape(3, 3)
    state3 = deepcopy(state)
    state3 = np.array([state3])
    state3 = state3.reshape(3, 3)
    state4 = deepcopy(state)
    state4 = np.array([state4])
    state4 = state4.reshape(3, 3)
    state5 = deepcopy(state)
    state5 = np.array([state5])
    state5 = state5.reshape(3, 3)
    zero_x = 0
    zero_y = 0
    # get the index of the 0 tile
    for i in range(3):
        for j in range(3):
            if (state_copy[i][j] == 0):
                zero_x = i
                zero_y = j

    # figure out the next move

    # if the tile right of 0 is misplace
    if (zero_y + 1 < 3 and state3[zero_x][zero_y + 1] != goal[zero_x][zero_y + 1]):
        # print("here")
        state3[zero_x][zero_y] = state3[zero_x][zero_y + 1]
        state3[zero_x][zero_y + 1] = 0
        add_arr = state3.flatten()
        final_arr.append(add_arr)

    # if the tile below 0 is misplaced
    if (zero_x + 1 < 3 and state2[zero_x + 1][zero_y] != goal[zero_x + 1][zero_y]):
        state2[zero_x][zero_y] = state2[zero_x + 1][zero_y]
        state2[zero_x + 1][zero_y] = 0
        add_arr = state2.flatten()
        final_arr.append(add_arr)


    if (zero_y - 1 >= 0 and state5[zero_x][zero_y - 1] != 'null'):
        state5[zero_x][zero_y] = state5[zero_x][zero_y - 1]
        state5[zero_x][zero_y - 1] = 0
        add_arr = state5.flatten()
        final_arr.append(add_arr)

    if (zero_x - 1 >= 0 and state4[zero_x - 1][zero_y] != 'null'):
        state4[zero_x][zero_y] = state4[zero_x - 1][zero_y]
        state4[zero_x - 1][zero_y] = 0
        add_arr = state4.flatten()
        final_arr.append(add_arr)

    #print(final_arr)
    return final_arr


# (g+h, ,state, (g,h,parent_index))
# g = total moves so far
# h = sum of mandist of each tile to its goal position

################################################ Expected Methods ####################################################

def print_succ(input_state):
    input_state = to2d(input_state)
    succ_states = succ(input_state)

    for i in range(len(succ_states)):
        succ_states[i] = list(succ_states[i])
    succ_states = list(succ_states)
    succ_states = sorted(succ_states)
    for i in range(len(succ_states)):
        print succ_states[i], ' h=', find_hs(succ_states[i])

## Lots of debugging, not a working method but an attempt at solve
def solve_fail (state):
    print("Solve method called")
    # given a state of the puzzle, perform the A* search algorithm and print the path from
    # the current state to the goal state
    open_pq = [] ## a priority queue
    closed_queue = [] ## a queue. helper list to backtrack. need to check if new additions/succ || node you have already explored
    ## len(closes_pq) = parent index of current child node
    start_state = state
    moves = 0

    # 1. put the start node s on the pq, called OPEN
    start_node = heapq.heappush(open_pq,     ((0+find_hs(start_state)), start_state, (moves,find_hs(start_state),-1)))
    #2. if open is empty, exit with failure

    #3. remove from open and place on closed a node n for which f(n) is minimum (f(n) = g(n) + h(n))
    while len(open_pq)>0:
        open_pq = sorted(open_pq)
        current_node = heapq.heappop(open_pq) ## get node on open w lowest cost
        closed_queue.append(current_node)  ## add this node to closed
        current_node_state = open_pq.get[0]
        print 'current node state:', current_node_state
        goal_state = [1, 2, 3, 4, 5, 6,7, 8, 0]
        print 'goal state: ', goal_state

        if current_node[1]== goal_state: ## reached goal state!
            path = []
            while current_node[1] != start_node[1]: ## save everything from closed into path variable
                path.append(current_node[1])
                current_node = closed_queue.pop(0)
            return path

        ## calculate the succesor states of this current node
        successors = succ(current_node[1])
        for i in range(len(successors)):
            successors[i] = list(successors[i])
        successors = list(successors)
        successors = sorted(successors)
        for i in range(len(successors)):
            heapq.heappush(open_pq, (moves+find_hs(successors[i]), successors[i][1], (moves,find_hs(successors[i]),len(closed_queue))))

        print_succ(current_node[1])
        #print successors


    ## heapq.heappush(pq,(5, [1, 2, 3, 4, 5, 0, 6, 7, 8], (0, 5, -1)))
    ## This format follows  (g+h, state, (g, h, parent_index))           g=total num moves      h=manhattan dist to goal
    # representing both the cost, state and the parent index
    # in A* search (a parent index of -1 denotes the initial state, without any parent)

def solve(state):
    goal_state = [1, 2, 3, 4, 5, 6,7, 8, 0]
    open_pq = []
    closed = []
    g = 0
    h = 0
    start_state = state
    start_cost = find_hs(start_state)
    parent_index = -1
    moves = 0
    heapq.heappush(open_pq, (start_cost + 0, start_state, (0, start_cost, parent_index)))

    while len(open_pq) >0:
        open_pq.sort()
        current = heapq.heappop(open_pq)
        closed.append(current)
        print 'current', current[1]

        if find_hs(current[1]) == 0:
            path = []
            for i in range(len(closed)):

                path.append(closed[i][1])
            return path

        else:
            parent_index += 1
            moves += 1
            successors = succ(current[1])
            for i in range (len(successors)):
                cost = find_hs(successors[i])
                state = successors[i][1]
                heapq.heappush(open_pq, (cost + moves, state, (moves, cost, parent_index)))


################################################ Testing ##############################################################
