class DirectedGraph():
    def __init__(self):
        self.adj, self.weight = self._getAdjList()

        self.vertex = list(self.adj.keys())
        self.arcs = []

        # auxiliar to the getAPath function
        self.path = []
        # auxiliar to the getACycle function
        self.cycle = []
        # self.arcs:
        # [vertex, neighbor, weight]
        # print("First for")

        for vertex, neighbors in self.adj.items():
            # print(vertex)
            for neighbor in neighbors:
                # Verification auxiliars
                arc = [vertex, neighbor[0], neighbor[1]]

                # Check if a arc already exist: Used in Undirected Graphs
                # if arc not in self.arcs and r_arc not in self.arcs:
                self.arcs.append(arc)

        """
        for i in range(0, adj.__len__()):
            neighbors = adj[i]
            
            self.arcs.append
            pass
            
        """
        self._check()

    def _check(self):
        # print("enterCheck")
        if self.arcs.__len__() != self.weight.__len__():
            print("graph input error!")
            return False

    def _dfsRecursive(self, start, c_time, vertex_color, vertex_pi, vertex_t):
        c_time = c_time + 1
        vertex_t[start][0] = c_time
        vertex_color[start] = 1
        for neighbor in self.getNeighbors(start)[0]:
            if vertex_color[neighbor] == 0:
                vertex_pi[neighbor] = start
                c_time = self._dfsRecursive(neighbor, c_time,
                                            vertex_color, vertex_pi, vertex_t)
        c_time = c_time + 1
        vertex_t[start][1] = c_time
        vertex_color[start] = 2

        return c_time

    def _getAdjList(self):
        # read file

        with open("USA-road-d.NY.gr", "r") as f:
            list = f.readlines()
            # print("readed")
        auxList = []
        for item in list:
            if not item.strip().startswith("c"):
                auxList.append(item.strip().split(" "))
            """ 
            *Convert the input:
            c 9th DIMACS Implementation Challenge: Shortest Paths
            c http://www.dis.uniroma1.it/~challenge9
            c TIGER/Line graph USA-road-d.NY
            c
            p sp 264346 733846
            c graph contains 264346 nodes and 733846 arcs
            c
            a 1 2 803
            ...

            *To:
            ['p', 'sp', '264346', '733846']
            ['a', '1', '2', '803']
            ...
            
            """
        # print("dict created")
        returnDict = {vertex: [] for vertex in range(1, int(auxList[0][2])+1)}
        fl = auxList.pop(0)
        heightList = []
        for item in auxList:
            returnDict[int(item[1])].append([int(item[2]), int(item[3])])
            """ 
            Structure:
            {
            vertex: [[neighbor, cost], [neighbor, cost], ...]
            }
            """
            heightList.append(int(item[3]))
        # print("dict returned")
        return returnDict, heightList

    def getTotalVertex(self):
        return self.vertex.__len__()

    def getTotalArcs(self):
        return self.arcs.__len__()

    def getNeighbors(self, vertex: int | str):
        """ Get the vertex neighbors by name """
        if (type(vertex) == int):
            return self.adj[vertex]
        else:
            return self.adj[vertex]

    def getDegree(self, vertex: int | str):
        """Get the vertex degree by name """
        if (type(vertex) == int):
            return self.adj[vertex].__len__()
        else:
            return self.adj[vertex].__len__()

    def getArcWeight(self, arc):
        """ Get the arc value """
        aux = self.adj[arc[0]]
        for item in aux:
            if item[0] == arc[1]:
                return item[1]
        # index = self.arcs.index(arc)
        # return self.weight[index]

    def getMinDegree(self):
        minD = self.adj[1].__len__()
        vertex = self.vertex[0]
        for i in range(1, self.adj.__len__()):
            if self.adj[i].__len__() < minD:
                minD = self.adj[i].__len__()
                vertex = self.vertex[i-1]

        return minD, vertex

    def getMaxDegree(self):
        maxD = self.adj[1].__len__()
        vertex = self.vertex[0]
        for i in range(1, self.adj.__len__()):
            if self.adj[i].__len__() > maxD:
                maxD = self.adj[i].__len__()
                vertex = self.vertex[i-1]

        return maxD, vertex

    def bfs(self, start):
        """Execute BFS in the Start vertex"""

        # 0 = Not Visited (Branco)
        # 1 = Visited (Cinza)
        # 2 = Finished (Preto)

        from sys import maxsize

        # Store the v.color, v.d, v.pi
        vertex_color = {vertex: 0 for vertex in self.vertex}
        vertex_d = {vertex: maxsize for vertex in self.vertex}
        vertex_pi = {vertex: None for vertex in self.vertex}

        # Initialize the Start vertex constant values
        vertex_color[start] = 1
        vertex_d[start] = 0
        vertex_pi[start] = None

        # Initialize the queue
        queue = []
        queue.append(start)

        # loop through the queue
        while queue:
            aux_vertex = queue.pop()
            for aux_neighbor in self.getNeighbors(aux_vertex)[0]:
                # BFS logic
                if vertex_color[aux_neighbor] == 0:
                    vertex_color[aux_neighbor] = 1
                    vertex_d[aux_neighbor] = vertex_d[aux_vertex] + 1
                    vertex_pi[aux_neighbor] = aux_vertex
                    queue.append(aux_neighbor)
                vertex_color[aux_vertex] = 2

        # return lists
        d = vertex_d
        pi = vertex_pi
        return d, pi

    def dfs(self, start):

        # Ignore the recursion limits
        from sys import setrecursionlimit
        setrecursionlimit(1000000)

        # Store the v.color, [v.ini, v.end], v.pi

        # 0 = Not Visited (Branco)
        # 1 = Visited (Cinza)
        # 2 = Finished (Preto)

        vertex_color = {vertex: 0 for vertex in self.vertex}
        vertex_pi = {vertex: None for vertex in self.vertex}
        vertex_t = {vertex: [0, 0] for vertex in self.vertex}

        # Time counter
        current_time = 0
        """
        for vertex in self.vertex:
            if vertex_color[vertex] == 0:
            
        """
        self._dfsRecursive(start, current_time,
                           vertex_color, vertex_pi, vertex_t)

        pi = vertex_pi
        ini = []
        fim = []
        for i in vertex_t:
            ini.append(vertex_t[i][0])
            fim.append(vertex_t[i][1])
        return pi, ini, fim

    def relax(self, arc, vertex_d, vertex_pi):
        if vertex_d[arc[1]] > vertex_d[arc[0]] + arc[2]:
            vertex_d[arc[1]] = vertex_d[arc[0]] + arc[2]
            vertex_pi[arc[1]] = arc[1]

        return vertex_d, vertex_pi

    def _initbf(self, start):
        from sys import maxsize
        vertex_d = {vertex: maxsize for vertex in self.vertex}
        vertex_pi = {vertex: None for vertex in self.vertex}

        vertex_d[start] = 0

        return vertex_d, vertex_pi

    def bf(self, start):
        vertex_d, vertex_pi = self._initbf(start)

        for _ in range(self.vertex.__len__() - 1):
            for arc in self.arcs:
                vertex_d, vertex_pi = self.relax(arc, vertex_d, vertex_pi)

        for arc in self.arcs:
            if vertex_d[arc[0]] > vertex_d[arc[1]] + arc[2]:
                return "Grafos com ciclos negativos!"

        dmin = vertex_d
        pi = vertex_pi
        return dmin, pi

    def djikstra(self, start):
        vertex_d, vertex_pi = self._initbf(start)
        from sys import maxsize
        maxDist = maxsize
        visited = set()
        print(set(vertex_d).__len__())

        while visited != set(vertex_d):
            print(visited.__len__())
            aux_vertex = None
            minDist = maxDist
            for vertex in self.vertex:
                if vertex not in visited and vertex_d[vertex] < minDist:
                    aux_vertex = vertex
                    minDist = vertex_d[vertex]

            visited.add(aux_vertex)

            for neighbor in self.getNeighbors(aux_vertex):
                vertex_d, vertex_pi = self.relax(
                    [aux_vertex, neighbor[0], neighbor[1]], vertex_d, vertex_pi)

        return vertex_d, vertex_pi

    def getACycle(self):
        from sys import setrecursionlimit
        setrecursionlimit(1000000)

        visited = {v: False for v in self.vertex}

        for vertex in self.vertex:
            if not visited[vertex]:
                if self.getACycleRecursive(vertex, visited, []):
                    return self.cycle

        return None

    def getACycleRecursive(self, current, visited, path):
        visited[current] = True
        path.append(current)

        if path.__len__() >= 5 and path[-5] in self.getNeighbors(current):
            self.cycle = path[-5:]
            return True

        for neighbor in self.getNeighbors(current):
            if not visited[neighbor[0]]:
                if self.getACycleRecursive(neighbor[0], visited, path):
                    return True
            elif visited[neighbor[0]] and path[-1] != neighbor[0]:
                index = path.index(neighbor[0])
                if path.__len__() - index >= 5:
                    self.cycle = path[index:]
                    return True

        path.pop()
        return False

    def getAPathRecursive(self, current: int, visited, path):
        visited[current] = True
        path.append(current)

        if path.__len__() >= 10:
            self.path = path[:]

        for neighbor in self.getNeighbors(current)[0]:
            if not visited[neighbor]:
                self.getAPathRecursive(neighbor, visited, path[:])

    def getAPath(self):
        from sys import setrecursionlimit
        setrecursionlimit(1000000)

        visited = {v: False for v in self.vertex}

        for vertex in self.vertex:
            if not visited[vertex]:
                path = self.getAPathRecursive(
                    current=vertex, visited=visited, path=[])

        return self.path


