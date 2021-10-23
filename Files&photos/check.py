def pixel_is_black(arr, x, y):
    if arr[x, y] == 1:
        return True
    return False


# steps one and two, condition two
def pixel_has_3_to_8_black_neighbors(arr, x, y):
    # pixel values can only be 0 or 1, so simply check if sum of
    # neighbors is between 3 and 8
    if (3 <= arr[x, y - 1] + arr[x + 1, y - 1] + arr[x + 1, y] + arr[x + 1, y + 1] +
            arr[x, y + 1] + arr[x - 1, y + 1] + arr[x - 1, y] + arr[x - 1, y - 1] <= 8):
        return True
    return False


# steps one and two, condition three
def pixel_has_1_white_to_black_neighbor_transition(arr, x, y):
    # neighbors is a list of neighbor pixel values; neighbor P2 appears
    # twice since we will cycle around P1.
    neighbors = [arr[x, y - 1], arr[x + 1, y - 1], arr[x + 1, y], arr[x + 1, y + 1],
                 arr[x, y + 1], arr[x, y + 1], arr[x - 1, y], arr[x - 1, y - 1],
                 arr[x, y - 1]]
    # zip returns iterator of tuples composed of a neighbor and next neighbor
    # we then check if the neighbor and next neighbor is a 0 -> 1 transition
    # finally, we sum the transitions and return True if there is only one
    transitions = sum((a, b) == (0, 1) for a, b in zip(neighbors, neighbors[1:]))
    if transitions == 1:
        return True
    return False


# step one condition four
def at_least_one_of_P2_P4_P6_is_white(arr, x, y):
    # if at least one of P2, P4, or P6 is 0 (white), logic statement will
    # evaluate to false.
    if not (arr[x, y - 1] and arr[x + 1, y] and arr[x, y + 1]):
        return True
    return False


# step one condition five
def at_least_one_of_P4_P6_P8_is_white(arr, x, y):
    # if at least one of P4, P6, or P8 is 0 (white), logic statement will
    # evaluate to false.
    if not (arr[x + 1, y] and arr[x, y + 1] and arr[x - 1, y]):
        return True
    return False


# step two condition four
def at_least_one_of_P2_P4_P8_is_white(arr, x, y):
    # if at least one of P2, P4, or P8 is 0 (white), logic statement will
    # evaluate to false.
    if not (arr[x, y + 1] and arr[x + 1, y] and arr[x - 1, y]):
        return True
    return False


# step two condition five
def at_least_one_of_P2_P6_P8_is_white(arr, x, y):
    # if at least one of P2, P6, or P8 is 0 (white), logic statement will
    # evaluate to false.
    if not (arr[x, y - 1] and arr[x, y + 1] and arr[x - 1, y]):
        return True
    return False


def howmany_neighbor(arr, x, y):
    return 24 - (arr[x + 1, y - 1] + arr[x + 1, y] + arr[x + 1, y + 1] + arr[x + 1, y - 2] + arr[x + 1, y + 2] +
                 arr[x + 2, y - 1] + arr[x + 2, y] + arr[x + 2, y + 1] + arr[x + 2, y - 2] + arr[x + 2, y + 2] +
                 arr[x - 1, y - 1] + arr[x - 1, y] + arr[x - 1, y + 1] + arr[x - 1, y - 2] + arr[x - 1, y + 2] +
                 arr[x - 2, y - 1] + arr[x - 2, y] + arr[x - 2, y + 1] + arr[x - 2, y - 2] + arr[x - 2, y + 2] +
                 arr[x, y - 1] + arr[x, y + 1] + arr[x, y + 2] + arr[x, y - 2])


def howmany_neighbor2(arr, x, y):
    return (8 - (arr[x + 1, y - 1] + arr[x + 1, y] + arr[x + 1, y + 1] +
                 arr[x - 1, y - 1] + arr[x - 1, y] + arr[x - 1, y + 1] +
                 arr[x, y - 1] + arr[x, y + 1]))


def make_3_angle(thresh):
    c = thresh.copy()
    for i in range(1, thresh.shape[0] - 2):
        for j in range(1, thresh.shape[1] - 2):
            if thresh[i][j] == 0:
                if howmany_neighbor2(thresh, i, j) == 3 and howmany_neighbor(thresh, i, j) == 5 and (
                        (thresh[i - 1][j + 1] == 0 and thresh[i - 1][j - 1] == 0) or
                        (thresh[i + 1][j + 1] == 0 and thresh[i + 1][j - 1] == 0) or
                        (thresh[i - 1][j - 1] == 0 and thresh[i + 1][j - 1] == 0) or
                        (thresh[i - 1][j + 1] == 0 and thresh[i + 1][j - 1] == 0) or
                        (thresh[i][j + 1] == 0 and thresh[i + 1][j] == 0 and thresh[i - 1][j] == 0) or
                        (thresh[i][j - 1] == 0 and thresh[i + 1][j] == 0 and thresh[i - 1][j] == 0) or
                        (thresh[i][j + 1] == 0 and thresh[i][j - 1] == 0 and thresh[i - 1][j] == 0) or
                        (thresh[i][j + 1] == 0 and thresh[i][j - 1] == 0 and thresh[i + 1][j] == 0)):
                    c[i][j] = 0
                else:
                    c[i][j] = 1
    return c


def make_1_angle(thresh):
    b = thresh.copy()
    for i in range(1, thresh.shape[0] - 5):
        for j in range(1, thresh.shape[1] - 5):
            if thresh[i][j] == 0:
                if howmany_neighbor2(thresh, i, j) == 1 and howmany_neighbor(thresh, i, j) == 2:
                    b[i][j] = 0
                else:
                    b[i][j] = 1
    return b
