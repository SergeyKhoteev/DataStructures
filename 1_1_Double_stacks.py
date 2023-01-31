from random import randint


class Stack():


	def __init__(self):
		self.body = []
		self.min = []
		self.len = 0
	

	def push_key(self, key):
		self.body.append(key)
		if self.len > 0:
			current_min = self.min[-1]
			if key < current_min :
				self.min.append(key)
			else:
				self.min.append(current_min)
		else:
			self.min.append(key)
		self.len += 1


	def pop_top(self):
		if self.len > 0:
			value = self.body.pop(-1)
			minimum = self.min.pop(-1)
			self.len -= 1
			return value, minimum
		return None


	def get_len(self):
		return self.len


	def top_key(self):
		if self.len > 0:
			return (self.body[-1], self.min[-1])
		return None


	def get_min(self):
		if self.len > 0:
			return self.min[-1]
		else: 
			return 99999999999999999999999999


def main():
	array_len = 10
	window = 3
	array = [randint(0, 30) for i in range(array_len)]
	result = get_min_in_array_for_window(array=array, window=window, array_len=array_len)
	print(array)
	print(result)


def get_min_in_array_for_window(array: list, window: int, array_len: int) -> list:
	push_stack = Stack()
	pop_stack = Stack()
	result = []
	for i in range(array_len):
		push_stack.push_key(array[i])
		if i < window - 1:
			continue
		current_len = push_stack.get_len()
		if current_len < window:
			push_val, push_min = push_stack.top_key()
			pop_val, pop_min = pop_stack.top_key()
			if push_min < pop_min:
				result.append(push_min)
			else:
				result.append(pop_min)
			pop_stack.pop_top()
		if current_len == window:
			while push_stack.top_key() is not None:
				value, minimum = push_stack.pop_top()
				pop_stack.push_key(value)
			value, minimum = pop_stack.pop_top()
			result.append(minimum)
	return result


if __name__ == '__main__':
	main()