a = DirectedGraph()

print("vertex pos 1: ", a.vertex[0])
print("arc 1: ", a.arcs[0])
print("weight 1: ", a.weight[0])
print("Neighbors 1: ", a.getNeighbors(1))
print("Degree 1:", a.getDegree(1))
print("arc1,2: ", a.getArcWeight([1, 2]))
print("Min Degree: ", a.getMinDegree())
print("Max Degree: ", a.getMaxDegree())
print("arcs: ", a.arcs.__len__())

b, c = a.bfs(1)
print("BFS")
for i in range(1, 30):
    print(i, "dist: ", b[i])
    print(i, "pi: ", c[i])

b, c, d = a.dfs(1)
print("DFS")
for i in range(1, 15):
    print(i, "pi: ", b[i])
    print(i, "ini: ", c[i])
    print(i, "end: ", d[i])
"""
b, c = a.bf(1)
print("BF")
for i in range(1, 15):
    print(i, "dist: ", b[i])
    print(i, "pi: ", c[i])

print(48, "dist: ", b[48])
print(48, "pi: ", c[48])
print(a.getNeighbors(2))
"""
"""
b, c = a.djikstra(129)
print("Djikstra")
sortedbyValue = sorted(b.items(), key=lambda x: x[1], reverse=True)
print(sortedbyValue[0])
# print(a.getNeighbors(2))

"""
print(a.getAPath())
print(a.getACycle())

# print(a.getArcWeight([1, 48]))
