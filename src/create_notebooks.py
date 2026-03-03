"""Generate Rust Quest notebooks for Quests 1-19 and sync download copies."""

from __future__ import annotations

import json
import shutil
from pathlib import Path


LESSONS = [
    (1, "variables", "Variables - Your Starter Toolkit"),
    (2, "data-types", "Data Types - The Shape of Data"),
    (3, "conditionals", "Conditionals - Choose Your Path"),
    (4, "loops", "Loops - Repeat with Confidence"),
    (5, "lists", "Vectors - Collecting Data"),
    (6, "functions", "Functions - Reusable Steps"),
    (7, "dictionaries", "HashMaps - Keys and Values"),
    (8, "fibonacci", "Fibonacci - Pattern Practice"),
    (9, "sorting", "Sorting - Organizing Data"),
    (10, "number-game", "Number Game - Guess and Check"),
    (11, "recursion", "Recursion - Functions Calling Themselves"),
    (12, "complexity", "Complexity - Why Speed Matters"),
    (13, "iterative-loops", "Iterative Loops - Pick the Right Loop"),
    (14, "functions-non-returning", "Functions Part 2 - Non-Returning"),
    (15, "functions-returning", "Functions Part 3 - Returning Values"),
    (16, "lambda-functions", "Closures - Quick Function Tools"),
    (17, "higher-order-functions", "Higher-Order Functions"),
    (18, "decorators", "Wrappers - Add Behavior Around Functions"),
    (19, "classes", "Structs and Impl - Rust Blueprints"),
]


RUST_EXAMPLES = {
    1: """fn main() {
    let mut hp = 3;
    hp += 1;
    println!(\"HP: {}\", hp);
}""",
    2: """fn main() {
    let score: i32 = 100;
    let ratio: f64 = 1.5;
    let passed: bool = true;
    println!(\"{} {} {}\", score, ratio, passed);
}""",
    3: """fn main() {
    let coins = 7;
    if coins >= 10 { println!(\"Buy potion\"); }
    else { println!(\"Save more coins\"); }
}""",
    4: """fn main() {
    for n in 1..=5 {
        println!(\"{}\", n);
    }
}""",
    5: """fn main() {
    let mut items = vec![\"map\", \"torch\"];
    items.push(\"key\");
    println!(\"{:?}\", items);
}""",
    6: """fn add(a: i32, b: i32) -> i32 { a + b }
fn main() { println!(\"{}\", add(2, 3)); }""",
    7: """use std::collections::HashMap;
fn main() {
    let mut stock = HashMap::new();
    stock.insert(\"apple\", 4);
    println!(\"{:?}\", stock.get(\"apple\"));
}""",
    8: """fn fib(n: usize) -> Vec<u64> {
    let mut seq = vec![0, 1];
    while seq.len() < n {
        let len = seq.len();
        seq.push(seq[len - 1] + seq[len - 2]);
    }
    seq
}
fn main() { println!(\"{:?}\", fib(10)); }""",
    9: """fn main() {
    let mut values = vec![9, 2, 7, 1, 5];
    values.sort();
    println!(\"{:?}\", values);
}""",
    10: """fn main() {
    let secret = 7;
    let guess = 5;
    if guess == secret { println!(\"Correct\"); }
    else if guess < secret { println!(\"Too low\"); }
    else { println!(\"Too high\"); }
}""",
    11: """fn factorial(n: u64) -> u64 {
    if n <= 1 { 1 } else { n * factorial(n - 1) }
}
fn main() { println!(\"{}\", factorial(5)); }""",
    12: """fn linear_search(data: &[i32], target: i32) -> bool {
    for item in data { if *item == target { return true; } }
    false
}
fn main() { println!(\"{}\", linear_search(&[3, 8, 12], 8)); }""",
    13: """fn main() {
    let mut n = 3;
    while n > 0 { println!(\"{}\", n); n -= 1; }
}""",
    14: """fn show_banner(name: &str) {
    println!(\"Welcome, {}!\", name);
}
fn main() { show_banner(\"Rust Learner\"); }""",
    15: """fn is_even(n: i32) -> bool { n % 2 == 0 }
fn main() { println!(\"{}\", is_even(8)); }""",
    16: """fn main() {
    let nums = vec![1, 2, 3];
    let doubled: Vec<i32> = nums.iter().map(|n| n * 2).collect();
    println!(\"{:?}\", doubled);
}""",
    17: """fn apply_twice<F>(v: i32, f: F) -> i32 where F: Fn(i32) -> i32 {
    f(f(v))
}
fn main() { println!(\"{}\", apply_twice(5, |x| x + 2)); }""",
    18: """fn with_logging<F>(name: &str, action: F) where F: Fn() {
    println!(\"[start] {}\", name);
    action();
    println!(\"[end] {}\", name);
}
fn main() { with_logging(\"demo\", || println!(\"hello\")); }""",
    19: """struct Hero { name: String, hp: i32 }
impl Hero {
    fn describe(&self) { println!(\"{} has {} HP\", self.name, self.hp); }
}
fn main() {
    let hero = Hero { name: String::from(\"Luna\"), hp: 60 };
    hero.describe();
}""",
}


def notebook_for_lesson(quest_num: int, slug: str, title: str) -> dict:
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"# Quest {quest_num}: {title} 🦀\n",
                "\n",
                "Welcome! This notebook is beginner-friendly and uses Rust examples.\n",
                "\n",
                "Run code in Rust Playground: <https://play.rust-lang.org/>\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Rust Example\n",
                "\n",
                "```rust\n",
                RUST_EXAMPLES[quest_num],
                "\n```\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Gentle Challenge\n",
                "\n",
                "1. Copy the Rust snippet into Rust Playground.\n",
                "2. Change one value.\n",
                "3. Re-run and describe what changed.\n",
            ],
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                f"Want full notes? Open `lessons/{quest_num:02d}-{slug}.qmd`.\n",
            ],
        },
    ]

    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    jupyter_dir = repo_root / "jupyterlite" / "content"
    download_dir = repo_root / "files" / "lessons"

    jupyter_dir.mkdir(parents=True, exist_ok=True)
    download_dir.mkdir(parents=True, exist_ok=True)

    for quest_num, slug, title in LESSONS:
        file_name = f"{quest_num:02d}-{slug}.ipynb"
        notebook = notebook_for_lesson(quest_num, slug, title)

        target = jupyter_dir / file_name
        target.write_text(json.dumps(notebook, indent=2, ensure_ascii=False), encoding="utf-8")
        shutil.copy2(target, download_dir / file_name)
        print(f"✅ Synced {file_name}")


if __name__ == "__main__":
    main()
