# QUESTION 1
def leftmost_minimum(arr, rows):
    if len(arr) == 1:
        # append the leftmost minimum in rows array
        rows.append(min(arr[0]))

    else:
        if (len(arr) % 2) == 1:  # if array's length is odd
            leftmost_minimum(arr[0:(len(arr) // 2)], rows)
            # append the leftmost minimum in rows array
            rows.append(min(arr[len(arr) // 2]))
            leftmost_minimum(arr[(len(arr) // 2) + 1:], rows)
        else:  # if array's length is even
            leftmost_minimum(arr[0:((len(arr)) // 2)], rows)
            leftmost_minimum(arr[((len(arr)) // 2):], rows)


# QUESTION 2
def kth_largest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]
    midofarr1 = len(arr1) // 2
    midofarr2 = len(arr2) // 2
    if midofarr1 + midofarr2 < k:
        if arr1[midofarr1] > arr2[midofarr2]:
            return kth_largest(arr1, arr2[midofarr2 + 1:], k - midofarr2 - 1)
        else:
            return kth_largest(arr1[midofarr1 + 1:], arr2, k - midofarr1 - 1)
    else:
        if arr1[midofarr1] > arr2[midofarr2]:
            return kth_largest(arr1[:midofarr1], arr2, k)
        else:
            return kth_largest(arr1, arr2[:midofarr2], k)


# QUESTION 3
def max_sum_subarray(arr, start, end):
    if start == end - 1:
        return start, end, arr[start]
    else:
        mid = (start + end) // 2
        left_start, left_end, left_max = max_sum_subarray(arr, start, mid)
        right_start, right_end, right_max = max_sum_subarray(arr, mid, end)
        cross_start, cross_end, cross_max = max_crossing_subarray(arr, start, mid, end)
        # Return the maximum sum of three sums and return the arrays
        # start and end points
        if left_max > right_max and left_max > cross_max:
            return left_start, left_end, left_max
        elif right_max > left_max and right_max > cross_max:
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max


def max_crossing_subarray(arr, start, mid, end):
    # Sum of elements on left of middle element
    sum_left = -10000
    sum = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum = sum + arr[i]
        if sum > sum_left:
            sum_left = sum
            cross_start = i
    # Sum of elements on right of middle element
    sum_right = -10000
    sum = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum = sum + arr[i]
        if sum > sum_right:
            sum_right = sum
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right


def find_max_subarray(arr):
    # Returns the maximum subarray
    arr2 = []
    n = len(arr)
    left = 0
    right = n
    if right > n:
        right = n
    if left < 0:
        left = 0
    start, end, max_sum = max_sum_subarray(arr, left, right)
    for i in range(start, end):
        arr2.append(arr[i])
    return arr2, max_sum


# QUESTION 4
def is_bipartite(graph, root=0):
    # Returns true if a graph is bipartite
    # Defaults to start on root 0

    # colors array stores colors assigned to vertices.
    colors = [-1 for i in range(0, len(graph))]
    colors[root] = 1
    queue = [root]
    # Perform BFS and mark nodes of the graph the proper color
    while queue:
        u = queue.pop()
        if graph[u][u] == 1:
            return False
        for v in range(len(graph)):
            if graph[u][v] == 1 and colors[v] == -1:
                colors[v] = 1 - colors[u]
                queue.append(v)
            # An edge exists but already connects to same color
            elif graph[u][v] == 1 and colors[v] == colors[u]:
                return False
    # no edge connecting two vertices of the same color
    return True


# QUESTION 5

def find_gain(cost, price, gain):
    # base case, 1 elements left in price and cost arrays
    if len(price) == 1 and len(cost) == 1:
        # append the difference between price and cost into gain array
        gain.append(price[0] - cost[0])
        return

    if (len(cost) % 2) == 1:  # if array's length is odd
        find_gain(cost[0:(len(cost) // 2)], price[0:(len(price) // 2)], gain)
        # append the difference between price and cost into gain array
        gain.append(price[len(price) // 2] - cost[len(cost) // 2])
        find_gain(cost[(len(cost) // 2) + 1:], price[(len(price) // 2) + 1:], gain)
    else:  # if array's length is even
        find_gain(cost[0:((len(cost)) // 2)], price[0:((len(price)) // 2)], gain)
        find_gain(cost[((len(cost)) // 2):], price[((len(price)) // 2):], gain)

    return best_day_buy_goods(gain)


def best_day_buy_goods(gain): # returns the best day to buy goods
    day = gain[0]
    for i in range(0, len(gain)):
        if day < gain[i]:
            day = gain[i]

    return i + 1


def main():
    # Question 1
    print("Test of -Question 1-")
    arr = [[10, 17, 13, 28, 23], [17, 22, 16, 29, 23], [24, 28, 22, 34, 24], [11, 13, 6, 17, 7], [45, 44, 32, 37, 23],
           [36, 33, 19, 21, 6], [75, 66, 51, 53, 34]]
    print("Special array is:")
    for row in arr:
        for item in row:
            print("{:4.0f}".format(item), end=" ")
        print("")
    rows = []
    leftmost_minimum(arr, rows)
    print("Leftmost elements of each row in special array:")
    print(rows)
    # ------------------------------------------------------------------ #
    # Question2
    print("\nTest of -Question 2-")
    arr1 = [1, 3, 4, 5, 7, 9]
    print("Array 1 is :", arr1)
    arr2 = [0, 2, 6, 8, 11]
    print("Array 2 is:", arr2)
    k = 10
    print(k, "th element is", kth_largest(arr1, arr2, k))
    # ------------------------------------------------------------------ #
    print("\nTest of -Question 3-")
    a = [5, -6, 6, 7, -6, 7, -4]
    print("Array is:", a)
    a2 = []
    sum = 0
    a2, sum = find_max_subarray(a)
    print("The contiguous subset with the largest sum is", a2, "with sum", sum)
    # ------------------------------------------------------------------ #
    print("\nTest of -Question 4-")
    g = [[0, 1, 0],
         [1, 0, 1],
         [0, 1, 0]]
    print("Graph is:")
    for row in g:
        for item in row:
            print("{:4.0f}".format(item), end=" ")
        print("")
    print("Bipartite graph? ->", is_bipartite(g, 0))
    g1 = [[0, 1, 0],
          [1, 0, 1],
          [0, 1, 1]]
    print("Graph is:")
    for row in g1:
        for item in row:
            print("{:4.0f}".format(item), end=" ")
        print("")
    print("Bipartite graph? ->", is_bipartite(g1, 0))
    # ------------------------------------------------------------------ #
    print("\nTest of -Question 5-")
    cost = [5, 11, 2, 21, 5, 7, 8, 12, 13]
    price = [7, 9, 5, 21, 7, 13, 10, 14, 20]
    gain = []
    print("Costs:", cost)
    print("Prices", price)
    best_day = find_gain(cost, price, gain)
    print("Gain:", gain)
    print("The best day to buy goods is", best_day)



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
