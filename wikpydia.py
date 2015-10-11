import wikipedia,sys

def search_links(page,target):
	counter = 1
	minimum = sys.maxint
	levels = [page]
	while True:
		print counter
		children = []
		counter += 1
		for level in levels:
			for sub_level in wikipedia.page(level).links:
				sub_level.lower()
				if sub_level == target:
					return counter
				elif sub_level not in children:
					print sub_level
					children.append(sub_level)
		levels = children

search_links(sys.argv[1].lower(), sys.argv[2].lower())