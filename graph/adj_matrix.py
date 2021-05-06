# Graph A: Non-directed graph

          #  0  1  2  3  4  5  6  7
graph_a = [[0, 0, 0, 1, 1, 0, 1, 0], # 0
           [0, 0, 1, 0, 1, 0, 0, 0], # 1
           [0, 1, 0, 0, 0, 1, 0, 0], # 2
           [1, 0, 0, 0, 0, 1, 1, 0], # 3
           [1, 1, 0, 0, 0, 0, 0, 1], # 4
           [0, 0, 1, 1, 0, 0, 0, 1], # 5 
           [1, 0, 0, 1, 0, 0, 0, 1], # 6
           [0, 0, 0, 0, 1, 1, 1, 0]  # 7
          ]




# Graph B: Directed graph

          #  0  1  2  3  4  5  6  7
graph_b =  [[0, 0, 0, 1, 1, 0, 1, 0],  #  0
            [0, 0, 0, 0, 1, 0, 0, 0],  #  1
            [0, 1, 0, 0, 0, 0, 0, 0],  #  2
            [0, 0, 0, 0, 0, 1, 1, 0],  #  3
	  [0, 0, 0, 0, 0, 0, 0, 1],  #  4 
            [0, 0, 1, 0, 0, 0, 0, 1],  #  5
            [0, 0, 0, 0, 0, 0, 0, 1],  #  6
            [0, 0, 0, 0, 0, 0, 0, 0]   #  7
          ]



def is_adjacent(graph, vert_a, vert_b):
	arr = []
	for i in range(len(graph[vert_a])):
		if 1 == graph[vert_a][i]:
			arr.append(i)

	while len(arr):
		for vert in range(len(arr) -1, -1, -1):
			if arr[vert] == vert_a:
				del arr[vert]
			elif arr[vert] == vert_b:
				return True

		for i in range(len(arr)):
			ind = arr[0]
			del arr[0]
			for j in range(len(graph[ind])):
				if 1 == graph[ind][j]:
					arr.append(j)

	return False



print("Graph A: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_a, i, j)))


print("Graph B: ")
for i in range(0, 8):
    for j in range(0, 8):
        print("Vertice {0} and vertice {1} are adjacent: {2}".format(i, j, is_adjacent(graph_b, i, j)))        
