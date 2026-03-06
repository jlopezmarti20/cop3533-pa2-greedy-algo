# Question 2: Bad Sequence for LRU or FIFO (k = 3)

For cache size k = 3, there does exist a request sequence where OPTFF incurs strictly fewer misses than LRU.

We used the following request sequence:

- k = 3
- m = 13
- Requests: `1 2 3 4 1 2 3 5 1 2 3 4 5`

(Stored as `tests/test_bad_sequence.in`.)

After running the test:

`python src/main.py tests/test_bad_sequence.in`

- FIFO: 13
- LRU: 13
- OPTFF: 8

So, OPTFF has strictly fewer misses than LRU (8 < 13), and also fewer than FIFO (8 < 13).
In this sequence, new pages like 4 and 5 appear, which forces the cache to evict one of the pages already stored. LRU removes the page that was used least recently. However, in this sequence that page often gets requested again very soon, which causes additional cache misses. OPTFF, on the other hand, looks at the future requests and removes the page whose next use is the farthest away. Because of this, it avoids evicting pages that will be needed again soon, which results in fewer cache misses.
