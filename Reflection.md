1. Which issues were the easiest to fix, and which were the hardest? Why?

•	Easiest:
The simplest fixes were related to naming conventions, unused imports, and adding file encoding. These changes were straightforward and didn’t affect the logic of the program. Similarly, replacing the bare except: with a specific except KeyError: was quick and clear.
•	Hardest:
The hardest issue was removing the use of eval() because it required rethinking the logic for how input commands were processed safely. Another slightly challenging part was implementing input validation since it involved checking multiple types and ensuring that validation didn’t break the existing functionality.

2. Did the static analysis tools report any false positives? If so, describe one example.

Yes. Pylint flagged a “missing docstring” warning for every function, even though the script was relatively small and self-explanatory. While technically correct, in this educational context, those warnings didn’t indicate an actual defect and could be considered false positives or low-priority issues.

3. How would you integrate static analysis tools into your actual software development workflow?
•	I would integrate tools like Pylint, Flake8, and Bandit into a Continuous Integration (CI) pipeline (e.g., GitHub Actions) to automatically run checks on every push or pull request.
•	During local development, I would use a pre-commit hook to ensure code passes static checks before it’s committed.
•	This ensures code quality, prevents bad practices (like eval() or bare exceptions), and maintains consistent formatting across the team.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
•	The code became safer by eliminating dangerous constructs like eval() and ensuring exceptions are handled explicitly.
•	Readability improved through consistent naming (snake_case), clear output formatting, and proper logging.
•	Robustness increased by adding input validation, safe file handling, and encoding support, preventing crashes and data corruption.
•	Overall, the script now feels more maintainable and professional, ready for integration into larger systems.

