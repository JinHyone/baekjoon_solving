import io
import os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline # sys.stdin.readline


n = int(input())

for i in range(n):
	posd = list(map(int, input().split()))
	pos1, pos2 = (posd[0], posd[1]), (posd[3], posd[4])
	t_dist1, t_dist2 = posd[2], posd[5]  # 반지름

	if pos1[0] == pos2[0] and pos1[1] == pos2[1] and t_dist1 == t_dist2:
		print(-1)
		continue

	dist = ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5  # 터렛 사이의 거리
	if dist > max(t_dist1, t_dist2) + min(t_dist1, t_dist2):
		print(0)
		continue

	if dist == max(t_dist1, t_dist2) + min(t_dist1, t_dist2):
		print(1)
		continue

	if dist < max(t_dist1, t_dist2) + min(t_dist1, t_dist2):
		if max(t_dist1, t_dist2) == dist + min(t_dist1, t_dist2):
			print(1)
			continue

		if max(t_dist1, t_dist2) > dist + min(t_dist1, t_dist2):
			print(0)
			continue

		else:
			print(2)
			continue
