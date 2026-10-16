# Student Grade Calculator

**Student Name:** Xyrad Caballero  
**Section:** BSIT-3R10  
**Course:** Bachelor of Science in Information Technology  

---

## 📖 Program Description

The **Student Grade Calculator** is a command-line interface (CLI) Python application created to compute and evaluate student academic performance efficiently. It takes scores across weighted course components (Quizzes, Assignments & Activities, Midterm Examination, and Final Examination), validates the input scores, calculates the final weighted percentage, and maps the result to both letter grades (A–F) and the standard Philippine collegiate 1.00–5.00 grading scale. Additionally, it outputs academic status remarks such as President's Lister, Dean's Lister, or Passed status.

---

## 🚀 How to Run the Program

### Prerequisites
- Python 3.8 or higher installed on your machine. Check by running:
  ```bash
  python --version
  ```

### Steps to Run
1. Open your terminal, Command Prompt, or PowerShell in this project directory:
   ```bash
   cd "path/to/repository"
   ```
2. Execute the Python script:
   ```bash
   python grade_calculator.py
   ```
3. Follow the on-screen prompts:
   - Enter the student's name and subject code/title.
   - Enter the numerical score (0 to 100) for each assessment component.
   - View the generated grade breakdown report.
   - Choose whether to calculate another grade or exit the application.

---

## 📊 Assessment Weight Distribution

| Component | Weight |
|---|---|
| Quizzes | 20% |
| Assignments & Activities | 20% |
| Midterm Examination | 25% |
| Final Examination | 35% |
| **Total** | **100%** |

### Grading Scale Reference

| Percentage Range | Collegiate Grade | Letter Grade | Academic Remarks |
|---|---|---|---|
| 97.0% – 100.0% | 1.00 | A | PASSED (President's Lister / Highest Honors) |
| 94.0% – 96.99% | 1.25 | A | PASSED (Dean's Lister / High Honors) |
| 91.0% – 93.99% | 1.50 | A | PASSED (With Honors) |
| 88.0% – 90.99% | 1.75 | B | PASSED (With Honors) |
| 85.0% – 87.99% | 2.00 | B | PASSED (Satisfactory) |
| 82.0% – 84.99% | 2.25 | B | PASSED (Satisfactory) |
| 79.0% – 81.99% | 2.50 | C | PASSED (Satisfactory) |
| 76.0% – 78.99% | 2.75 | C | PASSED (Satisfactory) |
| 75.0% – 75.99% | 3.00 | D | PASSED (Satisfactory) |
| Below 75.0% | 5.00 | F | FAILED (Needs Remedial / Retake Course) |

---

## 📝 Git Reflection (150–200 Words)

> **Word Count: 169 words**

While working on this assignment, I encountered an unexpected Git merge conflict when trying to merge my feature branch back into the main branch. I had modified the core calculation function in the feature branch while simultaneously adjusting the input handling logic on main without pulling latest changes. When executing `git merge`, Git halted the process, warning that automatic merge had failed and leaving conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) inside `grade_calculator.py`.

At first, this was intimidating because I worried about corrupting my commit history. To resolve the issue systematically, I opened the conflicting file in my code editor, carefully compared the conflicting blocks, and kept the necessary logic from both branches while deleting the conflict markers. Afterward, I ran `git status` to verify the modified file, tested the program using `python grade_calculator.py` to ensure runtime functionality, staged the resolved file with `git add`, and finalized the merge using `git commit`. This experience taught me the critical importance of keeping branches synchronized and gave me confidence in troubleshooting and resolving version control conflicts.

---

## 🌳 Repository Structure & Commit Log

```
.
├── .gitignore             # Git ignore file for Python & OS files
├── grade_calculator.py    # Main Python grade calculator program
├── README.md              # Project documentation and student information
└── REFLECTION.md          # Dedicated copy of Git reflection essay
```
