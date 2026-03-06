import sys
import fifo
import lru
import optff


# this file reads the input, runs the cache simulations, prints miss count
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    #store the input filename
    input_file = sys.argv[1]

    #open file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            k, m = map(int, f.readline().strip().split())
            requests = list(map(int, f.readline().strip().split()))

    except FileNotFoundError:
        print("The file was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    if len(requests) != m:
        print(f"Error: expected {m} requests, but got {len(requests)}")
        sys.exit(1)

    fifo_misses = fifo.simulate_fifo(k, requests)
    lru_misses = lru.simulate_lru(k, requests)
    optff_misses = optff.simulate_optff(k, requests)

    print(f"FIFO : {fifo_misses}")
    print(f"LRU  : {lru_misses}")
    print(f"OPTFF: {optff_misses}")
    

    
if __name__ == "__main__":
    main()
