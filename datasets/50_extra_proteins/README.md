datasets 50_extra proteins README

Here you have all the files that have been used for obtaining a new dataset containing 50 extra TMBs proteins

	- top_bp.txt is the dataset of TMBs downloaded from TOPDB, withouth any modification
	- New_dataset.py converts top_bp.txt into BetaBarrelDataset.txt and BetaBarrelDataset_fasta.txt
	- BetaBarrelDataset.txt is the top_bp.txt dataset translated to the topologies that my predictor will predict (either B or g).
	- BetaBarrelDataset_fasta.txt is the fasta file of BetaBarrelDataset.txt (without topologies)
	- Filtered_BetaBarrelDataset.txt and Filtered_BetaBarrelDataset_fasta.txt are datasets coming from the BetaBarrelDataset.txt and BetaBarrelDataset_fasta.txt files, but with a reduced number of proteins (from 123 to 50 proteins, filtered using https://web.expasy.org/decrease_redundancy/, with a 30% of max similarity)
