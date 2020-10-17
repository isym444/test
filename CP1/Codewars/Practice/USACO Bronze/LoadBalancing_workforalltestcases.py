import sys

""" sys.stdin = open("/Users/isym444/Desktop/PythonCP/CP1/Codewars/Practice/input.txt", "r")
sys.stdout = open("/Users/isym444/Desktop/PythonCP/CP1/Codewars/Practice/output.txt", "w")
 """
sys.stdin = open("balancing.in", "r")
sys.stdout = open("balancing.out", "w")

inters = [0 for _ in range(2)]
n, b = map(int, input().split())
points = [0 for _ in range(n)]
ans = 101
for i in range(n):
    points[i] = list(map(int, input().split()))


for i in range(0, n):
    for j in range(0, n):
        xdiv = points[i][0] + 1
        ydiv = points[j][1] + 1
        areas = [0 for _ in range(4)]
        for k in points:
            if k[0] < xdiv and k[1] > ydiv:
                areas[0] += 1
            if k[0] > xdiv and k[1] > ydiv:
                areas[1] += 1
            if k[0] < xdiv and k[1] < ydiv:
                areas[2] += 1
            if k[0] > xdiv and k[1] < ydiv:
                areas[3] += 1
        if max(areas) < ans:
            ans = max(areas)
print(ans)