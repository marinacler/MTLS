# MTLS Master Program - Course: Project in molecular Life science
## Repository for: Beta barrel (2 state) predictor

### Project Points
- [x] Extract the feature from your dataset
- [x] Create cross-validated sets
- [x] Train a SVM using single sequence information, using sklearn
- [x] Check different window sizes for the inputs
- [x] Add evolutionary information by running psi-blast and extracting the information
- [x] Train a SVM using multiple sequence information
- [x] Optimize the performance of the SVM
- [x] Analyze the results and compare it to previous work
- [x] Use random forests and a simple decision tree and compare the performance with the SVM performance.
- [x] Extract the data from 50 other proteins and test the performance
- [x] Review the state of art for your predictor
- [x] Write a report

### Repository structure
 - **Diary:** Contains the final version of my diary (PDF format)
 - **Paper presentation:** Contains all files used for the paper presentation (papers, PowerPoint presentation, relevant information...)
 - **Projects:** Contains all bash and python scripts used in this project
 - **Report_data:** Contains many documents with metrics (raw) data from the different models testes (accuracy, F1-score, R2 score, conufsion matrix...)
 - **datasets:** Contains the files needed to run the program: example files for testing, the training dataset, derived smaller datasets, new dataset of 50 proteins, PSSMs profiles from PSI-BLAST run, etc.

### Doing a prediction
1. Go to Projects -> general_scripts.
2. Here you can run two versions of the predictor:
- Predicting.py is a 2-state beta barrel predictor trained directly on aminoacid residues. You can run it directly. This script loads an already-trained model that gave the best results in comparison with the other models that I generated. It makes use of 35 sliding windows, linear kerel and C parameter equal to 1. 
  - Input format: FASTA file.
  - Output format:
  
*ID*

*Amino acid sequence*

*Predicted topology*

- Predicting_PSSM.py is a 2-state beta barrel predictor with evolutionary information added (extracted from the information given by a PSI-BLAST run using Uniref90).The SVM here was trained using multiple sequence information. You can run it directly, as the example for doing the prediction fullfills the requirements for the model to work.
  - Input format: FASTA file. In addition, a PSI-BLAST run should be done previously for every single protein contained in the input FASTA file. Each output PSSM needs to be placed in datasets -> fasta_psi -> pssm and named as follows: proteinID.fasta.pssm, being the proteinID the same exact name as the one in the FASTa file. 
  - Output format:
  
*ID*

*Amino acid sequence*

*Predicted topology*

3. After doing the prediction, the program will ask you to write down the name of the output file. The output will be then saved in the same folder you are working, as a txt and named as: ChosenName_prediction.txt

### Modification of training parameters
In Projects -> general_scripts you can find the scripts used for training the predictor (Training.py, Training_PSSM.py, SVM_training_module.py). Optimization of different parameters has been done (kernel types, sliding windows, gamma values, cost values...) and the best performing models, along with two additional examples using Random Forest, have been placed in Projects -> general_scripts -> trained_models. Hundreds of different combinations have been carefully tested and selected but, however, if you want to train again the model, you can do it directly from these scripts (Training.py/Training_PSSM.py) specifying the values that you might want. 
