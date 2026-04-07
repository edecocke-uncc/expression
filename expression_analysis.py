#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Erin Nicole Decocker
# edecocke@charlotte.edu
# ID: 801442694

"""
expression_analysis.py

A dramatic bioinformatics adventure in which five brave genes
battle it out across three tissue samples to claim the throne
of Highest Expression.
"""

import pandas as pd

class TheGeneThrone:
    """
    Holds gene expression data across tissue samples and performs
    analyses.

    Each column in the underlying DataFrame is a Pandas Series —
    one-dimensional labeled arrays that together form the two-dimensional
    DataFrame table.
    """

    def __init__(self, data: dict, genes: list):
        """
        Initialises with raw expression data.

        Parameters
        ----------
        data  : dict  – tissue names → list of expression values
        genes : list  – gene names used as the DataFrame index
        """
        self.df = pd.DataFrame(data, index=genes)

    def show_off_a_series(self, tissue: str) -> pd.Series:
        """
        Extract a single tissue column and prove that yes, each
        DataFrame column really is just a humble Pandas Series.

        Parameters
        ----------
        tissue : str – name of the tissue column to extract

        Returns
        -------
        pd.Series
        """
        series = self.df[tissue]
        print(f"\n{'-'*60}")
        print(f" A Series example: {tissue} expression")
        print(f"{'-'*60}")
        print(series)
        print(f"\nType: {type(series)}")
        print(f"dtype: {series.dtype}")
        return series

    def show_off_the_dataframe(self) -> None:
        """Print the full two-dimensional DataFrame in all its glory."""
        print(f"\n{'-'*60}")
        print("Full Dataframe")
        print(f"{'-'*60}")
        print(self.df)
        print(f"\nShape : {self.df.shape}  (rows × columns)")
        print(f"Type  : {type(self.df)}")


    def crown_the_mean(self) -> None:
        """
        Calculate the mean expression per gene across all tissues
        and add it as a new 'Mean' column.
        """
        # axis=1 means we average across columns (tissues) for each gene row
        self.df['Mean'] = self.df[['Heart', 'Liver', 'Brain']].mean(axis=1).round(2)
        print(f"\n{'-'*60}")
        print("Mean expression per gene (across all tissue types)")
        print(f"{'-'*60}")
        print(self.df)

    def declare_brain_champion(self) -> str:
        """
        Find and announce the most highly expressed gene in the Brain.

        Returns
        -------
        str – name of the winning gene
        """
        champion = self.df['Brain'].idxmax()
        print(f"  Most expressed gene in the brain: {champion}")
        print(f"  Expression level: {self.df.loc[champion, 'Brain']}")
        return champion

    def calculate_the_dramatic_fold_change(self) -> None:
        """
        Calculate the fold-change between Brain and Liver expression
        for each gene and add it as a 'Fold_Change_Brain_vs_Liver' column.

        Fold-change = Brain / Liver
        """
        self.df['FoldChange_Brain_vs_Liver'] = (
            self.df['Brain'] / self.df['Liver']
        ).round(3)

        print(f"\n{'-'*60}")
        print(" Fold Change (Brain vs Liver)")
        print(f"{'-'*60}")
        print(self.df)

    def export_to_csv(self, filename: str = "gene_expression.csv") -> None:
        """
        Export the completed DataFrame to a CSV file for further analysis
        (e.g., clustering, plotting, impressing your PI :)) )

        Parameters
        ----------
        filename : str – output file path (default: gene_expression.csv)
        """
        self.df.to_csv(filename)
        print(f"\n Results saved to '{filename}'")

def deliver_the_wisdom_of_the_ancients() -> None:
    """
    Print answers to the three reflection questions.
    No genomics deity was harmed in the making of this function.
    """
    reflections = {
        "1. What happens if one tissue has missing data for some genes?": (
            "If a tissue has missing data for some genes, you can handle it during "
            "the filtering step — for example, using a minimum-expression filter that "
            "keeps only genes expressed above a threshold in a minimum number of samples. "
            "The course shows df.isnull().sum() to check for missing values, "
            "and df.dropna() or df.fillna(0) to remove or replace them."
        ),
        "2. How could you normalize expression values across samples?": (
            "you could use: "
            "CPM = (raw_count / total_counts_in_sample) * 1,000,000. "
            "Which corrects for differences in sequencing depth across samples. "
            "In pandas: cpm = df.divide(df.sum(axis=0), axis='columns') * 1e6. "
            "For comparing different genes to each other, RPKM or TPM also "
            "correct for gene length."
        ),
        "3. How could you use df.to_csv() to export results?": (
            "Just call df.to_csv('gene_expression.csv').\n"
            "This writes the dataframe with the index to the CSV file "
        ),
    }

    print(f"\n{'-'*60}")
    print("Q&A")
    print(f"{'-'*60}")
    for question, answer in reflections.items():
        print(f"\n {question}")
        print(f"   {answer}")


if __name__ == "__main__":

    expression_data = {
        'Heart': [5.2, 3.3, 7.1, 4.5, 2.8],
        'Liver': [4.8, 2.9, 6.5, 4.1, 2.5],
        'Brain': [6.1, 3.7, 8.2, 5.3, 3.0],
    }
    gene_names = ['BRCA1', 'TP53', 'EGFR', 'MYC', 'KRAS']
    throne = TheGeneThrone(data=expression_data, genes=gene_names)
    throne.show_off_a_series(tissue='Brain')
    throne.show_off_the_dataframe()
    throne.crown_the_mean()
    throne.declare_brain_champion()
    throne.calculate_the_dramatic_fold_change()
    throne.export_to_csv("gene_expression.csv")
    deliver_the_wisdom_of_the_ancients()
