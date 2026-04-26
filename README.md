# Experiment 06 — Python File Handling

A set of 5 beginner Python exercises focused on file I/O, string operations, and binary file storage using `pickle`.

## Problems

| File | Description |
|------|-------------|
| [problem01.py](problem01.py) | Accept sentences from the user until "END", save to a text file, then print only lines that start with an uppercase letter. |
| [problem02.py](problem02.py) | Count and display the number of characters, words, and lines in a user-entered string. |
| [problem03.py](problem03.py) | Read a text file, search for a given word, and display how many times it appears. |
| [problem04.py](problem04.py) | Store student name/marks records in a binary file using `pickle`, then update a specific student's marks. |
| [problem05.py](problem05.py) | Read numbers from a text file, filter out the odd ones, and store them in a binary file using `pickle`. |

## Concepts Covered

- Text file read/write (`open`, `r`, `w`)
- Binary file read/write (`rb`, `wb`)
- Object serialization with `pickle`
- String methods (`split`, `splitlines`, `isupper`, `lower`)
- Basic loops and conditionals

## How to Run

```bash
python problem01.py
```

> Each script is standalone. Run them individually from the terminal or your IDE.

## Requirements

- Python 3.x
- No external libraries (only built-in `pickle`)
