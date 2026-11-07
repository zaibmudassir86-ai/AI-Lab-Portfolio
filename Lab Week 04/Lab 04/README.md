# Lab 4: Informed Search, Heuristics and A*

**Student:** Syed Mudassir Zaib  
**Roll Number:** SU92-BSAIM-F25-232  
**GitHub username:** zaibmudassir86-ai

## Files
- `Lab4_Report.docx`: manual A* frontier trace, heuristic audit, A*/UCS comparison, overestimate experiment, edge cases and reflection.
- `lab4_astar_audit.py`: A*, UCS control, heuristic audit, overestimate experiment and edge-case tests.
- `lab4_manual_trace.py`: reproducible frontier trace for the first three A* expansions.
- `lab4_astar_output.txt`: captured A*, UCS and overestimate results.
- `lab4_manual_trace_output.txt`: captured manual frontier trace.
- `data/campus_graph.json`: graph, edge costs, heuristic estimates and true remaining costs.
- `edge_case_tests.py`: optimality and input edge case checks.

## Run
```bash
python lab4_astar_audit.py
python lab4_manual_trace.py
```
Requires Python 3 only. No third-party packages are required.

## Counting convention
A node is counted as expanded when its successors are examined. The goal is processed but not counted as expanded. Stale queue entries are ignored. Queue entries are ordered by `(f, g, node, path)`.

## Graph and heuristic
The supplied directed graph and heuristic are reproduced in the source code. Edge costs and heuristic estimates use the same abstract travel-time units. They are not real campus measurements.
## Edge case tests

Run `python edge_case_tests.py` to check the optimal route, start equals goal, unreachable goals, an overestimated heuristic and invalid start nodes. The output is saved in `outputs/edge_case_tests_output.txt`.
