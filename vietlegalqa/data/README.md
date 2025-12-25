# Data Module

This module provides data structures and utilities for loading and managing documents and QA datasets.

## Components

### Classes

- **`Article`**: Represents a single article with id, title, summary, and context
- **`Document`**: Collection of Articles, implements the Dataset interface
- **`QAPair`**: Represents a single question-answer pair with metadata
- **`QADataset`**: Collection of QAPairs, implements the Dataset interface

### Loading Functions

- **`load_document()`**: Load documents from local JSON or pickle files
- **`load_document_hf()`**: Load documents from HuggingFace datasets
- **`load_qa()`**: Load QA datasets from local JSON or pickle files
- **`load_qa_hf()`**: Load QA datasets from HuggingFace datasets

## Usage Examples

### Loading Documents

```python
from vietlegalqa import load_document, load_document_hf

# From local JSON file
doc = load_document("data/documents.json", type="json")

# From HuggingFace
doc = load_document_hf("vietlegalqa/tvpl_summary_kha", split="train")
```

### Working with Documents

```python
# Access articles
article = doc["article_id"]
article = doc[0]  # By index

# Iterate over articles
for article in doc:
    print(article.title)
    print(article.summary)
    print(article.context)

# Convert to different formats
doc_list = doc.to_list()  # List of dictionaries
doc_json = doc.to_json("output.json")  # Export to JSON
hf_dataset = doc.to_dataset()  # Convert to HuggingFace Dataset
```

### Working with QA Datasets

```python
from vietlegalqa import load_qa, QAPair

# Load QA dataset
qa = load_qa("data/qa_pairs.json", type="json")

# Access QA pairs
pair = qa["qa_id"]
pair = qa[0]  # By index

# Create new QA pair
new_pair = QAPair(
    id="qa_001",
    article="article_id",
    question="What is the question?",
    answer="The answer",
    start=42,
    type="NOUNPHRASE",
    is_impossible=False
)

qa.append(new_pair)

# Export dataset
qa.to_json("output.json")
qa.to_pickle("output.pkl")
```

## Data Format

### Document Format

```json
{
  "id": "article_001",
  "title": "Article Title",
  "summary": ["Summary sentence 1", "Summary sentence 2"],
  "context": ["Context paragraph 1", "Context paragraph 2"]
}
```

### QA Pair Format

```json
{
  "id": "qa_001",
  "article": "article_001__0",
  "question": "What is the NOUNPHRASE?",
  "answer": "legal document",
  "start": 42,
  "type": "NOUNPHRASE",
  "is_impossible": false
}
```

## Field Constants

- **`DOC_FIELD`**: `["id", "title", "summary", "context"]`
- **`QA_FIELD`**: `["id", "article", "question", "answer", "start", "type", "is_impossible"]`

## Utilities

- **`get_extension()`**: Helper function to ensure file extensions
- **`Entry`**: Base class for Article and QAPair
- **`Dataset`**: Base class for Document and QADataset
