General_scripts README

Here you have the main scripts for running the Predictor.

	- parser_FASTA_psiblast converts the dataset into individual fasta files for each protein sequence

	- parser_module contains all the parser functions needed for the program to work

	- Predicting is the actual predictor

	- Predicting_PSSM is the actual predictor using PSSM. For using it, the fasta file that is used as input for predicting needs to be runned with PSIBLAST and the obtained PSSM profile placed in datasets-> psi_blast -> pssm with the ID name used for naming it. 

	- SVM_predicting_module contains all the functions needed for Predicting(_PSSM).py to work

	- SVM_training_module contains all the functions needed for Training(_PSSM).py to work

	- Test_performance tests the performance of the predictions done (as I know the real topologies)

	- Training is used for training the predictor from sequence data

	- Training_PSSM is used for training the predictor from PSSMs (obtained from PSIBLAST with Uniref90)


Also, the following files contain:

	- RandomForest_DecisionTree contains training files using Random Forest and Decision Trees

	- trained_models contains some of the models generated (different kernels, c values, gamma values, sliding windows...). I could  not upload all of them because of the size, but more thant 500 models were generated and analyzed throughout the course of the project.
	  Only the best performing model is used in the predictor (Predicting)


Finally, the remaining files:

	- testing_prediction.txt is an example of the output given by my predictor

	- 3Protein_PSSM_prediction.txt is the prediction given from my PSSM-trained model from a fasta file of 3 proteins (topologies are known)

	- 50Prot_dataset_prediction.txt is the prediction given from my residue-trained model from a fasta file of 50 proteins (topologies are known)
