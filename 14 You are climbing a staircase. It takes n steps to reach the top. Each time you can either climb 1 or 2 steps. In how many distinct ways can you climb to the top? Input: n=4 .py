def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    first = 1  # ways to reach step 1
    second = 2  # ways to reach step 2
    
    for i in range(3, n + 1):
        current = first + second
        first = second
        second = current
    
    return second

# Input
n = int(input("Enter number of steps: "))
print(f"Number of distinct ways to climb {n} steps: {climb_stairs(n)}")
