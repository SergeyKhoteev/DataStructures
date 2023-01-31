from sys import stdin


class TreeStack():

	def __init__(self, length: int):
		self.tree = [None for i in range(length)]
		self.height = 0
		self.length = length


	def push_item(self, key):
		self.tree[self.height] = key
		self.height += 1


	def pop_item(self):
		self.tree[self.height - 1] = None
		self.height -= 1


	def reverse_tree(self):
		temp_tree = self.tree[:self.height]
		temp_tree.reverse()
		for i in range(self.height):
			self.tree[i] = temp_tree[i]


def get_tree_height_stack(array_tree: list, length: int) -> int:
	item_level = [None for i in range(length)]
	tree_stack = TreeStack(length=length)
	now = 0
	i = 0
	max_height = 0
	while now < length:
		if item_level[now] is not None:
			now += 1
			i = now
			continue
		tree_stack.push_item(i)
		if array_tree[i] == -1:
			tree_stack.reverse_tree()
			for j in range(tree_stack.height - 1, -1, -1):
				item_level[tree_stack.tree[j]] = tree_stack.height
				max_height = max(max_height, tree_stack.height)
				tree_stack.pop_item()
			now += 1
			i = now
			continue
		if item_level[array_tree[i]] is None:
			i = array_tree[i]
		else:
			tree_stack.reverse_tree()
			for j in range(tree_stack.height - 1, -1, -1):
				item_level[tree_stack.tree[j]] = tree_stack.height + item_level[array_tree[i]]
				max_height = max(max_height, item_level[tree_stack.tree[j]])
				tree_stack.pop_item()
	return max_height

def main():
	tree_len = int(input())
	tree = list(map(int, input().split()))
	result = get_tree_height_stack(array_tree=tree, length=tree_len)
	print(result)


def test_get_tree_height():
	assert get_tree_height_stack(array_tree=[9, 7, 5, 5, 2, 9, 9, 9, 2, -1], length=10) == 4
	assert get_tree_height_stack(array_tree=[-1], length=1) == 1
	assert get_tree_height_stack(array_tree=[], length=0) == 0
	assert get_tree_height_stack(array_tree=[-1, 0, 1, 2, 3, 4, 5], length=7) == 7
	assert get_tree_height_stack(array_tree=[-1 if i == (int(1e5) - 1) else i + 1 for i in range(int(1e5))], length=int(1e5)) == int(1e5)


if __name__ == '__main__':
	main()
	