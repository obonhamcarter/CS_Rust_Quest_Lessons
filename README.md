# Rust Quest - Coding Adventures 🦀

A friendly Quarto website with beginner Rust mini-lessons for students who have never used Rust before.

## What this project includes

- 19 beginner-to-intermediate Rust quests with introductions, examples, and gentle challenges
- Matching lesson notebooks in:
  - `jupyterlite/content/`
  - `files/lessons/`
- Quarto website pages (`index.qmd`, `all-quests.qmd`, `interactive.qmd`)

## Quests in this version

1. Variables - Your Starter Toolkit
2. Data Types - The Shape of Data
3. Conditionals - Choose Your Path
4. Loops - Repeat with Confidence
5. Vectors - Collecting Data
6. Functions - Reusable Steps
7. HashMaps - Keys and Values
8. Fibonacci - Pattern Practice
9. Sorting - Organizing Data
10. Number Game - Guess and Check
11. Recursion - Functions Calling Themselves
12. Complexity - Why Speed Matters
13. Iterative Loops - Pick the Right Loop
14. Functions Part 2 - Non-Returning
15. Functions Part 3 - Returning Values
16. Closures - Quick Function Tools
17. Higher-Order Functions
18. Wrappers - Add Behavior Around Functions
19. Structs and Impl - Rust Blueprints

## Quick start

### Build the site

```bash
quarto render
```

### Preview locally

```bash
quarto preview
```

## Running Rust code

The lessons contain Rust code snippets. Run them with one of these options:

1. **Rust Playground**: <https://play.rust-lang.org/>
2. **Local Rust**:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustc --version
cargo --version
```

## Notes

- All Quests 1-19 are now Rust-focused in lesson pages and generated notebooks.