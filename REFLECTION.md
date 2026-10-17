# Individual Assignment: Git Reflection

**Student Name:** Xyrad Caballero  
**Section:** BSIT-3R10  
**Word Count:** 169 words  

---

### Reflection: A Git Challenge and Resolution

While working on this assignment, I encountered an unexpected Git merge conflict when trying to merge my feature branch back into the main branch. I had modified the core calculation function in the feature branch while simultaneously adjusting the input handling logic on main without pulling latest changes. When executing `git merge`, Git halted the process, warning that automatic merge had failed and leaving conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) inside `grade_calculator.py`.

At first, this was intimidating because I worried about corrupting my commit history. To resolve the issue systematically, I opened the conflicting file in my code editor, carefully compared the conflicting blocks, and kept the necessary logic from both branches while deleting the conflict markers. Afterward, I ran `git status` to verify the modified file, tested the program using `python grade_calculator.py` to ensure runtime functionality, staged the resolved file with `git add`, and finalized the merge using `git commit`. This experience taught me the critical importance of keeping branches synchronized and gave me confidence in troubleshooting and resolving version control conflicts.
