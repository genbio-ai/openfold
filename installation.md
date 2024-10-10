# Installation

## CSCC

```bash
eval "$(/home/nicolas.brosse/miniforge3/bin/conda shell.bash hook)"
conda create --name openfold python=3.10 -y
conda activate openfold
pip install -r requirements.txt
git clone https://github.com/NVIDIA/cutlass --depth 1
conda env config vars set CUTLASS_PATH=$PWD/cutlass
python -m pip wheel . -r requirements.txt -w wheel/
```