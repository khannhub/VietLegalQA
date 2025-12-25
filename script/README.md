# Scripts

Command-line scripts for dataset generation and processing.

## answer_extraction.py

Main script for generating QA datasets from documents.

### Usage

```bash
python script/answer_extraction.py [OPTIONS]
```

### Options

- **`--doc`** (default: `"vietlegalqa/tvpl_summary_kha"`): HuggingFace dataset path or identifier
- **`--stopwords_dir`** (default: `"./data/vietnamese-stopwords.txt"`): Path to stopwords file
- **`--id_prefix`** (default: `"tvpl"`): Prefix for QA pair IDs
- **`--output_file`** (default: `"./data/tvpl_construct.pkl"`): Output file path for generated QA dataset
- **`--lang`** (default: `"vi"`): Language code for Stanza pipeline
- **`--use_gpu`**: Flag to use GPU for processing (action flag, no value needed)
- **`--device`** (default: `0`): GPU device index
- **`--verbose`** (default: `0`): Verbosity level for Stanza pipeline (0-3)

### Examples

#### Basic Usage

```bash
python script/answer_extraction.py \
    --doc "vietlegalqa/tvpl_summary_kha" \
    --output_file "./data/my_dataset.pkl"
```

#### Using GPU

```bash
python script/answer_extraction.py \
    --use_gpu \
    --device 0 \
    --lang "vi"
```

#### Custom Configuration

```bash
python script/answer_extraction.py \
    --doc "my_dataset/hf_path" \
    --stopwords_dir "./custom_stopwords.txt" \
    --id_prefix "custom" \
    --output_file "./output/custom_qa.pkl" \
    --verbose 1
```

### Input Format

The script expects a HuggingFace dataset with the following fields:
- `id`: Article identifier
- `title`: Article title
- `summary`: List of summary sentences
- `document`: List of context paragraphs (or `context` field)

### Output

The script generates a pickle file containing a `QADataset` object with the following structure:

- Each QA pair includes:
  - `id`: Unique identifier (format: `{prefix}_{index}`)
  - `article`: Article identifier with context index
  - `question`: Generated cloze question
  - `answer`: Answer text
  - `start`: Starting position in context
  - `type`: Answer type (NE, NOUNPHRASE, etc.)
  - `is_impossible`: Boolean flag

### Requirements

- Stanza Vietnamese models must be downloaded
- GPU recommended for faster processing (optional)
- Stopwords file in UTF-8 encoding
