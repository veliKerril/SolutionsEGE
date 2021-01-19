Fin = open("27a.txt")
Del = 5

N = int(Fin.readline())

sum = 0
dMin = [10001] * 5
for i in range(N):
  a, b = map(int, Fin.readline().split())
  sum += min(a, b)
  d = abs(a - b)
  r = d % Del

  if r > 0:
    dMinNew = dMin[:]
    for j in range(1, Del):
      r0 = (r + j) % Del
      dMinNew[r0] = min(d + dMin[j], dMin[r0])
    dMinNew[r] = min(d, dMin[r])
    dMin = dMinNew[:]

if sum % Del == 0:
  print(sum)
else:
  print(sum + dMin[Del - sum % Del])


Fin = open("27b.txt")
N = int(Fin.readline())

sum = 0
for i in range(N):
  a, b = map(int, Fin.readline().split())
  sum += min(a, b)
  d = abs(a - b)
  r = d % Del

  if r > 0:
    dMinNew = dMin[:]
    for j in range(1, Del):
      r0 = (r + j) % Del
      dMinNew[r0] = min(d + dMin[j], dMin[r0])
    dMinNew[r] = min(d, dMin[r])
    dMin = dMinNew[:]

if sum % Del == 0:
  print(sum)
else:
  print(sum + dMin[Del - sum % Del])

Fin.close()
