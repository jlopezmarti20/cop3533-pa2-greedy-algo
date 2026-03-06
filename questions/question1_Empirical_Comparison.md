# Question 1: Empirical Comparison

We tested the three caching algorithms (FIFO, LRU, and OPTFF) using three input files located in the `tests/` directory.  
Each test contains 50 page requests with different cache sizes.

| Test File | Cache Size (k) | Requests (m) | FIFO Misses | LRU Misses | OPTFF Misses |
| --------- | -------------- | ------------ | ----------- | ---------- | ------------ |
| test1.in  | 3              | 50           | 47          | 48         | 26           |
| test2.in  | 2              | 50           | 42          | 42         | 26           |
| test3.in  | 4              | 50           | 46          | 46         | 22           |

## Does OPTFF have the fewest misses?

Yes. In all three tests, OPTFF produced the fewest cache misses. This matches theory, since OPTFF (Farthest-in-Future) is the optimal offline caching algorithm and always evicts the page whose next use is farthest in the future.

## How does FIFO compare to LRU?

FIFO and LRU performed very similarly in our tests. In two tests they produced the same number of misses, while in one case LRU had slightly more misses than FIFO. This shows that the performance of these algorithms depends on the specific pattern of page requests.
