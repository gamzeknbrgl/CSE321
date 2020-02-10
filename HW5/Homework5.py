# QUESTION 1
def optimalPlan(NY, SF, M):
    n = len(SF)
    optNi = [0 for i in range(0, n)]
    optSi = [0 for i in range(0, n)]
    for i in range(0, n):
        # if the optimal plan ends in NY
        optNi[i] = NY[i] + min(optNi[i - 1], M + optSi[i - 1])
        # if the optimal plan ends in SF
        optSi[i] = SF[i] + min(optSi[i - 1], M + optNi[i - 1])
    return min(optNi[n - 1], optSi[n - 1])


# QUESTION 2
def optimal_list_of_sessions(start, finish):
    n = len(finish)
    # sort the activities according their finish time
    finish.sort()
    selected_sessions = []
    # the first activity
    i = 0
    selected_sessions.append(i)
    for j in range(n):
        if start[j] >= finish[i]:
            selected_sessions.append(j)
            i = j
    return selected_sessions


# QUESTION 3
def find_subset(arr, sum):
    possible_set = []
    locations = [(sum, len(arr), [])]

    while len(locations) > 0:
        i, j, curr = locations.pop()
        if i < 0 or j < 1:
            continue
        if arr[j - 1] == i:
            possible_set.append(curr + [i])
            return possible_set
        elif arr[j - 1] > i:
            locations.append((i, j - 1, curr))
        elif arr[j - 1] < i:
            locations.append((i, j - 1, curr))
            locations.append((i - arr[j - 1], j - 1, curr + [arr[j - 1]]))


# QUESTION 4
def comparison(ch1, ch2):
    if ch1 == ch2:
        return 2
    elif ch1 == '-' or ch2 == '-':
        return -1
    else:
        return -2


def sequence_cost(s1, s2):
    gap = -1
    m, n = len(s1), len(s2)
    cost = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # Initialize the array of the row 0 and column 0 with j*gap and i*gap
    for i in range(m + 1):
        cost[i][0] = gap * i
    for j in range(n + 1):
        cost[0][j] = gap * j

    # Matrix filling is the step that filling the matrix with maximum scores.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = cost[i - 1][j - 1] + comparison(s1[i - 1], s2[j - 1])
            delete = cost[i - 1][j] + gap
            insert = cost[i][j - 1] + gap
            cost[i][j] = max(diag, delete, insert)
    align1, align2 = '', ''
    i, j = m, n

    # Traceback the matrix for find the best alignment
    while i > 0 and j > 0:
        # Check the neighbours for find the find the maximum score
        curr = cost[i][j]
        diag = cost[i - 1][j - 1]
        left = cost[i][j - 1]
        up = cost[i - 1][j]
        if curr == diag + comparison(s1[i - 1], s2[j - 1]):
            a1, a2 = s1[i - 1], s2[j - 1]
            i, j = i - 1, j - 1
        elif curr == up + gap:
            a1, a2 = s1[i - 1], '-'
            i -= 1
        elif curr == left + gap:
            a1, a2 = '-', s2[j - 1]
            j -= 1
        align1 += a1
        align2 += a2
    while i > 0:
        a1, a2 = s1[i - 1], '-'
        align1 += a1
        align2 += a2
        i -= 1
    while j > 0:
        a1, a2 = '-', s2[j - 1]
        align1 += a1
        align2 += a2
        j -= 1
    align1 = align1[::-1]
    align2 = align2[::-1]
    length_seq = len(align2)
    c = s2[len(s2) - 1]
    count = 0
    for i in range(length_seq):
        count = count + 1
        if align2[i] == c:
            break
    align = ''
    cost = 0
    ident = 0
    for i in range(count):
        a1 = align1[i]
        a2 = align2[i]
        if a1 == a2:
            align += a1
            ident += 1
            cost += comparison(a1, a2)
        else:
            cost += comparison(a1, a2)
            align += ' '
    return cost


# QUESTION 5
def array_sum_operations(arr):
    total_sum = 0
    arr.sort()
    arr2 = [0] * len(arr)
    op1 = arr[0] + arr[1]
    arr2[0] = op1
    for i in range(1, len(arr) - 1):
        op = arr2[i - 1] + arr[i + 1]
        arr2[i] = op
    for j in range(0, len(arr2)):
        total_sum = total_sum + arr2[j]
    return total_sum


def main():
    # Question 1
    print("Test of -Question 1-")
    ny = [1, 3, 20, 30]
    sf = [50, 20, 2, 4]
    M = 10
    print("NY:", ny)
    print("SF:", sf)
    print("M is:", M)
    print("Cost of optimal plan is", optimalPlan(ny, sf, M))
    # ------------------------------------------------------------------ #
    # Question 2
    print("\nTest of -Question 2-")
    s = [1, 5, 4, 9, 4, 2]
    print("Starting times of sessions:", s)
    f = [2, 11, 9, 10, 9, 6]
    print("Finishing times of sessions:", f)
    print("Optimal list of sessions:")
    print(optimal_list_of_sessions(s, f))
    # ------------------------------------------------------------------ #
    # Question 4
    print("\nTest of -Question 3-")
    arr = [-1, 6, 4, 2, 3, -7, -5]
    print("Array is", arr)
    print("Subset with the sum of 0", find_subset(arr, 0))
    # ------------------------------------------------------------------ #
    # Question 4
    print("\nTest of -Question 4-")
    s1 = ['A', 'L', 'I', 'G', 'N', 'M', 'E', 'N', 'T']
    s2 = ['S', 'L', 'I', 'M', 'E']
    print("String 1", s1)
    print("String 2", s2)
    print("Score is", sequence_cost(s1, s2))
    # ------------------------------------------------------------------ #
    # Question 5
    print("\nTest of -Question 5-")
    arr = [1, 5, 9, 7, 3, 4, 8]
    print("Array is:", arr)
    print("Minimum number of operations:", array_sum_operations(arr))


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
