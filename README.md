# Artificial Intelligence Lab Portfolio

A collection of practical assignments for the **BS Artificial Intelligence** course. This repository contains the work for Labs 1 to 6, with each lab kept in its own weekly folder.

**Student:** Syed Mudassir Zaib  
**Course:** Artificial Intelligence Lab, CAI601400  
**GitHub:** [zaibmudassir86-ai](https://github.com/zaibmudassir86-ai)

## Repository overview

| Week | Lab topic | Main work | Folder |
|---|---|---|---|
| 01 | Introduction to AI and paradigms | AI timeline, rule based scholarship checker, Turing Test comparison | [Lab Week 01](Lab%20Week%2001/Lab%2001/) |
| 02 | Intelligent agents and PEAS | Agent percepts, stateful control, environment analysis | [Lab Week 02](Lab%20Week%2002/Lab%2002/) |
| 03 | Uninformed search | BFS, DFS, DLS, IDDFS and UCS | [Lab Week 03](Lab%20Week%2003/Lab%2003/) |
| 04 | Informed search | Heuristics, A*, UCS comparison and heuristic checks | [Lab Week 04](Lab%20Week%2004/Lab%2004/) |
| 05 | Adversarial search | Minimax, Alpha Beta pruning and leaf evaluation counts | [Lab Week 05](Lab%20Week%2005/Lab%2005/) |
| 06 | NLP fundamentals | Tokenization, chunking, TF IDF, sentence embeddings and retrieval | [Lab Week 06](Lab%20Week%2006/Lab%2006/) |

Each lab folder contains its own `README.md`, Python source files, supporting data, captured outputs where available, and a Word report. The [Python task index](TASK_CODE_INDEX.md) maps the practical requirements to their source files. The portfolio contains **35 Python source files**. See [VERIFICATION.md](VERIFICATION.md) for the latest test record and measured Lab 6 TF IDF results.

## Quick start

### 1. Get the repository

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace the placeholders with the public repository URL and folder name shown on GitHub.

### 2. Python version

Use Python 3.10 or newer for the full portfolio. Labs 1 to 5 use the Python standard library and do not need third party packages.

### 3. Install Lab 6 dependencies

Create and activate a virtual environment from the repository root, then install the requirements:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

Install the packages used by the NLP lab:

```bash
python -m pip install -r requirements.txt
```

The sentence embedding model downloads the first time an embedding script runs. It can run on CPU. No GPU is required. Do not commit the virtual environment, downloaded model files or private credentials.

## Run a lab

Open the relevant lab folder in a terminal. For example, to run the Week 3 search exercises:

```bash
cd "Lab Week 03/Lab 03"
python lab3_bfs_dfs.py
python lab3_depth_search.py
python lab3_ucs.py
python edge_case_tests.py
```

Use the README inside each lab folder for its complete run commands and notes. Interactive programs, such as the FAQ and document chatbots in Lab 6, wait for terminal input.

## Lab 6 notes

Lab 6 compares lexical TF IDF retrieval with a real pretrained Sentence Transformers encoder. Its data is synthetic teaching material, not actual university, company or legal policy. The embedding scripts require the dependencies in `requirements.txt` and access to download the model on first use.

The saved evaluation files distinguish completed TF IDF runs from embedding runs that were not available in the preparation environment. Do not treat a similarity score as proof that a passage is correct or complete.

## Repository contents

```text
.
|-- Lab Week 01/
|   `-- Lab 01/
|-- Lab Week 02/
|   `-- Lab 02/
|-- Lab Week 03/
|   `-- Lab 03/
|-- Lab Week 04/
|   `-- Lab 04/
|-- Lab Week 05/
|   `-- Lab 05/
|-- Lab Week 06/
|   `-- Lab 06/
|-- README.md
|-- TASK_CODE_INDEX.md
|-- NOTICE.md
|-- VERIFICATION.md
|-- requirements.txt
`-- .gitignore
```

## Reports and outputs

The `LabN_Report.docx` file in each lab folder contains the written analysis and task explanations. Output text files and CSV logs are included where relevant so that the recorded results can be inspected without rerunning every script.

## Sources and academic use

The practical tasks follow the course supplied *CAI601400 Artificial Intelligence Lab Manual*. Some exercises adapt the reference procedures supplied in that manual. External technical references are listed in the relevant lab README files. See [NOTICE.md](NOTICE.md) for attribution and data notes.

This repository is a student learning portfolio. Review the code, assumptions and source material before reusing it. No license is declared for third party course material.

## Current scope

This repository currently includes Labs 1 to 6. Later labs can be added as new weekly folders while keeping the same structure.
