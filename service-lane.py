def min_width(list_item, a, b):
    return min(k for k in list_item[a:b+1])

N, T = raw_input().strip().split()
N, T = int(N), int(T)
width = [int(i) for i in raw_input().strip().split()]

for i in range(T):
    i, j = raw_input().strip().split()
    i, j = int(i), int(j)
    print min_width(width, i, j)
