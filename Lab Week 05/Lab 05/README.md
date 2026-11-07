# Lab 5: Adversarial Search, Minimax and Alpha-Beta Pruning

**Student:** Syed Mudassir Zaib  
**Roll Number:** SU92-BSAIM-F25-232  
**GitHub username:** zaibmudassir86-ai

## Files
- `Lab5_Report.docx`: manual Minimax trace, leaf counter comparison, branch reordering, edge cases, limitations and reflection.
- `lab5_minimax_alphabeta.py`: Minimax and Alpha-Beta implementations with leaf counters and tests.
- `lab5_manual_trace.py`: bottom-up hand trace.
- `lab5_output.txt`: captured algorithm output.
- `lab5_manual_trace_output.txt`: captured manual trace.
- `data/game_tree.json`: leaf scores and tree configuration.
- `edge_case_tests.py`: branch order, equal values, single leaf and invalid input checks.

## Run
```bash
python lab5_minimax_alphabeta.py
python lab5_manual_trace.py
```
Requires Python 3 only. No third-party packages are required.

## Reproducibility notes
The six supplied leaf scores are padded with two zeros as shown in the manual. Both algorithms use the same eight-leaf tree. Leaf counters increment only when a terminal utility is evaluated. Branch reordering reverses sibling order while preserving each subtree's descendants.
## Edge case tests

Run `python edge_case_tests.py` to verify Minimax and Alpha Beta values, branch reordering, the single leaf case and empty input handling. The output is saved in `outputs/edge_case_tests_output.txt`.
