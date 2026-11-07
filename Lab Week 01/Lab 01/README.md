# Lab 1: Introduction to AI and Paradigms

**Student Name:** Syed Mudassir Zaib  
**Roll Number:** SU92-BSAIM-F25-232  
**Course:** Artificial Intelligence Lab  
**Week:** 1  
**Lab:** 1

## Contents

| File | Purpose |
|---|---|
| `lab1_compare.py` | Compares a symbolic rule with a probability threshold using the supplied lab examples. |
| `lab1_rules.py` | Implements four transparent scholarship screening conditions and exactly four core tests. |
| `Lab1_Report.docx` | Report containing the timeline, implementation explanation, test results, comparison, limitations and reflection. |
| `lab1_compare_output.txt` | Captured output from the comparison script. |
| `lab1_rules_output.txt` | Captured output from the four rule tests. |
| `data/test_cases.csv` | Small CSV fixture documenting the four scholarship test cases. |

## Requirements

- Python 3.8 or later
- Microsoft Word or a compatible DOCX reader for the report

## Run

From this folder, run:

```bash
python lab1_compare.py
python lab1_rules.py
```

## Important assumptions

- The score threshold of 70 and probability threshold of 0.70 are demonstration values from the lab.
- The added conditions in `lab1_rules.py` are synthetic lab assumptions.
- `Review` means that a human reviewer should inspect the application. It does not mean that a scholarship is awarded.
- The probability values are supplied demonstration inputs. No machine learning model is trained, and no predictive accuracy is measured.

## Historical sources

1. Turing, A. M. (1950), *Computing Machinery and Intelligence*: https://plato.stanford.edu/entries/turing/
2. Dartmouth, *The Founding and Future of AI*: https://ai.dartmouth.edu/our-story
3. Actuaries Institute, *History of AI Winters*: https://www.actuaries.asn.au/research-analysis/history-of-ai-winters
4. Krizhevsky, Sutskever and Hinton (2012), *ImageNet Classification with Deep Convolutional Neural Networks*: https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
5. Vaswani et al. (2017), *Attention Is All You Need*: https://research.google/pubs/attention-is-all-you-need/
