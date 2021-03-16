#Sofia Khan
# CS 540 Fall 2020

#returns a copy of state which fills the jug corresponding to the index in which (0 or 1) to its maximum capacity.
# Do not modify state.
def fill(state, max, which):
    states = state
    if which ==  0:
        states[0] = max[0]
    elif which == 1:
        states[1] = max[1]
    return states

# x = fill(s0, max, 1)
# print(x)
# y = fill(s0, max, 0)
# print(y)

# Returns a copy of state which empties the jug corresponding to the index in which (0 or 1).
# Do not modify state.
def empty(state, max, which):
    states = state
    if which ==  0:
        states[0] = 0
    elif which == 1:
        states[1] = 0
    return states

# returns a copy of state which pours the contents of the jug at index source into the jug at index dest,
# until source is empty or dest is full. Do not modify state. xfer is shorthand for transfer.
def xfer(state, max, source, dest):
    copy = state
    while copy[dest] < max[dest] and copy[source] > 0:
        copy[dest] += 1
        copy[source] -= 1
    return copy


## Debug Statements!

# s0 = [0,0]
# max = [12,23]
# state = [0,0]

# x = fill(s0,max,1)
# print x
# y = fill(s0,max,0)
# print y
#
# zzz = [2,7]
# z = xfer(zzz,max,0,1)
# print z

state = [3,6]
maximum = [12,35]

#prints the list of unique successor states of the current state in any order.
# This function will generate the unique successor states of the current state by applying fill, empty, xfer operations
# on the current state. (Note: You have to apply an operation at every step for generating a successor state.)
def succ(state, max):

    import copy

    curr = copy.deepcopy(state)
    op1 = fill(curr, max, 0)
    print(op1)

    curr1 = copy.deepcopy(state)
    op2 = fill(curr1, max, 1)
    print op2

    curr2 = copy.deepcopy(state)
    op3 = empty(curr2, max, 0)
    print op3

    curr3 = copy.deepcopy(state)
    op4 = empty(curr3, max, 1)
    print op4

    curr4 = copy.deepcopy(state)
    op5 = xfer(curr4, max, 0, 1)
    print op5

    curr5 = copy.deepcopy(state)
    op6 = xfer(curr5, max, 1, 0)
    print op6


succ(state, maximum)

