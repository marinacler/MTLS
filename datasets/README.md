datsets README

Here you have the main datasets for running the Predictor:
	- membrane-beta_2state.3line is my given dataset (beta barrel, 2 states)
	- membrane-beta_2state.3line_fasta is my given dataset in FASTA format
	- example is a smaller dataset obtained from membrane-beta_2state.3line
	- myexample is a smaller dataset obtained from membrane-beta_2state.3line
	- examplefortesting is an example file to do a prediction
	- examplefortesting_PSSM is an example file to do a prediction with a trained PSSM predictor. It includes 3 proteins from the 50_extra_proteins
	- Filered_BetaBarrelDataset_fasta.txt is a fasta file containing 50 proteins with known topology (see 50_extra_proteins for more details) used for predicting  with a trained predictor based on aminoacid residues

Also, the following files:
	- fasta_psi contains all the data for running the PSIBLAST (individual fasta files, as the alignment and pssm files obtained as output when running it)
	- 50_extra_proteins contains the new dataset of 50 extra proteins properly labeled
