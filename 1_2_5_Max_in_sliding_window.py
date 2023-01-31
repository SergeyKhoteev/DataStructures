from sys import stdin


class MaxStack():

	def __init__(self, total, sequence=False):
		self.body = [None for i in range(total)]
		self.index = 0
		self.max = [None for i in range(total)]
		if sequence:
			for i in range(total - 1, -1, -1):
				self.push(sequence[i])

	def __str__(self):
		return f'{self.body}'

	def push(self, key):
		self.body[self.index] = key
		if self.index == 0:
			self.max[self.index] = key
		else:
			self.max[self.index] = max(key, self.max[self.index - 1])
		self.index += 1

	def pop(self):
		if self.index > 0:
			self.index -= 1
			value = self.body[self.index]
			self.body[self.index] = None
			self.max[self.index] = None
			return value

	def return_max(self):
		if self.index > 0:
			return self.max[self.index - 1]

	def return_len(self):
		return self.index


def get_maximums_in_array(total: int, sequence: list, window:int):
	stack_1 = MaxStack(total=window)
	stack_2 = MaxStack(total=window)
	result = []
	for i in range(total):
		stack_1.push(sequence[i])
		if stack_1.return_len() == window:
			stack_2 = MaxStack(total=window, sequence=stack_1.body)
			stack_1 = MaxStack(total=window)
		if stack_2.return_max() is not None:
			if stack_1.return_max() is not None:
				result.append(max(stack_1.return_max(), stack_2.return_max()))
				stack_2.pop()
			else:
				result.append(stack_2.return_max())
				stack_2.pop()
	return result


def main():
	reader = (line for line in stdin)
	global n, array, window
	n = int(next(reader))
	array = list(map(int, next(reader).split()))
	window = int(next(reader))
	result = get_maximums_in_array(total=n, sequence=array, window=window)
	print(*result)


def naive_main(n=None, array=None, window=None):
	naive_result = []
	reader = (line for line in stdin)
	if not n:
		n = int(next(reader))
		array = list(map(int, next(reader).split()))
		window = int(next(reader))
	for i in range(window - 1, n):
		naive_result.append(max(array[i - (window - 1): i + 1]))
	return naive_result


if __name__ == '__main__':
	main()
