from sys import stdin
import pytest


class queue():

	def __init__(self, size, length):
		self.queue = [None for i in range(length)]
		self.start = 0
		self.finish = 0
		self.packages_in_queue = 0
		self.size = size
		self.starting_time = False

	def enqueue(self, key: tuple) -> int:
		if self.packages_in_queue < self.size:
			self.queue[self.finish] = key
			if self.starting_time is False or self.starting_time < key[0]:
				self.starting_time = key[0]
			self.queue[self.finish] += (self.starting_time, self.starting_time + key[1])
			self.starting_time += key[1]
			self.packages_in_queue += 1
			self.finish += 1
			return self.queue[self.finish - 1][2]
		return False

	def dequeue(self, index):
		if self.start < self.finish:
			while self.queue[self.start][3] <= index:
				self.start += 1
				self.packages_in_queue -= 1
				if self.start == self.finish:
					break


def get_package_info(size:int, n: int, sequence: list) -> list:
	if n == 0:
		return None
	q = queue(length=n, size=size)
	result = [-1 for i in range(n)]
	for i in range(n):
		q.dequeue(index=sequence[i][0])
		response = q.enqueue(key=sequence[i])
		if response is not False:
			result[i] = response
	return result


def main():
	reader = (tuple(map(int, line.split())) for line in stdin)
	size, n = tuple(next(reader))
	packages = list(reader)
	result = get_package_info(size=size, n=n, sequence=packages)
	if result is not None:
		print('\n'.join(list(map(str, result))))


@pytest.mark.parametrize(
	"size, n, sequence, expected", [
	(5, 7, [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)], [0, 1, 2, 3, 4, -1, -1]),
	(1, 0, [], None),
	(5, 10, [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
	(1, int(1e5), [(i, 1) for i in range(int(1e5))], [i for i in range(int(1e5))]),
	(4, 10, [(0, 2), (0, 2), (1, 2), (1, 2), (2, 2), (2, 2), (3, 2), (3, 2), (4, 2), (4, 2)], [0, 2, 4, 6, 8, -1, -1, -1, 10, -1]),
	(1, 2, [(0,1), (0, 1)], [0, -1]),
	(1, 2, [(0,1), (1, 1)], [0, 1]),
	(1, 5, [(0, 5), (0, 5), (0, 5), (0, 5), (0, 5), ], [0, -1, -1, -1, -1]),
	(1, 5, [(0, 5), (0, 5), (0, 5), (0, 5), (10, 1), ], [0, -1, -1, -1, 10]),
	(2, 8, [(0, 0), (0, 0), (0, 0), (1, 0), (1, 0), (1, 1), (1, 2), (1, 3)], [0, 0, 0, 1, 1, 1, 2, -1]),
	(2, 8, [(0, 0), (0, 0), (0, 0), (1, 1), (1, 0), (1, 0), (1, 2), (1, 3)], [0, 0, 0, 1, 2, -1, -1, -1]),
	(1, 5, [(9, 1), (10, 0), (10, 1), (10, 0), (10, 0)], [9, 10, 10, -1, -1,]),])
def test_queue(size, n, sequence, expected):
	assert get_package_info(size=size, n=n, sequence=sequence) == expected
	


if __name__ == '__main__':
	main()
