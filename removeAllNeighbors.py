import sys
from iota import Iota

if not sys.argv[1:]:
	print("Error: No nodes given as parameters")
	print("Use: removeAllNeighbors [Node Direction]")
	sys.exit(1)

for node in sys.argv[1:]:
	api = Iota('http://'+node+':14265')
	print(node)
	neighbors = api.getNeighbors()
	uris = []

	for v in neighbors.get("neighbors"):
		addr = v.get("address")
		protocol = v.get("connectionType")
		uris.append(protocol+"://"+addr)
		api.remove_neighbors(uris)
