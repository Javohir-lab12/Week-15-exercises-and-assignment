grid = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for a in grid:
   a = map(lambda n: n+10 if n+10 <= 255 else 255, a)
print(grid)