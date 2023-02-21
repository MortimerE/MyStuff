"""import math
queue = [1,3,3,5,6,7,8,10]
node = 3
def bSearch(split, end):
    print(f"split: {split}, end: {end}")
    if split>end: return False
    if split == 0:
        if queue[split] == node:
            return split
        else: return False #not found
    else:
        if queue[split] == node:
            return split
        if queue[split] > node: # go left 
            i = math.floor(split/2)
            return bSearch(i, split-1)
        if queue[split] < node: #go right 
            if split == end:
                return False #node not found
            else: 
                i = math.floor((end-split)/2)
                if i==0: i += 1
                print(f"i: ", i)
                return bSearch(split+i, end)    
        else: return False        
i = math.floor(len(queue)-1/2)
index = bSearch(i, len(queue)-1)
print(index)"""

import heapq
heap= [1,2,3,4]
heapq.heapify(heap)
print(type(heap))
heapq.heappush(heap, [1,0])
heapq.heappush(heap, [1,1])
print(type(heap))