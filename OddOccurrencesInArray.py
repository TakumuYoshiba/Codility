def solution(A):
  ans = 0
  for i in A:
    ans ^= n
  return ans

A = [9,3,9,3,9,7,9]
solution(A)