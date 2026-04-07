# Gene Expression Analysis

An exercise using python that looks at using Pandas series and dataframe objects using gene expression data across three tissue samples.


### Setup

1. Clone the repository:
```bash
git clone https://github.com/edecocke-uncc/expression.git
```

2. Go into the project folder:
```bash
cd expression
```

3. Create the environment:
```bash
conda env create -f environment.yml
```

4. Activate the environment:
```bash
conda activate expression
```

## Run
```bash
python3 expression_analysis.py
```

## What it does

- Loads expression data for 5 genes (BRCA1, TP53, EGFR, MYC, KRAS) across Heart, Liver, and Brain samples
- Demonstrates the difference between a series and dataframes
- Calculates mean expression per gene, determines the most highly expressed gene in the brain, and computes Brain vs Liver fold-change
- Exports results to expression.csv

## Output

A expression.csv file is written to the current directory after each run.
