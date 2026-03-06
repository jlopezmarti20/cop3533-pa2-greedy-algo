# COP3533 Programming Assignment 2 — Greedy Caching Algorithms

## Students

- Jesus Lopez — UFID: 1328-5108

---

# Project Overview

This project implements and compares three caching algorithms:

- FIFO (First-In First-Out)
- LRU (Least Recently Used)
- OPTFF (Farthest-in-Future / Optimal Caching)

The program reads a sequence of page requests and reports the number of cache misses for each caching policy.

---

# How to Run the Program

From the root directory of the repository:

```bash
python src/main.py <input_file>
```

Example:

```bash
python src/main.py data/example.in
```

or

```bash
python src/main.py tests/test1.in
```

---

## Input Format

Each input file follows this format:

```
k m
r1 r2 r3 ... rm
```

Where:

- k = cache size
- m = number of page requests
- r1 ... rm = sequence of page requests

Example:

```
3 12
1 2 3 4 1 2 5 1 2 3 4 5
```

## Output Format

The program prints the number of cache misses for each policy:

```
FIFO : X
LRU  : X
OPTFF: X
```

---

## Test Inputs

Test input files are located in the `tests/` directory:

```
tests/
test1.in
test2.in
test3.in
test_bad_sequence.in
```

Example:

```bash
python src/main.py tests/test1.in
```

---

## Written Questions

The written components of the assignment are located in the `questions/` directory:

```
questions/
question1_Empirical_Comparison.md
question2_bad_sequence.md
question3_FF_optimality.png
```

These files contain the answers to the written questions for the assignment.
