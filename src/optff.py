import heapq
from utils.io import read_input
def simulate_optff(k, requests):
    n = len(requests)
    next_occ = [float("inf")] * n
    prev_seen = {}
    # preprocess data
    for i in range(n - 1, -1, -1):
        curr = requests[i]
        if curr in prev_seen:
            next_occ[i] = prev_seen[curr]
        prev_seen[curr] = i

    cache = set()
    misses = 0
    hp = []
    for i in range(n):
        curr = requests[i]
        # print(curr, cache)
        if curr in cache:
            heapq.heappush(hp, (-next_occ[i], curr))
            continue
        misses += 1
        if len(cache) < k:
            cache.add(curr)
        else:
            while True:
                _, cache_cand = heapq.heappop(hp)
                if cache_cand in cache:
                    break
            cache.remove(cache_cand)
            cache.add(curr)
        heapq.heappush(hp, (-next_occ[i], curr))
    return misses

if __name__ == "__main__":
    k, requests = read_input("example.in")
    misses = simulate_optff(k, requests)
    print(misses)
        

    