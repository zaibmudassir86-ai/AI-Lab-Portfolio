# Python code index, Labs 1 to 6

This index maps the practical task requirements to the 35 Python source files in the six weekly folders. Written tasks such as explanations, comparisons and reflections are covered in the corresponding Word report where a separate program is not required by the manual.

## Lab Week 01, Lab 01

Folder: `Lab Week 01/Lab 01/`

- `lab1_rules.py`: scholarship rule checker, added conditions and four tests.
- `lab1_compare.py`: rule based versus probability threshold comparison.
- AI timeline with historical sources and Turing Test versus general intelligence comparison: documented in `Lab1_Report.docx`, because these are research and explanation tasks rather than required executable programs.

## Lab Week 02, Lab 02

Folder: `Lab Week 02/Lab 02/`

- `lab2_percepts.py`: original reflex agent and percept sequence.
- `lab2_model.py`: stateful agent that remembers the previous mode and suppresses duplicate commands.
- `lab2_check.py`: boundary, repeated percept, transition and empty room checks.
- PEAS specifications and environment classifications: documented in `Lab2_Report.docx`, as these are analysis tasks.

## Lab Week 03, Lab 03

Folder: `Lab Week 03/Lab 03/`

- `lab3_bfs_dfs.py`: BFS and DFS traces.
- `lab3_depth_search.py`: DLS and IDDFS with FOUND, CUTOFF and FAILURE outcomes.
- `lab3_ucs.py`: UCS, weighted path cost and BFS comparison.
- `edge_case_tests.py`: start equals goal, unreachable goal and cycle tests for the search algorithms.
- `data/graph.json`: the unweighted and weighted demonstration graphs.

## Lab Week 04, Lab 04

Folder: `Lab Week 04/Lab 04/`

- `lab4_manual_trace.py`: first three A* expansions and frontier trace.
- `lab4_astar_audit.py`: A*, UCS, heuristic audit and overestimate experiment.
- `edge_case_tests.py`: optimal path, start equals goal, unreachable goal, overestimate and invalid node tests.
- `data/campus_graph.json`: graph, heuristic and true remaining costs.

## Lab Week 05, Lab 05

Folder: `Lab Week 05/Lab 05/`

- `lab5_manual_trace.py`: bottom up Minimax trace.
- `lab5_minimax_alphabeta.py`: Minimax and Alpha-Beta, leaf counters and branch ordering.
- `edge_case_tests.py`: matching values, reordered branches, single leaf and invalid empty input.
- `data/game_tree.json`: the manual leaf scores and padded tree.

## Lab Week 06, Lab 06

Folder: `Lab Week 06/Lab 06/`

- Task 1: `task1_tokens.py`, `task1_chatbot_check.py`, `guided_chatbot.py`.
- Task 2: `task2_chunks.py`, `task2_semantic_check.py`, `guided_embeddings.py`, `guided_suggestions.py`.
- Task 3: `task3_retrieval.py`, `document_chatbot.py`, `create_dataset.py`.
- Shared retrieval helper: `lab6_search.py`.
- Guided tokenization, chunking, limits and metrics: `guided_tokens.py`, `guided_chunks.py`, `guided_limits.py`, `guided_metrics.py`.
- Guided scenarios: `scenario1_handbook.py`, `scenario2_support.py`, `scenario3_docs.py`, `scenario4_workplace.py`, `scenario5_equipment.py`.

See the Lab 6 README for installation and run commands. The embedding files use the actual Sentence Transformers model and need the package and model download.
