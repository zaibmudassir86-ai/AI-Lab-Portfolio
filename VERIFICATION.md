# Repository verification

Verification was performed on 7 November 2026 in the preparation environment.

## Checks completed

| Check | Result |
|---|---|
| Python source files parsed with Python AST | 35 files, no syntax errors |
| Labs 1 and 2 program runs | Completed |
| Labs 3, 4 and 5 main program runs | Completed |
| Labs 3, 4 and 5 edge case test runners | Completed |
| Lab 6 tokenization, chunking, metrics and FAQ checks | Completed where dependencies were available |
| Lab 6 five guided scenario scripts | Completed |
| Lab 6 TF IDF retrieval evaluation | Completed for all three chunking strategies |
| Lab 6 Sentence Transformers evaluation | Not run, package and model were unavailable in this environment |
| Interactive chatbot transcripts | Captured separately in the Lab 6 folder |

## Lab 6 TF IDF results

The evaluation used four answerable development queries and four answerable held out test queries. Two unanswerable queries were retained in the retrieval log and excluded from answerable Hit@3 and MRR@3.

| Chunking strategy | Development Hit@3 | Development MRR@3 | Test Hit@3 | Test MRR@3 |
|---|---:|---:|---:|---:|
| 40 word windows, overlap 0 | 0.750 | 0.750 | 0.750 | 0.583 |
| 40 word windows, overlap 10 | 1.000 | 0.875 | 0.750 | 0.750 |
| Sentence aware, 40 word budget | 0.750 | 0.750 | 0.500 | 0.500 |

The 40 word window with 10 word overlap was selected using development results. The held out test results are reported without retuning. These results describe this small synthetic dataset only.

## Embedding limitation

The `sentence-transformers` package and pretrained model were unavailable in the preparation environment. Embedding scripts retain the real model implementation and print a clear not run message when the dependency is missing. No embedding scores or semantic improvements are claimed. Install the packages in `requirements.txt` and allow the first model download before running the embedding experiments.

## Interactive scripts

`guided_chatbot.py` and `document_chatbot.py` require terminal input. Their sample transcripts are included as text files.
