#!/usr/bin/env python

""" sum of dividers"""
__author__      = "Andrey"

sum_of_both = int(1)
start_a = int(1)
while start_a < 1000000:
  sum_of_dividers_a = 0
  for i in range(start_a - 1, 1, -1):
      if (start_a % i == 0):
          sum_of_dividers_a += i
  start_b = int(sum_of_dividers_a)
  sum_of_dividers_b = 0
  for k in range(start_b - 1, 1, -1):
      if (start_b % k == 0):
          sum_of_dividers_b += k
  if start_a == sum_of_dividers_b and start_b == sum_of_dividers_a :
    sum_of_both = start_a + start_b
    print("BINGO!", " number one=",  start_a, ";  number two=", start_b, ";  sum of both=", sum_of_both)
    if start_b > start_a:
        start_a = start_b + 1
    else:
        start_a += 1
  else:
    start_a += 1
