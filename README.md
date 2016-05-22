# WikiPYdia
WikiPYdia implements basic path finding algorithms to determine the shortest path between two wikipedia pages. Currently, WikiPYdia uses Djikstra's shortest path algorithm, a modified breadth-first search, to comb through all the links on a page and find the shortest method of getting to the second page. As correlations between the two pages are found, the algorithm can be convered to A*, using a heuristic to guide the algorithm towards the desired page rather than search every single link as it currently does.

Current limitations: the wikipedia parser that we're using has a limit on the number of requests we are allowed, which is a problem when you're searching through thousands of links at a time.

Usage:
python wikpydia.py *page1* *page2*
