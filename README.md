# PLP Python Week 7 - Shopping List Manager

- `list_warmup.py` demonstrates indexing, appending, removing, and using `len()` with a list of fruits.
- `shopping_list.py` creates a small interactive shopping list manager with add, remove, show, and done commands.
- `list_report.py` prints a numbered list, counts items with names longer than four letters, and finds the longest item name.

It is safer to check `in` before calling `.remove()` because `.remove()` raises a `ValueError` when the item is missing. This prevents the program from crashing and lets it handle the situation politely instead.
