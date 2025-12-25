# Modules

This directory contains the core processing modules for QA dataset generation.

## Structure

- **`construct/`**: QA pair construction from documents
- **`preprocess/`**: Preprocessing utilities (placeholder)

## Construct Module

The construct module implements the main QA generation pipeline.

### QAConstruct Class

Main class for generating QA pairs from documents.

#### Initialization

```python
from vietlegalqa.modules import QAConstruct
from stanza import Pipeline

parser = Pipeline(lang="vi", processors="tokenize, pos, ner, constituency")
pos = Pipeline(lang="vi", processors="tokenize, pos, lemma")

constructor = QAConstruct(
    stopwords=["các", "là", "của"],  # List of stopwords
    parser=parser,                    # Stanza parser pipeline
    pos=pos                           # Stanza POS pipeline
)
```

#### Usage

```python
from vietlegalqa import load_document_hf

# Load documents
doc = load_document_hf("vietlegalqa/tvpl_summary_kha")

# Generate QA pairs
qa_dataset = constructor(document=doc, id_prefix="tvpl")
```

### Answer Types

The framework supports multiple answer types:

- **NE (Named Entities)**: Person names, locations, organizations, etc.
- **NP (Noun Phrases)**: Noun phrases extracted from constituency parse trees
- **AP (Adjective Phrases)**: Adjective phrases
- **VP (Verb Phrases)**: Verb phrases
- **S (Clauses)**: Complete clauses

### Processing Pipeline

1. **Summary Processing**: Tokenizes and parses summaries using Stanza
2. **Key Extraction**: Extracts NE and POS-tagged phrases
3. **Clause Extraction**: Identifies meaningful clauses using:
   - Constituency parsing (S nodes with length > threshold)
   - Comma-based segmentation
4. **Question Generation**: Creates cloze questions by replacing answer spans with type placeholders
5. **Answer Localization**: Finds answer positions in context documents using:
   - Token matching (excluding stopwords)
   - Score-based context ranking

### Utility Functions

- **`get_summary_nlp()`**: Processes summary text with Stanza parser
- **`get_keys()`**: Extracts phrases of specific POS tags from parse tree
- **`extract_clauses()`**: Extracts clauses from parsed documents
- **`get_answer_start()`**: Finds answer position in context documents

## Configuration

### POS Tags and Replacements

```python
POS_TAGS = ["NUM", "NP", "AP", "VP", "S"]

POS_REPLACE = {
    "NUM": "NUMBER",
    "NP": "NOUNPHRASE",
    "AP": "ADVPHRASE",
    "VP": "VERBPHARSE",
    "S": "CLAUSE"
}
```

### Thresholds

- **`s_threshold`**: Minimum number of words in a clause (default: 3)
- **`comma_threshold`**: Minimum words before comma-based splitting (default: 5)

## Preprocess Module

Currently a placeholder for future preprocessing utilities.
