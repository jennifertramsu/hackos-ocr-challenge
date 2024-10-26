import shutil
import glob
from genomic_benchmarks.loc2seq import download_dataset
from pathlib import Path

# Paths
PATHS = [Path('data'), Path('models'), Path('results'), Path('src')]
for path in PATHS:
    path.mkdir(exist_ok=True)

# Subpaths
SUB_PATHS = [PATHS[0] / 'raw', PATHS[0] / 'processed']
for sub_path in SUB_PATHS:
    sub_path.mkdir(exist_ok=True)

# Downloading dataset human_ocr_ensembl
if not (SUB_PATHS[0] / 'human_ocr_ensembl').exists():
    download_dataset('human_ocr_ensembl', version = 0, dest_path = SUB_PATHS[0])

# Move files to the right place
for file in glob.glob(str(SUB_PATHS[0] / 'human_ocr_ensembl' / '*')):
    shutil.move(file, str(SUB_PATHS[0] / Path(file).name))
    
# Check if human_ocr_ensembl is empty directory
if not list((SUB_PATHS[0] / 'human_ocr_ensembl').iterdir()):
    shutil.rmtree(SUB_PATHS[0] / 'human_ocr_ensembl')