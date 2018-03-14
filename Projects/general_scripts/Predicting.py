import parser_module as prs
from datetime import datetime
import pickle
import SVM_predicting_module as prdc

################################################################################
### Loading the (best found) model
################################################################################
start_time = datetime.now()
print('Model Predicting Program is running...')
loaded_model=prdc.Loading()

################################################################################
### Predicting topology from another fasta file
################################################################################
# WRITE HERE THE FASTA FILE FOR PREDICTING IF YOU WANT TO USE ANOTHER ONE:
filetopredict='Filtered_BetaBarrelDataset_fasta.txt'
dictionary_prediction,prediction=prdc.PredictionParser(filetopredict,loaded_model)

################################################################################
### Saving the prediction with desired name
################################################################################
name=input('Please specify the file name in which the prediction will be saved: ')
prdc.Saveprediction(dictionary_prediction,prediction,name)
print('\nYour prediction has been saved in a txt with the name: '+name+'_prediction.txt')

end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
