#binary tree implementation
class binaryTree:
        def __init__(self, intKey):
                self.key = intKey
                self.left = None
                self.right = None
                self.parent = None
	
	def add(self, value, parentValue):
		node = self.search(parentValue)
		if (node != None):
			if (node.left == None):
				node.left = binaryTree(value)
				node.left.parent = node.key
			elif (node.left != None and node.right == None):
				node.right = binaryTree(value)
				node.right.parent = node.key
			elif (node.left != None and node.right != None):
				print "Parent has two children, node not added"
		else:
			print "Parent not found"

	def search(self, value):
		if (self != None):
			if(self.key == value):
				return self
			else:
				if (self.left != None):
					if (self.left.search(value) != None):
						return self.left.search(value)
				if (self.right != None):
					if (self.right.search(value) != None):
						return self.right.search(value)
		else:
			return None		
		
	def delete(self,value):
		node = self.search(value)
		if (node != None):
			if ( node.left == None and node.right == None):
				tmpNode = self.search(node.parent)
				if(tmpNode.left == node):
					tmpNode.left = None
				if(tmpNode.right == node):
					tmpNode.right = None
				node = None
				return
			else:
				print "Node not deleted, has children"
				return
		else:
			print "Node not found"
			return


	def printTree(self, tree):
		if (tree != None):
			print (tree.key)
			if (tree.left != None): 
				tree.left.printTree(tree.left)
			if (tree.right != None):
				tree.right.printTree(tree.right)
			return

#tree tests
testBinTree = binaryTree(1)
testBinTree.add(2, 1)
testBinTree.add(3, 1)
testBinTree.add(4, 2)
testBinTree.add(5, 2)
testBinTree.add(6, 3)
testBinTree.add(7, 3)
testBinTree.add(8, 4)
testBinTree.add(9, 4)
testBinTree.add(10, 5)
print "Should Have ten nodes (1-10): "
testBinTree.printTree(testBinTree)
testBinTree.delete(10)
testBinTree.delete(9) 
print "Should have Eight Nodes (deleted 10 and 11)"
testBinTree.printTree(testBinTree)
