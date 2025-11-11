

from functools import reduce


num = [1,33,3,33,3,3,44,8,6,7,8,8]

even_no = list(filter(lambda x : x % 2 == 0, num))

dbs = list(map(lambda x : x * 2,even_no))

sum = reduce(lambda x,y : x + y,dbs)
print(dbs)


print(sum)