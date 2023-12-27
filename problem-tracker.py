from datetime import date
from pathlib import Path

# Calculating question counters
lc_sol_dir = Path("C:\\programming\\Leetcode-Solutions")
tot_questions = (date.today() - date(year=2023, month=10, day=1)).days

questions_solved = -1
for f in lc_sol_dir.glob("*.py"): questions_solved+=1

questions_2_solve = tot_questions - questions_solved

# Updating README
old_rd = lc_sol_dir / "README.md"
new_rd = Path(old_rd.parent, f"{old_rd.stem}-temp{old_rd.suffix}")
old_rd.rename(new_rd)

"""
Bug: after the rename statement above executes, the file is not renamed and the program tries
to read and write from the same file? but that doesn't happen and it just ends up renaming the file?
"""

with open(new_rd, "r") as reader, open(lc_sol_dir / "README.md", "w") as writer:
    for line in reader:
        if "**Problems solved:" in line:
            writer.write(f"**Problems solved: {questions_solved}**\n")
        elif "**Problems to solve:" in line:
            writer.write(f"**Problems to solve: {questions_2_solve}**\n")
        elif "_**Total problems I should have solved since day 1:" in line:
            writer.write(f"_**Total problems I should have solved since day 1: {tot_questions}**_\n")
        else:
            writer.writelines(line)

try:
    old_rd.unlink()
except Exception as e:
    print(f"Error while deleting file using pathlib: {e}")