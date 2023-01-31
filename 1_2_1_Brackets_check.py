# from InputDataGenerator import brackets_check
from sys import stdin


class BracketsChecker():


	def __init__(self, total=100):
		self.body = [(None, None) for i in range(total)]
		self.index = 0
		self.current = -1
		self.len = total
		self.status = True
		self.brackets = {'}': '{', ')': '(', ']': '['}


	def push(self, key):
		self.index += 1
		if key in self.brackets.values():
			self.current += 1
			self.body[self.current] = (key, self.index)
		else:
			if key in self.brackets:
				if self.brackets[key] == self.body[self.current][0]:
					self.pop_top()
					self.current -= 1
				else:
					self.status = False


	def pop_top(self):
		self.body[self.current] = None


def string_checker(string: str) -> str:
	length = len(string)
	checker = BracketsChecker(total=length)
	for i in range(length):
		checker.push(string[i])
		if checker.status is False:
			break
	if checker.status is True:
		if checker.current == -1:
			return 'Success'
		else:
			return checker.body[checker.current][1]
	else:
		return checker.index


def main():
	string = input()
	result = string_checker(string=string)
	print(string)


def test_checker():
	assert string_checker("([](){([])})") == "Success"
	assert string_checker("()[]}") == 5
	assert string_checker("{{{") == 3
	assert string_checker("{{[()]]") == 7
	assert string_checker("{{{[][][]") == 3
	assert string_checker("{*{{}") == 3
	assert string_checker("[[*") == 2
	assert string_checker("{*}") == "Success"
	assert string_checker("{{") == 2
	assert string_checker("{}") == "Success"
	assert string_checker("") == "Success"
	assert string_checker("}") == 1
	assert string_checker("*{}") == "Success"
	assert string_checker("{{{**[][][]") == 3


if __name__ == "__main__":
	# brackets_check()
	main()
