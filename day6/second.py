direction = {
    'up': [-1, 0],
    'down': [1, 0],
    'right': [0, 1],
    'left': [0, -1]
}


def getGrid():
    grid = []
    file = open('input1.txt', 'r')
    with file as f:
        for line in f:
            line = line.strip()
            grid.append([])
            for element in line:
                grid[-1].append(element)
    return grid


def printgrid(grid):
    for row in grid:
        print(row)


def getStart():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                return [i, j]

    return [-1, -1]


def dfs2(i, j, facing, grid):

    path = {}
    while True:
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return False
        if grid[i][j] == '#':
            if facing == 'up':
                i = i+1
                facing = 'right'
            elif facing == 'down':
                i = i-1
                facing = 'left'
            elif facing == 'right':
                j = j-1
                facing = 'down'
            elif facing == 'left':
                j = j+1
                facing = 'up'
        else:
            path[str((i, j))] = path.get(str((i, j)), 0)+1
            if path[str((i, j))] >= 6:
                return True
            grid[i][j] = 'X'
            ix, iy = direction[facing]
            i = i+ix
            j = j+iy


res2 = 0
grid = getGrid()
sx, sy = getStart()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#' or grid[i][j] == '^':
            continue
        grid[i][j] = '#'
        if dfs2(sx, sy, 'up', grid):
            res2 += 1
        grid[i][j] = '.'

print(res2)
