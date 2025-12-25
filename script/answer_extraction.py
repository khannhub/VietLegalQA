import argparse
from vietlegalqa import load_document_hf, QAConstruct
from stanza import Pipeline
from torch.cuda import is_available, device_count


FIELD = ["url", "title", "summary", "document"]
DOC_HF = "vietlegalqa/tvpl_summary_kha"
STOPWORDS_DIR = "./data/vietnamese-stopwords.txt"
PREFIX = "tvpl"


def check_args(args) -> tuple[bool, str]:
    if args.use_gpu is True:
        if not is_available():
            setattr(args, "use_gpu", False)

    if args.device >= device_count() or args.device < 0:
        setattr(args, "device", 0)

    return True


def main(args):
    doc = load_document_hf(path=args.doc, split="train", field=FIELD)

    with open(
        args.stopwords_dir,
        "r",
        encoding="utf-8",
    ) as stopwords_file:
        STOPWORDS = stopwords_file.read().splitlines()

    PARSER = Pipeline(
        lang=args.lang,
        processors="tokenize, pos, ner, constituency",
        use_gpu=args.use_gpu,
        device=args.device,
        verbose=args.verbose,
        allow_unknown_language=True,
        tokenize_pretokenized=True,
        tokenize_no_ssplit=True,
    )
    POS = Pipeline(
        lang=args.lang,
        processors="tokenize, pos, lemma",
        use_gpu=args.use_gpu,
        device=args.device,
        verbose=args.verbose,
        allow_unknown_language=True,
        tokenize_pretokenized=True,
        tokenize_no_ssplit=True,
    )

    constructor = QAConstruct(stopwords=STOPWORDS, parser=PARSER, pos=POS)
    qa = constructor(document=doc, id_prefix=args.id_prefix)
    output_path = args.output_file if args.output_file.endswith('.pkl') else f"{args.output_file}.pkl"
    qa.to_pickle(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--doc", default=DOC_HF, type=str, help="HuggingFace dataset path or identifier")
    parser.add_argument("--stopwords_dir", default=STOPWORDS_DIR, type=str, help="Path to stopwords file")
    parser.add_argument("--id_prefix", default=PREFIX, type=str, help="Prefix for QA pair IDs")
    parser.add_argument("--output_file", default=f"./data/{PREFIX}_construct.pkl", type=str, help="Output file path for generated QA dataset")
    parser.add_argument("--lang", default="vi", type=str, help="Language code for Stanza pipeline")
    parser.add_argument("--use_gpu", action="store_true", help="Use GPU for processing")
    parser.add_argument("--device", default=0, type=int, help="GPU device index")
    parser.add_argument("--verbose", default=0, type=int, help="Verbosity level for Stanza pipeline")
    args = parser.parse_args()

    if check_args(args):
        main(args)
