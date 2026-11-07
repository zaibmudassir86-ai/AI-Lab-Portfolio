# Lab 2: Intelligent Agents and the PEAS Framework

**Student:** Syed Mudassir Zaib  
**Roll Number:** SU92-BSAIM-F25-232  
**GitHub username:** zaibmudassir86-ai

## Files
- `Lab2_Report.docx`: PEAS specifications, environment classifications, implementation explanation, trace, tests, limitations and reflection.
- `lab2_percepts.py`: original reflex agent and supplied percept sequence.
- `lab2_model.py`: stateful agent that suppresses repeated identical target commands.
- `lab2_check.py`: small verification checks.
- `*_output.txt`: captured program outputs.
- `data/percepts.csv`: sample percept sequence used for the agent exercise.

## Run
Use Python 3. Run these commands from this folder:

```bash
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```

No third-party packages are required.

## Important assumptions
- Classroom modes are simulated labels. No physical hardware is controlled.
- The first target command is sent because the stored previous mode starts as `None`.
- Empty-room priority and the original strict thresholds are preserved.
- The delivery robot and student-support environment labels are qualified by their model boundaries in the report.

## Test result
All five checks in `lab2_check.py` passed in the captured run.
