Fin = open("26.txt")
N, K = map(int, Fin.readline().split())
data = list(map(int, Fin.readlines()))
del data[0]

data.sort()

print(round(sum(data[-K-1: -(2*K)-1: -1]) / K - 0.5), round(sum(data[-1:-K-1:-1])/K - 0.5))

Fin.close()
