# VietLegalQA

VietLegalQA - Unsupervised Vietnamese Legal Question Answering by Cloze Translation

## Overview

VietLegalQA is an end-to-end unsupervised framework designed to generate high-quality training datasets for Extractive Question Answering (QA) tasks, specifically targeting the Vietnamese language and legal domain. The framework transforms source documents into QA pairs using Named Entity Recognition (NER), Part-of-Speech (POS) tagging, and cloze translation techniques.

## Features

- **Unsupervised QA Generation**: Generates QA pairs from raw documents without manual annotation
- **Multiple Answer Types**: Supports various answer types including Named Entities (NE), Noun Phrases (NP), Adjective Phrases (AP), Verb Phrases (VP), and Clauses (S)
- **Vietnamese NLP Integration**: Uses Stanza and underthesea for Vietnamese language processing
- **Flexible Data Loading**: Supports loading documents from HuggingFace datasets or local JSON files
- **Export Capabilities**: Export generated QA datasets in JSON, pickle, or push to HuggingFace Hub

## Installation

1. Clone the repository:
```bash
git clone https://github.com/khannhub/VietLegalQA.git
cd VietLegalQA
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download Vietnamese language models for Stanza:
```python
import stanza
stanza.download('vi')
```

## Quick Start

### Generate QA Dataset from HuggingFace Dataset

```python
from vietlegalqa import load_document_hf, QAConstruct
from stanza import Pipeline

# Load documents
doc = load_document_hf(
    path="vietlegalqa/tvpl_summary_kha",
    split="train",
    field=["id", "title", "summary", "document"]
)

# Load stopwords
with open("./data/vietnamese-stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = f.read().splitlines()

# Initialize Stanza pipelines
parser = Pipeline(
    lang="vi",
    processors="tokenize, pos, ner, constituency",
    use_gpu=True
)

pos = Pipeline(
    lang="vi",
    processors="tokenize, pos, lemma",
    use_gpu=True
)

# Generate QA pairs
constructor = QAConstruct(stopwords=stopwords, parser=parser, pos=pos)
qa_dataset = constructor(document=doc, id_prefix="tvpl")

# Export dataset
qa_dataset.to_json("./data/output.json")
qa_dataset.to_pickle("./data/output.pkl")
```

### Using the Command-Line Script

```bash
python script/answer_extraction.py \
    --doc "vietlegalqa/tvpl_summary_kha" \
    --stopwords_dir "./data/vietnamese-stopwords.txt" \
    --id_prefix "tvpl" \
    --output_file "./data/tvpl_construct.pkl" \
    --lang "vi" \
    --use_gpu \
    --device 0 \
    --verbose 0
```

## Project Structure

```
VietLegalQA/
├── vietlegalqa/          # Main package
│   ├── data/            # Data structures and loading utilities
│   ├── modules/         # Core processing modules
│   │   ├── construct/   # QA pair construction
│   │   └── preprocess/  # Preprocessing utilities
│   └── models/          # Model definitions (placeholder)
├── script/              # Command-line scripts
├── data/                # Data files and outputs
├── notebooks/           # Jupyter notebooks for experimentation
└── requirements.txt     # Python dependencies
```

## Documentation

- [Data Module](vietlegalqa/data/README.md) - Data structures and loading utilities
- [Modules](vietlegalqa/modules/README.md) - Processing modules documentation
- [Scripts](script/README.md) - Command-line scripts usage

## Methodology

The framework follows these steps:

1. **Document Loading**: Loads source documents (articles with titles, summaries, and contexts)
2. **Entity Extraction**: Extracts Named Entities (NE) and various POS-tagged phrases (NP, AP, VP, S)
3. **Clause Extraction**: Identifies meaningful clauses from summaries
4. **Question Generation**: Converts clauses to cloze-style questions by replacing answer spans with placeholders
5. **Answer Localization**: Finds answer positions in the original context documents
6. **Dataset Construction**: Assembles QA pairs into a structured dataset

## Citation

If you use this work, please cite:

```bibtex
@inproceedings{vietlegalqa2023,
  title={VietLegalQA: Unsupervised Legal Question Answering for Vietnamese Using Cloze Translation Approach},
  author={Nguyen Ngoc, Kha and Nguyen Trong, Phuc and Luong Nguyen Minh, Chanh and Nguyen Hoang Gia, Khang and Nguyen Quoc, Trung and Truong Hoang, Vinh},
  booktitle={2023 IEEE 15th International Conference on Computational Intelligence and Communication Networks (CICN)},
  year={2023},
  doi={10.1109/CICN.2023.10402152}
}
```

## License

This work is copyrighted by IEEE. 

According to IEEE copyright policies, authors retain the right to post the accepted version on their personal servers or institutional repositories, provided that:
- The posted version includes a prominently displayed IEEE copyright notice
- When published, a full citation to the original IEEE publication is included, including a link to the article abstract in IEEE Xplore

For the full published version, please refer to: [IEEE Xplore](https://ieeexplore.ieee.org/document/10402152)

For questions about IEEE copyright policy, please contact: IEEE Intellectual Property Rights Office, copyrights@ieee.org

## Authors

- Kha Nguyen Ngoc
- Phuc Nguyen Trong
- Chanh Luong Nguyen Minh
- Khang Nguyen Hoang Gia
- Trung Nguyen Quoc
- Vinh Truong Hoang

## References

- Paper: [IEEE Xplore](https://ieeexplore.ieee.org/document/10402152)
- SQuAD Dataset: [Rajpurkar et al., 2016](https://arxiv.org/abs/1606.05250)
- UIT-ViQuAD: [Nguyen et al., 2020](https://aclanthology.org/2020.coling-main.233/)
