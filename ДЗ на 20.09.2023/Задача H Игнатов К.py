# -*- coding: utf-8 -*-
"""Untitled51.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1801W2NvE8S4rkZgoN9qOBcdfjfu894Vd
"""

N, M, K = map(int, input().split())

start = [i for i in range(1, N + 1)]
racers = set()

ans = []
for _ in range(M):
  i, j = map(int, input().split())
  start[i - 1], start[j - 1] = start[j - 1], start[i - 1]

  if(abs(start[i - 1] - i) > K):
    racers.add(i)
  elif i in racers:
    racers.remove(i)


  if(abs(start[j - 1] - j) > K):
    racers.add(j)
  elif j in racers:
    racers.remove(j)


  if len(racers) != 0:
    ans.append(1)
  else:
    ans.append(0)


print(*ans, sep='\n')