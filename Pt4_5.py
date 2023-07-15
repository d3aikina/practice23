graph = {
 'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'D': [],
 'E': ['F'],
 'F': []
}
start = 'A'
end = 'F'

paths = [start]
finished_paths = []

while paths:
  for path in paths:
    paths.remove(path)
    for i in graph[path[-1]]:
      if i == end:
        finished_paths += [path + i]
      else:
        paths += [path + i]
print(finished_paths)