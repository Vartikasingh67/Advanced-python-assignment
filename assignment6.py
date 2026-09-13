# Memoization method

# Inputs
weights = (2, 1, 3, 2)
values = (12, 10, 20, 15)
capacity = 5

n = len(weights)

# Create memoization table
memo = [[-1] * (capacity + 1) for _ in range(n + 1)]


def knapsack(weights, values, n, capacity, memo):

    # Base case
    if n == 0 or capacity == 0:
        return 0

    # Return already calculated value
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # Check if current item can fit
    if weights[n - 1] <= capacity:

        # Include the item
        include = values[n - 1] + knapsack(weights,values,n - 1,capacity - weights[n - 1],memo)

        # Exclude the item
        exclude = knapsack(weights,values,n - 1,capacity,memo)

        # Choose maximum
        memo[n][capacity] = max(include, exclude)

    else:
        # Item cannot fit
        memo[n][capacity] = knapsack(weights,values,n - 1,capacity,memo)

    return memo[n][capacity]


# Find maximum value
result = knapsack(weights,values,n,capacity,memo)

print("Maximum value:", result)
