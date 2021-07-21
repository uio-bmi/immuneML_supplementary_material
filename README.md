# immuneML supplementary material
This repository contains supplementary material for creating figures as they appear in the immuneML manuscript (https://www.biorxiv.org/content/10.1101/2021.03.08.433891v3).

Content:

- figure 2 (Use cases demonstrating ML model training, benchmarking and platform extension):

    - 2B: raw data: performance comparison of the method proposed by Emerson et al. 2017 across dataset sizes
    - 2C: raw data: CMV-associated TCRB sequences across datasets
    - 2E: raw data: performance comparison of newly added ML method (CNN) with logistic regression and TCRdist-based classifier for predicting paired chain receptor specificity for Influenza A (epitope GILGFVFTL)
    - 2F: raw data: discovered motifs by logistic regression, CNN, TCRdist and GLIPH2
    - 2H: raw data: performance across simulated datasets with immune events of increasing complexity
    - 2I: raw data: assessment of motifs recovered by ML models

- supplementary figure 4 (Reproducing the CMV status prediction study by Emerson et al. 2017):
    
    - 4A: raw data used to plot the Venn diagram
    - 4B: code and data for plotting the overlap of CMV-associated sequences in cross-validation splits
    - 4C: beta distribution parameters for CMV positive (labeled 1) and CMV negative class (labeled 0) in a YAML file used to plot the distribution
    - 4D: code and data for plotting the area under the curve over different p-value thresholds for training and test datasets
    
- supplementary figure 5 (Extending immuneML with a new ML method):
    
    - 5C: area under the ROC curve on CMV-specific dataset (epitope KLGGALQAK) and EBV-specific dataset (epitope AVFDRKSDAK) comparing the newly added ML method with logistic regression and TCRdist-based classification
    
- supplementary figure 6 (The benchmarking use case model coefficients and motif recovery, where the repertoire data is represented by 3-mer amino acid frequencies):

    - 6A, 6B, 6C, and 6D: raw data as provided by immuneML as a part of the corresponding report output.

All plots with code provided as a part of this repository can now be obtained directly from immuneML through corresponding reports.

## References

Emerson, R. O. et al. Immunosequencing identifies signatures of cytomegalovirus exposure history and HLA-mediated effects on the T cell repertoire. Nat. Genet. 49, 659–665 (2017). doi: 10.1038/ng.3822

TCRdist:

Dash, P. et al. Quantifiable predictive features define epitope-specific T cell receptor repertoires. Nature 547, 89–93 (2017). doi: 10.1038/nature22383

Mayer-Blackwell, K. et al. TCR meta-clonotypes for biomarker discovery with tcrdist3: quantification of public, HLA-restricted TCR biomarkers of SARS-CoV-2 infection. bioRxiv 2020.12.24.424260 (2020) doi:10.1101/2020.12.24.424260.

GLIPH:

Glanville, J. et al. Identifying specificity groups in the T cell receptor repertoire. Nature 547, 94–98 (2017). doi: 10.1038/nature22976

Huang, H., Wang, C., Rubelt, F., Scriba, T. J. & Davis, M. M. Analyzing the Mycobacterium tuberculosis immune response by T-cell receptor clustering with GLIPH2 and genome-wide antigen screening. Nat. Biotechnol. 1–9 (2020) doi:10.1038/s41587-020-0505-4.