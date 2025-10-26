def grid_paths(n,m):
    if n == 1 or m == 1:
        return 1
    return grid_paths(n-1,m) + grid_paths(n,m-1)
#print(grid_paths(3,3)) #this outputs 6