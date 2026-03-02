from collections import deque

def simulate_fifo(k, requests):
    misses = 0
    cache = set()
    queue = deque()

    # handle edge case k == 0
    if k == 0:
        return len(requests)
    
    for item in requests:
        if item not in cache:
            misses += 1
            if len(cache) < k:
                cache.add(item)
                queue.append(item)
            else:
                oldest = queue.popleft()
                cache.remove(oldest)
                cache.add(item)
                queue.append(item)

    return misses