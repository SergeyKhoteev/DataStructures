from sys import stdin


class MaxStack():

	def __init__(self, total):
		self.body = [None for i in range(total)]
		self.index = 0
		self.max = [None for i in range(total)]

	def push(self, key):
		self.body[self.index] = key
		if self.index == 0:
			self.max[self.index] = key
		else:
			self.max[self.index] = max(key, self.max[self.index - 1])
		self.index += 1

	def pop(self):
		if self.index > 0:
			self.body[self.index] = None
			self.max[self.index] = None
			self.index -= 1

	def return_max(self):
		if self.index > 0:
			print(self.max[self.index - 1])


def main():
	n = int(input())
	stack = MaxStack(total=n)
	for i in range(n):
		command = tuple(input().split())
		if len(command) == 1:
			if command[0] == 'max':
				stack.return_max()
			elif command[0] == 'pop':
				stack.pop()
		else:
			stack.push(int(command[1]))


if __name__ == "__main__":
	main()
