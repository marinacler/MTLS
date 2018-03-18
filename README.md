# MTLS
Repository for Project in molecular Life science 

Hello!

Go to projects -> general_scripts.
Several trained models have been produced and can be found in the file general_scripts.

Once there (general_scripts), run Predicting.py. It will load a trained model with the best parameters found so far (C=0,9, kernel=linear, sliding window=35), but I am still working on the optimization. (See in Report_data some of the values/accuracies that I  have been obtaining).

If you want to train again the model, you can do it directly from Training.py specifying the values that you might want. 
Right now this file is a little bit messy, because I am changing many parameters for the optimization.

Predict.py is predicting the topology on a fasta file that I  have prepared (containing 3 proteins).

Beta barrel (4 state) individual assignment

clean_CV includes functions for:

parser
window list
binary list of aa
numerical list of topology
topology back to ch
save into .npz file
SVM
cross validation
cv

tested on a range of window sizes
window size 17
trained_model

saves trained model
final_predictor

predicts topology using model
output looks like this for each protein:
*ID
*amino acid sequence
*predicted topology
Trained my model with all the proteins I was given (42 proteins) and window size 17 with a linear kernel. Used "testingdata_pred.txt" as my test file for predictor.

For PSSM portion:

all_pssm includes functions to:

parse and prepare input for predictor
optimized version (PSSM_model.sav)
PSSM_predictor

predicts topology on 50 proteins using model
"PSSM_prediction.txt" is the output for the predicted topology of 50 proteins
"PSSM_prediction_scores.txt" is all the data of my scores
Trained my model with the PSSMs found in folder "PSSM" and tested on the PSSMs found in folder "PSSM_50test", both located in "PSI-BLAST".
