# A trie implementation in Python

class Node(object):
	"""
	Trie node implementation
	"""
	def __init__(self, char):
		self.char = char
		self.children = []
		self.complete = False
		self.counter = 1

def add(root, word):
	"""
	Adding a word into the tree
	"""
	node = root
	for char in word:
		found_in_child = False

		for child in children:
			if child.char == char:
				child.counter += 1
				node = child
				found_in_child = True
				break

		if not found_in_child:
			new_node = Node(char)
			node.children.append(new_node)
			node = new_node

	node.complete = True

def find_prefix(root, prefix):
	"""
	Check and return 
	1. If the prefix exsists in any of the words we added so far
	2. If yes then how may words actually have the prefix
	"""
	node = root
	# If the root node has no children, then return False.
	# Because it means we are trying to search in an empty trie
	if not root.children:
		return False, 0
	
	for char in prefix:
		char_not_found = True
		# Search through all the children of the present `node`
		for child in node.children:
			if child.char == char:
			# We found the char existing in the child.
				char_not_found = False
				# Assign node as the child containing the char and break
				node = child
				break
		# Return False anyway when we did not find a char.
		if char_not_found:
			return False, 0
	# Well, we are here means we have found the prefix. Return true to indicate that
	# And also the counter of the last node. This indicates how many words have this
	# prefix
	return True, node.counter