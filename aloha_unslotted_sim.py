import random
import numpy as np
from numba import jit

@jit(nopython=True)
def pure_aloha(lamb, p):

    intervals = np.random.exponential(1/lamb, 10000)
    #intervals = np.array(intervals)
    intervals = np.cumsum(intervals)
    limit = intervals[-1] + 1
    current_str = -1
    current_end = 0
    success = 0
    timestamps = []
    backlog = []
    succ_list = []

    while current_end < limit:

        count = 0
        current_str = intervals.min()
        current_end = current_str + 1

        for z in range(len(intervals)):
            temp = intervals[z]
            if (temp <= current_end):
                count += 1
            if temp > current_end:
                break
        
        if count == 1:
            intervals[0] = np.inf
            success += 1

        if count >1:
            for z in range(len(intervals)):
                temp = intervals[z]
                if (temp <= current_end):
                    current_end = intervals[z] + 1
                    intervals[z] = current_end + random.expovariate(p)
                if temp > current_end:
                    break

        succ_list.append(success)
        timestamps.append(current_str)
        backlog.append(count)

        intervals.sort()

    return success/current_end, timestamps, backlog, succ_list

print("Running Case 1...")
#Case 1
results = []
a = np.arange(0.01, 0.5, 0.01)

for z in np.arange(0.01, 0.5, 0.01):
    #print(z)
    test=0
    for _ in range(10):
        cum, timest, backl, succ_ = pure_aloha(0.1, z)
        test += cum
    results.append(test/10)

print("Case 1 Results:")
print(f"    Best mu: {(max(range(len(results)), key=results.__getitem__)*0.01) + 0.01} ----- Best throughput: {max(results)}")

print("Running Case 2...")
#Case 2
results = []
a = np.arange(0.01, 0.5, 0.01)

for z in np.arange(0.01, 0.5, 0.01):
    #print(z)
    test=0
    for _ in range(10):
        cum, timest, backl, succ_ = pure_aloha(0.2, z)
        test += cum
    results.append(test/10)

print("Case 2 Results:")
print(f"    Best mu: {(max(range(len(results)), key=results.__getitem__)*0.01) + 0.01} ----- Best throughput: {max(results)}")
newp = (max(range(len(results)), key=results.__getitem__)*0.01) + 0.01

print("Running Case 3...")
#Case 3
results = []
a = np.arange(0.01, 0.5, 0.01)

for z in np.arange(0.01, 0.5, 0.01):
    #print(z)
    test=0
    for _ in range(10):
        cum, timest, backl, succ_ = pure_aloha(0.3, z)
        test += cum
    results.append(test/10)

print("Case 3 Results:")
print(f"    Best mu: {(max(range(len(results)), key=results.__getitem__)*0.01) + 0.01} ----- Best throughput: {max(results)}")

print("Running Case 4...")
#Case 4
results = []
a = np.arange(0.01, 0.5, 0.01)

for z in np.arange(0.01, 0.5, 0.01):
    #print(z)
    test=0
    for _ in range(10):
        cum, timest, backl, succ_ = pure_aloha(z, newp)
        test += cum
    results.append(test/10)

print("Case 4 Results:")
print(f"    Best lambda: {(max(range(len(results)), key=results.__getitem__)*0.01) + 0.01} ----- Best throughput: {max(results)}")