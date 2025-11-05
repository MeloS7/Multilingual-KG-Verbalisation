# Multilingual-KG-Verbalisation

This repository is for the paper, "Multilingual Verbalisation of Knowledge Graphs" (EMNLP 2025 Findings). We provide the following components:
- Training/Prompting codes for our three methods:
    - FTMT: Machine Translation models fine tuned on multilingual datasets of (Knowledge Graph, Text) pairs
    - NLG+MT: Machine Translating the English text produced by the SOTA KG-to-Text [Control Prefix Model](https://aclanthology.org/2022.gem-1.31.pdf) 
    - Few-Shot Prompting of LLMs
- Evaluation code and generated output texts

## Authors:
- Yifei Song (CNRS/Loria & Université de Lorraine)
- William Soto Martinez (CNRS/Loria & Université de Lorraine)
- Anna Nikiforovskaya (CNRS/Loria & Université de Lorraine)
- Claire Gardent (CNRS/Loria & Université de Lorraine)

## Citation
If you find this repo useful, please cite: 


```bibtex

@inproceedings{song-etal-2025-multilingual-verbalisation,
    title = "Multilingual Verbalisation of Knowledge Graphs",
    author = "Song, Yifei  and
      Martinez, William Soto  and
      Nikiforovskaya, Anna  and
      Chapple, Evan Parker Kelly  and
      Gardent, Claire",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2025",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-emnlp.60/",
    pages = "1111--1162",
    ISBN = "979-8-89176-335-7",
}
```
