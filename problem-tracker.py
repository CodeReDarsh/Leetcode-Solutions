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

new_rd.touch()

"""
Bug fixed by creating new temp file, writing to it and then deleting the old file and renaming new one.
Originally I was trying to rename the old file to README-temp.md after which I was trying to create a new file via open(lc_sol_dir / "README.md", "w").
I would then try to read from README-temp and write into README. I assumed it would rename the old file in time before trying to create a new readme file 
but that wasn't working for some reason and the program would run but not do anything other than just rename the readme file.
"""

with open(old_rd, "r") as reader, open(new_rd, "w") as writer:
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
    new_rd.rename(Path(new_rd.parent, f"README.md"))
except Exception as e:
    print(f"Error while deleting file using pathlib: {e}")