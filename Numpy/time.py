import time
import numpy as np
x = np.random.random(100000000)

start = time.time()
sum(x) / len(x)
print(time.time() - start)

start = time.time()
np.mean(x)
print(time.time() - start)