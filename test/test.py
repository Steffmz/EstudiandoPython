# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n %2 == 0:
#         if n >= 2 and n <= 5:
#             print("Not weird")
#         if n >= 6 and n <= 20:
#             print("Weird")
#         if n > 20:
#             print("Weird")
#     else:
#         print("Weird")

def is_leap(year):
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    

year = int(input())
print(is_leap(year))