from utils import timer
from algorithms import simple
import random

med_size=10**1
large_size=10**6

M_sm=[1,0,1,1,3,4]

M_med_rand=[random.randrange(0,med_size) for i in range(med_size)]
M_med_sequential=list(range(1,med_size))+[0]

print(M_med_sequential)



timer.start('Test')
print(simple(M))
timer.end('Test')
