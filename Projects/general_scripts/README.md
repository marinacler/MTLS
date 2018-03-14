General_scripts README

Here you have the main scripts for running the Predictor.
	- parser_FASTA_psiblast converts the dataset into individual fasta files for each protein sequence
	- parser_module contains all the parser functions needed for the program to work
	- Predicting is the actual predictor
	- SVM_predicting_module contains all the functions needed for Predicting.py to work
	- SVM_training_module contains all the functions needed for Training(_PSSM).py to work
	- Training is used for training the predictor from sequence data
	- Training_PSSM is used for training the predictor from PSSMs (obtained from PSIBLAST with Uniref90)


Also, the following files contain:
	- RandomForest_DecisionTree contains training files using Random Forest and Decision Trees
	- trained_models contains all the models generated (different kernels, c values, gamma values, sliding windows...). 
	  Only the best performing model is used in the predictor (Predicting)


Finally, the remaining file:
	- testing_prediction.txt is an example of the output given by my predictor
