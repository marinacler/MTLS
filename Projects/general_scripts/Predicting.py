import parser_module as prs
from datetime import datetime
import pickle
import SVM_predicting_module as prdc

################################################################################
### LOADING THE (BEST FOUND) MODEL 
################################################################################
start_time = datetime.now()
print('Model Predicting Program is running...')
loaded_model=prdc.Loading()

################################################################################
### PREDICT TOPOLOGY FROM ANOTHER FASTA FILE
################################################################################
# WRITE HERE THE FASTA FILE FOR PREDICTING IF YOU WANT TO USE ANOTHER ONE:
filetopredict='examplefortesting.txt' # ('membrane-beta_3state.3line.FASTA.txt')
dictionary_prediction,prediction=prdc.PredictionParser(filetopredict,loaded_model)

################################################################################
### SAVE PREDICTION WITH DESIRED NAME
################################################################################
name=input('Please specify the file name in which the prediction will be saved: ')
prdc.Saveprediction(dictionary_prediction,prediction,name)
print('\nYour prediction has been saved in a txt with the name: '+name+'_prediction.txt')

end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
