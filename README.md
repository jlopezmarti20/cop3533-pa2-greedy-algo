# COP3533 Programming Assignment 2 — Greedy Caching Algorithms

## Members

Jesus Lopez - 13

## Testing Results

We tested the three caching algorithms (FIFO, LRU, and OPTFF) using three input files located in the `tests/` directory.  
Each test contains **50 page requests** with different cache sizes.

| Test File | Cache Size (k) | Requests (m) | FIFO Misses | LRU Misses | OPTFF Misses |
| --------- | -------------- | ------------ | ----------- | ---------- | ------------ |
| test1.in  | 3              | 50           | 47          | 48         | 26           |
| test2.in  | 2              | 50           | 42          | 42         | 26           |
| test3.in  | 4              | 50           | 46          | 46         | 22           |

## Observations

- OPTFF consistently produced the fewest cache misses, which matches theory since OPTFF is the optimal offline caching algorithm that uses knowledge of future requests to make eviction decisions.
- FIFO and LRU sometimes produced the same number of misses, depending on the request pattern.
- In some sequences (such as Test 1), LRU performed slightly worse than FIFO, showing that cache performance depends heavily on the access pattern.

## How to Run

From the root directory of the repository:

```bash
python src/main.py <input_file>

## Example

python src/main.py tests/test1.in
```
