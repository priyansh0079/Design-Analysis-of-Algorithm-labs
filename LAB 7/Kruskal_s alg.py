print("Kruskal Algorithm")
print()
def find(i):
	while parent[i] != i:
		i = parent[i]
	return i

def union(i, j):
	a = find(i)
	b = find(j)
	parent[a] = b

def kruskalMST(cost):
	mincost = 0

	for i in range(V):
		parent[i] = i

	edge_count = 0
	while edge_count < V - 1:
		min = INF
		a = -1
		b = -1
		for i in range(V):
			for j in range(V):
				if find(i) != find(j) and cost[i][j] < min:
					min = cost[i][j]
					a = i
					b = j
		union(a, b)
		print('({}, {}, {})'.format(dict[a], dict[b], min))
		edge_count += 1
		mincost += min
	print()
	print("Minimum cost= {}".format(mincost))



V = 9
parent = [i for i in range(V)]
INF = float('inf')
cost = [[INF, 4, INF,INF,INF,INF,INF, 8, INF],
		[4, INF,8,INF,INF,INF,INF, 11, INF],
		[INF, 8, INF,7, INF,4,INF,INF, 2],
		[INF,INF,7,INF,6, 14, INF, INF, INF],
		[INF,INF,INF,6 ,INF,10 ,INF,INF, INF],
        [INF,INF,4, 14, 10, INF,2, INF,INF,],
        [INF,INF,INF,INF,INF,2, INF,1, 6],
        [8, 11, INF,INF,INF,INF,1, INF,7],
        [INF,INF,2, INF,INF,6, INF,7, INF]]

dict={0:'a',
      1:'b',
      2:'c',
      3:'d',
      4:'e',
      5:'f',
      6:'g',
      7:'h',
      8:'i'}


kruskalMST(cost)

