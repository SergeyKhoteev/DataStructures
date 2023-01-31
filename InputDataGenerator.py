from random import choice, randint


def generator(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		with open('test_data.txt', 'w') as file:
			file.write(result)
	return wrapper


@generator
def brackets_check():
	array = [')', '(', '[', ']', '{', '}', '"', '"', "'", "'"]
	array = [')', '(', '[', ']', '{', '}']
	to_write = ''
	for i in range(randint(10, 20)):
		to_write += choice(array)
	return to_write

@generator
def sliding_window():
	to_write = ''
	for i in range(5):
		length = int(1e3)
		seq = ' '.join(str(randint(0, 1e5)) for i in range(length))
		window = str(randint(1, 20))
		to_write += '\n'.join([str(length), seq, window]) + '\n'
	return to_write


