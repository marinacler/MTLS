# MTLS
Repository for Project in molecular Life science 

Hello!

Go to projects -> general_scripts.

Several trained models have been produced and can be found in the file general_scripts.

Once there, run Predict.py. It would load a trained model with the best parameters found so far (C=0,9, kernel=linear, sliding window=35), but I am still working on the optimization.

If you want to train again the model, you can do it directly from Training.py specifying the values that you might want. 
Right now this file is a little bit messy, because I am changing many parameters for the optimization.

It is predicting the topology on a fasta file that I  have prepared (it contains 3 proteins).


