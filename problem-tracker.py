import pathlib
from datetime import date
lc_sol_dir = pathlib.Path("C:\programming\Leetcode-Solutions")
tot_questions = (date.today() - date(year=2023, month=10, day=1)).days

questions_solved = -1
for f in lc_sol_dir.glob("*.py"): questions_solved+=1

questions_2_solve = tot_questions - questions_solved