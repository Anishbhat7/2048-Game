import random

def start_game():
  grid = [[0 for i in range(4)]for j in range(4)]
  return grid

def add_new_2(grid):
  r = random.randint(0,3)
  c = random.randint(0,3)
  while grid[r][c] != 0:
    r = random.randint(0,3)
    c = random.randint(0,3)
  grid[r][c] = 2

  return grid

def compress(grid):
  changed = False
  new_grid = []

  for i in range(4):
    new_grid.append([0]*4)

  for i in range(4):
    pos = 0
    for j in range(4):
      if grid[i][j] != 0:
        new_grid[i][pos] = grid[i][j]
        if j!=pos:
          changed = True
        pos+=1
  return new_grid, changed

def merge(grid):
  changed = False
  for i in range(4):
    for j in range(3):
      if grid[i][j] == grid[i][j+1] and grid[i][j]!=0:
        grid[i][j] = 2* grid[i][j]
        grid[i][j+1] = 0
        changed = True
  return grid, changed

def reverse(grid):
  new_grid = []
  for i in range(4):
    new_grid.append([])
    for j in range(4):
      new_grid[i].append(grid[i][4-j-1])

  return new_grid

def transpose(grid):
  new_grid = []
  for i in range(4):
    new_grid.append([])
    for j in range(4):
      #print(i, j)
      new_grid[i].append(grid[j][i])
    #print(new_grid)
  return new_grid

def move_left(grid):
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, changed3 = compress(new_grid)
  return new_grid, changed

def move_right(grid):
  new_grid = reverse(grid)
  new_grid, changed1 = compress(new_grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, changed3 = compress(new_grid)
  new_grid = reverse(new_grid)

  return new_grid, changed

def move_up(grid):
  transposed_grid = transpose(grid)
  new_grid, changed1 = compress(transposed_grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, changed3 = compress(new_grid)
  final_grid = transpose(new_grid)

  return final_grid, changed

def move_down(grid):
  transposed_grid = transpose(grid)
  new_grid = reverse(transposed_grid)
  new_grid, changed1 = compress(new_grid)
  new_grid, changed2 = merge(new_grid)
  changed = changed1 or changed2
  new_grid, changed3 = compress(new_grid)
  final_reverse_grid = reverse(new_grid)
  final_transpose_grid = transpose(final_reverse_grid)

  return final_transpose_grid, changed

def get_current_state(grid):
  for i in range(4):
    for j in range(4):
      if grid[i][j] == 2048:
        return 'WON'

  for i in range(4):
    for j in range(4):
      if grid[i][j] == 0:
        return 'GAME NOT OVER'

  for i in range(3):
    for j in range(3):
      if grid[i][j] == grid[i+1][j] or grid[i][j] == grid[i][j+1]:
        return 'GAME NOT OVER'

  for j in range(3):
    if grid[3][j] == grid[3][j+1]:
      return 'GAME NOT OVER'

  for i in range(3):
    if grid[i][3] == grid[i+1][3]:
      return 'GAME NOT OVER'

  return 'LOST'

