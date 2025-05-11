import sys
input = sys.stdin.readline


def binary_search(k):
	start = 0
	mid = n // 2
	end = n - 1

	while not (mid < start or mid > end):
		if k == cards[mid]:
			return ansd[k]

		elif k > cards[mid]:
			start = mid + 1
			mid = (start + end) // 2

		elif k < cards[mid]:
			end = mid - 1
			mid = (start + end) // 2

	return 0


n = int(input())
cards = list(map(int, input().split()))

m = int(input())
answers = list(map(int, input().split()))

cards = sorted(cards)
ansd = dict()

for card in cards:
	cd = ansd.get(card)
	ansd[card] = 1 if cd is None else cd + 1

for ans in answers:
	print(binary_search(ans), end=' ')

