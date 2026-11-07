# Lab 3: Uninformed Search

**Student Name:** Syed Mudassir Zaib  
**Roll Number:** SU92-BSAIM-F25-232  
**Manual label:** Lab 3, Week 3

## Files
- `Lab3_Report.docx`: complete report with manual traces, DLS/IDDFS results, weighted graph, UCS comparison, reflection and responsible practice.
- `lab3_bfs_dfs.py`: BFS and DFS implementations with processing and frontier traces.
- `lab3_depth_search.py`: DLS and IDDFS implementations.
- `lab3_ucs.py`: UCS, BFS comparison on the weighted topology, and independent path-cost calculation.
- `*_output.txt`: captured outputs from running each script.
- `data/graph.json`: graph fixture for the search examples.
- `edge_case_tests.py`: start equals goal, unreachable goal and cycle checks.

## Requirements
Python 3. No third-party packages are required for the scripts.

## Run
```bash
python lab3_bfs_dfs.py
python lab3_depth_search.py
python lab3_ucs.py
```

## Assumptions
The original unweighted graph follows the successor order in the manual. In the weighted experiment, the visible manual excerpt does not provide the numeric edge-weight list. Therefore, explicit nonnegative demonstration weights are defined in `lab3_ucs.py` and in the report. The original corridors are retained and `C -> G` is added as instructed.
## Edge case tests

Run `python edge_case_tests.py` to check start equals goal, unreachable goals and cycle handling. The matching output is saved in `outputs/edge_case_tests_output.txt`.
