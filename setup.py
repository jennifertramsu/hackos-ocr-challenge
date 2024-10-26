from genomic_benchmarks.loc2seq import download_dataset
from pathlib import Path

DATA_PATH = Path('data')
DATA_PATH.mkdir(exist_ok=True)

# Downloading dataset human_ocr_ensembl
download_dataset('human_ocr_ensembl', version = 0, dest_path = DATA_PATH / 'human_ocr_ensembl')