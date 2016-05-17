import wikipedia
import heapq
import sys
import itertools

def search_links(page, target):
	pq = []                         # list of entries arranged in a heap
	entry_finder = {}               # mapping of tasks to entries
	REMOVED = '<removed-task>'      # placeholder for a removed task
	counter = itertools.count()     # unique sequence count

	def add_task(task, priority=0):
	    'Add a new task or update the priority of an existing task'
	    if task in entry_finder:
	        remove_task(task)
	    count = next(counter)
	    entry = [priority, count, task]
	    entry_finder[task] = entry
	    heapq.heappush(pq, entry)

	def remove_task(task):
	    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
	    entry = entry_finder.pop(task)
	    entry[-1] = REMOVED

	def pop_task():
	    'Remove and return the lowest priority task. Raise KeyError if empty.'
	    while pq:
	        priority, count, task = heapq.heappop(pq)
	        if task is not REMOVED:
	            del entry_finder[task]
	            return task
	    raise KeyError('pop from an empty priority queue')

	edgeTo = {}
	distance = {}
	edgeTo[page] = None
	distance[page] = 0

	add_task(page, 0)

	while page != target:
		page = pop_task()
		print(page)
		new_dist = distance[page] + 1
		for neighbor in page_neighbor(page):
			if not (neighbor in distance) or (new_dist < distance[neighbor]):
				add_task(neighbor, new_dist)
				edgeTo[neighbor] = page
				distance[neighbor] = new_dist

	while page != None:
		print(page)
		page = edgeTo[page]

def page_neighbor(page): 
	neighbors = []
	for sub_level in wikipedia.page(page).links:
		sub_level.lower()
		neighbors.append(sub_level)
	return neighbors

search_links(sys.argv[1].lower(), sys.argv[2].lower())
