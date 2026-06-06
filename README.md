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
python3 cs50p/week0/Hello.py
python3 cs50p/week0/tip/tip.py
python3 cs50p/week1/compare.py
python3 cs50p/week1/grade.py
python3 cs50p/week1/parity.py
python3 cs50p/week1/deep_thought/deep.py
python3 cs50p/week1/bank/bank.py
python3 cs50p/week1/extensions/extensions.py
python3 cs50p/week1/interpreter/interpreter.py
python3 cs50p/week1/meal/meal.py
```

Use `python3` (or `python` on your system) with the path to any `.py` file you want to run.

## CS50P

Week folders under `cs50p/` mirror the course (`week0/`, `week1/`, …).

### Week 0 — Functions, Variables

**Lecture**

| File | Topics |
|------|--------|
| `Hello.py` | `input`, functions, default parameters |
| `calculator.py` | `int`, functions, return values |

**Problem Set 0** (one folder per exercise)

| Folder | Topics |
|--------|--------|
| `indoor/` | strings, `.lower()` |
| `playback/` | strings, `.replace()` |
| `faces/` | string replacement, functions |
| `einstein/` | `int`, f-strings, arithmetic |
| `tip/` | `float`, parsing input, formatted output |

### Week 1 — Conditionals

**Lecture**

| File | Topics |
|------|--------|
| `compare.py` | `if` / `else`, equality |
| `grade.py` | `elif` chains, score ranges |
| `parity.py` | modulo, functions, even/odd |
| `house.py` | `match` / `case`, pattern matching |

**Problem Set 1** (one folder per exercise)

| Folder | Topics |
|--------|--------|
| `deep_thought/` | conditionals, string normalization, `in` |
| `bank/` | `.startswith()`, `elif` chains |
| `extensions/` | `.endswith()`, MIME types |
| `interpreter/` | `.split()`, arithmetic, `float` |
| `meal/` | time parsing, ranges, functions |

## Requirements

- Python 3 (no extra dependencies yet)
- A terminal and text editor or IDE of your choice

## License

This repository is for personal learning. CS50 course materials are © Harvard and used under their terms; see [CS50](https://cs50.harvard.edu/) for course policies.
