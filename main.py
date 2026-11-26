"""My Deploy'S Been Stuck Since: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'Worst Monday One-Liners' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 122 UTF-8 characters, inside the 1-140 gate.
"""
import os

LINE = "My deploy's been stuck since 9 a.m., my inbox has 400 unread, and stand-up just asked if I'm 'blocked' — yes, by stand-up."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
