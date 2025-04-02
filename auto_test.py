# auto_test.py -- Automated Batch Test Runner for Search Algorithms
# ----------------------------------------------------------------------------------------
# This script automates the testing process for all implemented search algorithms by
# running them against a set of predefined input map files.
#
# Main functionalities:
# 1. Iterates through all `.txt` map files located in the `test_case/` directory.
# 2. Executes each file with every available search method (AS, BFS, DFS, etc.).
# 3. Uses `subprocess.run()` to invoke `search.py <filename> <method>` just like CLI.
# 4. Collects and prints standard output and errors for each execution.
#
# This helps to verify correctness, performance, and consistency of all algorithms.
# Modify the ALGORITHMS or TEST_CASE_DIR variable as needed to customize your tests.
#
# ----------------------------------------------------------------------------------------
# Written by Xiaonan Li, 105206175
# Date: 2025/04/02
#

import os
import subprocess

TEST_CASE_DIR = "test_case/"

test_files = [f for f in os.listdir(TEST_CASE_DIR) if f.endswith(".txt")]

ALGORITHMS = ["AS", "BFS", "DFS", "GBFS", "CUS1", "CUS2"]

PYTHON_CMD = "python"

def run_tests():
    for algo in ALGORITHMS:
        print(f"\n==== Testing algorithm: {algo} ====")
        for file in test_files:
            full_path = os.path.join(TEST_CASE_DIR, file)
            print(f"\n→ Running {file} with {algo}")
            try:
                result = subprocess.run(
                    [PYTHON_CMD, "search.py", full_path, algo],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                print(result.stdout)
                if result.stderr:
                    print("[ERROR]", result.stderr)
            except Exception as e:
                print(f"[Exception] Failed to run {file} with {algo}: {e}")

if __name__ == "__main__":
    run_tests()