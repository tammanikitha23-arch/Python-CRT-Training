# Read input
N = 5

# Upper hollow triangle
for i in range(N):
    # Left spaces
    print(" " * (N - i - 1), end="")

    # Hollow part
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower hollow triangle
for i in range(N - 2, -1, -1):
    # Left spaces
    print(" " * (N - i - 1), end="")

    # Hollow part
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Read input
N = 5

# Print hollow inverted right triangle
for i in range(N):
    for j in range(N - i):
        # Print star for:
        # first row OR first column OR last column
        if i == 0 or j == 0 or j == (N - i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()