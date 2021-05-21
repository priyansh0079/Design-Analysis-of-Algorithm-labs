#-------------------------------------------------Graph-----------------------------------------------------------------#
print()
graph = {
  1 : [2,3],
  2 : [1,4],
  3 : [1,4,5],
  4 : [2,3],
  5 : [3,6],
  6 : [],
}

#--------------------------------------------BFS implementation----------------------------------------------------------#

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)

  queue.append(node)
  print("The BFS traversal of the graph is, ", end=" ")
  while queue:
      s = queue.pop(0)
      print(s, end=" ")

      try:
          for neighbour in graph[s]:
              if neighbour not in visited:
                  visited.append(neighbour)
                  queue.append(neighbour)
      except:
          print()

bfs(visited, graph, 1)
print()
print()

#---------------------------------------------DFS implementation---------------------------------------------------#

visited = []
Stack = []

def bfs(visited, graph, node):

  visited.append(node)
  Stack.append(node)
  print("The DFS traversal of the graph is, ", end=" ")
  while Stack:
    s = Stack.pop(-1)
    print (s, end = " ")

    try:
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                Stack.append(neighbour)
    except:
        print()

bfs(visited, graph, 1)


print()
print()

#-----------------------------Code for checking strongly connected graph------------------------------------------#

dict_keys = [key for key in graph]


def SC(graph, starting_node):
    global dict_keys
    visited_nodes = []
    stack = [starting_node]

    while len(stack) != 0:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            for neighbours in graph[current_node]:
                stack.append(neighbours)

    if sorted(visited_nodes) != sorted(dict_keys):
        print("This Graph is not strongly connected")

    else:
        print("This graph is strongly connected")

    return visited_nodes


SC(graph, dict_keys[0])

#-----------------------------------pre order and post order times------------------------------------------#


trav_time = {}
for i in dict_keys:
    trav_time.update({i: [0, 0]})


def pre_and_post_order(graph):
    global trav_time

    time = 0
    dict_keys_2 = [key for key in graph]

    for node in graph:
        time += 1
        if len(graph[node]) != 0:
            trav_time[node][0] = time
        else:

            trav_time[node][0] = time
            time += 1
            trav_time[node][1] = time
            counter = dict_keys_2.index(node)
            while counter >= 0:

                trav_time[dict_keys_2[counter]][1] = time
                time += 1
                counter -= 1

            return (trav_time)

print()
dict_new=pre_and_post_order(graph)
for i in range(len(dict_new)):
    print("pre and post visited times for node ",i+1," = ",dict_new[i+1])