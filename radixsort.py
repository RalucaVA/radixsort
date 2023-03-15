import time
st = time.time()


def countingsort(l, p):
    size = len(l)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = l[i] // p
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = l[i] // p
        output[count[index % 10] - 1] = l[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        l[i] = output[i]
def radixsort(l):
    max_element = max(l)
    p= 1
    while max_element // p > 0:
        countingsort(l, p)
        p *= 10

import random
dataset = []
for i in range(8000):
    #x=random.randrange(0, 30033)
    dataset.append(i)
radixsort(dataset)
print(dataset)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
 
 