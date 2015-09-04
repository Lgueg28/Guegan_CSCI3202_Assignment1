#Graph Implementation
class graph:
	def __init__(self):
		self.vertices = []
		self.edges = {}

	def addVertex(self, value):
		for i in self.vertices:
			if (value == i):
				print "Vertex Already Exits"
				return
		self.vertices.append(value)
		return

	def addEdge(self, value1, value2):
		aFound = False
		bFound = False
		for i in self.vertices:
			if (i == value1):
				aFound = True
		for j in self.vertices:
			if (j == value2):
				bFound = True
		if ( not(aFound and bFound )):
			print "One or more vertices not found"
			return
		else:
			if value1 in self.edges: 
				for k in self.edges[value1]:
					if ( k == value2 ):
						print "Edge already exists"
						return 
				self.edges[value1].append(value2)
				if value2 in self.edges:
					self.edges[value2].append(value1)
				else:
					self.edges[value2] = [value1]  
				return
			else:
				self.edges[value1] = [value2]
				self.edges[value2] = [value1]
				return

	def findVertex(self, value):
		for i in self.vertices:
			if (value == i):
				print "Found Node: "
				print i
				print "List of Adajcent vertices: "
				if i in self.edges:
					for k in self.edges[i]:
						print k
					return
				else:
					return
		print "node not found"
		return

#Graph tests
testGraph = graph()
testGraph.addVertex(1)
testGraph.addVertex(2)
testGraph.addVertex(3)
testGraph.addVertex(4)
testGraph.addVertex(5)
testGraph.addVertex(6)
testGraph.addVertex(7)
testGraph.addVertex(8)
testGraph.addVertex(9)
testGraph.addVertex(10)
testGraph.addEdge(1, 2)
testGraph.addEdge(1, 3)
testGraph.addEdge(1, 4)
testGraph.addEdge(1, 5)
testGraph.addEdge(1, 6)
testGraph.addEdge(1, 7)
testGraph.addEdge(1, 8)
testGraph.addEdge(1, 9)
testGraph.addEdge(1, 10)
testGraph.addEdge(2, 3)
testGraph.addEdge(2, 4)
testGraph.addEdge(2, 5)
testGraph.addEdge(2, 6)
testGraph.addEdge(2, 7)
testGraph.addEdge(2, 8)
testGraph.addEdge(2, 9)
testGraph.addEdge(2, 10)
testGraph.addEdge(3, 4)
testGraph.addEdge(3, 5)
testGraph.addEdge(3, 6)
testGraph.addEdge(3, 7)
testGraph.addEdge(3, 8)
testGraph.addEdge(3, 9)
testGraph.findVertex(1)	
testGraph.findVertex(2)
testGraph.findVertex(3)
testGraph.findVertex(4)
testGraph.findVertex(5)
