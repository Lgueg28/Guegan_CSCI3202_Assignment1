#Queue Implementation
import Queue

class pyQueue():
	def __init__(self):
		self.queue = Queue.Queue()

	def add(self, integer):
		return self.queue.put(integer)

	def empty(self):
		return self.queue.empty()

	def retrieve(self):
		return self.queue.get()

#Queue test
print "Running Queue Test"
testQueue = pyQueue()
for (i) in range (10):
	testQueue.add(i)

while not testQueue.empty():
	print testQueue.retrieve()

