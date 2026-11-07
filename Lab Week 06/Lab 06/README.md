# Lab 6: NLP Fundamentals, Tokenization, Embeddings and Text Chunking

**Student:** Syed Mudassir Zaib  
**Roll Number:** SU92-BSAIM-F25-232  
**GitHub:** zaibmudassir86-ai  
**Course:** CAI601400, Artificial Intelligence Lab

## Contents

This folder contains 20 Python source files covering the three assessed tasks, five guided scenarios, reusable retrieval and chunking modules, tokenization, embedding examples, FAQ and document chatbots. It also includes the expanded synthetic corpus, labeled queries, output captures, CSV evaluation logs, `requirements.txt` and `Lab6_Report.docx`.

## Setup

Use Python 3.10 or newer. In this folder run:

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

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

The TF-IDF tasks run with NumPy and scikit-learn. The embedding tasks need `sentence-transformers` and an internet connection for the first download of `sentence-transformers/all-MiniLM-L6-v2`. CPU execution is supported. Do not submit the virtual environment or model cache.

## Task 1, tokenization and FAQ

```bash
python task1_tokens.py
python task1_chatbot_check.py
python guided_chatbot.py
```

Run the FAQ assistant with embeddings after installing the model:

```bash
python guided_chatbot.py --backend embedding
```

Exact canonical FAQ questions return the stored answer and source. Other questions show candidates for confirmation. Empty and unsupported inputs use a fallback.

## Task 2, chunking and semantic suggestions

```bash
python task2_chunks.py
python guided_chunks.py
python guided_embeddings.py
python guided_suggestions.py
python task2_semantic_check.py
```

`task2_chunks.py` supports 40 word windows with overlap 0 or 10 and sentence-aware packing with a 40 word budget. Every chunk stores source offsets. `guided_embeddings.py`, `guided_suggestions.py` and `task2_semantic_check.py` require the pretrained encoder.

## Task 3, document retrieval evaluation

```bash
python task3_retrieval.py
python document_chatbot.py
```

The expanded `corpus.json` and labeled `queries.json` are already included, so do not run the dataset generator before the evaluation. The corpus has five expanded synthetic documents. The query file contains eight answerable questions, four for development and four for held out testing, plus two unanswerable questions. The evaluation writes `retrieval_log.csv` and `retrieval_summary.csv`. Unanswerable queries are logged but excluded from answerable Hit@3 and MRR@3.

`create_dataset.py` is an optional starter dataset generator for a clean, separate folder. It intentionally refuses to overwrite an existing `corpus.json` or `queries.json`.

## Guided scenarios

```bash
python scenario1_handbook.py
python scenario2_support.py
python scenario3_docs.py
python scenario4_workplace.py
python scenario5_equipment.py
```

Other guided scripts include `guided_tokens.py`, `guided_chunks.py`, `guided_limits.py` and `guided_metrics.py`.

## Evaluation notes

A chunk counts as relevant only when it belongs to the labeled document and contains the full labeled evidence string. Hit@3 measures whether at least one such chunk occurs in the first three results. MRR@3 is the reciprocal rank of the first relevant chunk. Similarity scores are not probabilities and do not verify truth. Review unanswerable queries and conflicting source passages manually.

The embedding implementation is real and uses Sentence Transformers. If an execution environment lacks the package or model, the evaluation records the embedding configuration as NOT RUN rather than substituting hand-made vectors. The report identifies this limitation.

## Data and safety

All policy, account, returns, workplace and equipment text is synthetic teaching data. It is not actual university or company policy. Do not use this prototype for consequential policy, legal, financial or safety decisions. Keep personal data and credentials out of GitHub.

## References

- Sentence Transformers semantic search: https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html
- Model card: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
