def solution(A, K):
  from collections import deque
  if len(A) == 0:
    return []
  else:
    d = deque(A)

    lst = list(range(K))  
    for i in lst:
      num = d.pop()
      d.appendleft(num)
    return list(d)

A = [3, 8, 9, 7, 6]
K = 3
solution(A,K)




'''
[3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
[6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
[7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
'''