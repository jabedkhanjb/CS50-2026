# CS50 Learning Codebase - AI Agent Instructions

## Project Overview

This is a progressive learning codebase from Harvard's CS50 course demonstrating fundamental Python concepts. Files are sequenced by complexity, from basic I/O to functions with return values.

### File Progression
- **1stcode.py**: String manipulation (input, strip, capitalize, title, f-strings)
- **2ndcode.py**: Chained string methods and formatting
- **3rdcode.py**: Numeric operations (int, float, rounding, formatting with precision)
- **4thcode.py**: Function basics (definition, parameters, default arguments)
- **5thcode_function.py**: Function definition patterns and organization
- **6thcode_return.py**: Return values with `main()` pattern

## Code Patterns & Conventions

### Input Processing Pattern
Always chain methods for cleaner code:
```python
name = input("Enter your name: ").strip().title()
```
Rather than multi-line assignments. The pattern is: **input() → strip() → convert case → use**

### Function Organization
- Use `main()` as entry point (preferred in recent files)
- Define helper functions before `main()`
- Call `main()` at module end
```python
def main():
    # orchestration logic
    
def helper_function():
    # reusable logic
    
main()
```

### Default Parameters
Functions use default arguments for optional inputs:
```python
def hello(to="World!"):
    print("Hello,", to)
```

### Numeric Formatting
- Use `round(value, decimals)` for precision
- Use f-strings with format specifiers: `f"{value:.2f}"` or `f"{value:,}"`

## Testing & Execution

All files are standalone scripts with built-in user input. Run with:
```bash
python3.11 filename.py
```

No external dependencies. Each file demonstrates isolated concepts and should execute successfully.

## Common Editor State

- Workspace root: `/Users/jabedkhan/MacOS Disk 1/Software Engineering/CS50/`
- Python version: 3.11 (via homebrew)
- Terminal execution context preserved across session

## AI Agent Guidelines

1. **Maintain progression**: When modifying files, preserve the learning sequence—simpler concepts in early files, advanced in later ones
2. **String method chaining**: Prefer chained methods over intermediate variables for I/O processing
3. **Function architecture**: New functions should follow main() pattern with helper functions defined first
4. **Comments in code**: Current codebase uses minimal comments; preserve this style unless demonstrating a new concept
5. **Input validation**: Current code lacks error handling—maintain this unless explicitly asked to add robustness
