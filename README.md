# learning-python

Personal notes and code while learning Python, mainly from [CS50’s Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/).

## Repository layout

| Path | Purpose |
|------|---------|
| `cs50p/` | Problem sets and lecture exercises from CS50P, organized by week |
| `practice/` | Standalone experiments and small scripts outside the course |

## Running scripts

From the repository root:

```bash
# Lecture examples (week 0)
python3 cs50p/week0/Hello.py
python3 cs50p/week0/calculator.py

# Problem Set 0 (one folder per exercise)
python3 cs50p/week0/indoor/indoor.py
python3 cs50p/week0/tip/tip.py
```

Use `python3` (or `python` on your system) with the path to any `.py` file you want to run.

## CS50P — week 0

### Lecture

| File | Topics |
|------|--------|
| `Hello.py` | `input`, functions, default parameters |
| `calculator.py` | `int`, functions, return values |

### Problem Set 0

Each exercise lives in its own folder under `cs50p/week0/`.

| Folder | Topics |
|--------|--------|
| `indoor/` | strings, `.lower()` |
| `playback/` | strings, `.replace()` |
| `faces/` | string replacement, functions |
| `einstein/` | `int`, f-strings, arithmetic |
| `tip/` | `float`, parsing input, formatted output |

Week folders under `cs50p/` mirror the course (`week0/`, `week1/`, …). Add scripts here as you work through each week.

## Requirements

- Python 3 (no extra dependencies yet)
- A terminal and text editor or IDE of your choice

## License

This repository is for personal learning. CS50 course materials are © Harvard and used under their terms; see [CS50](https://cs50.harvard.edu/) for course policies.
