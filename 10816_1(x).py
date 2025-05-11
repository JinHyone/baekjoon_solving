import sys
input = sys.stdin.readline


def binary_search(k):
	start = 0
	mid = n // 2
	end = n - 1

	while not (mid == start or mid == end):
		if k == cards[mid]:
			return True

		elif k > cards[mid]:
			start = mid
			mid = (start + end) // 2

		elif k < cards[mid]:
			end = mid
			mid = (start + end) // 2

	return mid


n = int(input())
cards = list(map(int, input().split()))

m = int(input())
answers = list(map(int, input().split()))

cards = sorted(cards)
ansd = dict()

for ans in answers:
	ad = ansd.get(ans)
	ansd[ans] = 0 if ad is None else ad

for ans in answers:
	ad = ansd.get(ans)
	ansd[ans] = 0 if ad is None else ad

	bs = binary_search(ans - 0.1)
	bs = 0 if bs == 0 else bs + 1

	while bs < n and ans == cards[bs]:
		ansd[ans] += 1
		bs += 1


print(' '.join(list(map(str, ansd.values()))))
