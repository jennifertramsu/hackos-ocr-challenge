from genomic_benchmarks.loc2seq import download_dataset
from pathlib import Path

PATHS = [Path('data'), Path('models'), Path('results')]
for path in PATHS:
    path.mkdir(exist_ok=True)

# Downloading dataset human_ocr_ensembl
if not (PATHS[0] / 'human_ocr_ensembl').exists():
    download_dataset('human_ocr_ensembl', version = 0, dest_path = path[0] / 'human_ocr_ensembl')