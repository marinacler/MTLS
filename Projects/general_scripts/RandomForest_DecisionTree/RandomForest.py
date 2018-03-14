import parser_module as prs
import SVM_training_module as train
import sklearn
from datetime import datetime
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
#Tools for visualizing single decision tree
#from sklearn.tree import export_graphviz
#import pydot

################################################################################
### Get input for training the Random Forest (RF)
################################################################################
start_time = datetime.now()
print('Random Forest: Model Training Program is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../../datasets/membrane-beta_2state.3line.txt')
for slidwindow in range(3,36,2):
    traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)
    
################################################################################
### Evaluating the RF
################################################################################   
    for n_estimators in range(100,400,50):
        for min_samples_split in range(2,11):
            forest = RandomForestClassifier(n_estimators = n_estimators, min_samples_split = min_samples_split)
            print('Random Forest: Sliding window: ', slidwindow, '\nN_estimators: ', n_estimators, '\nMin_samples_split: ', min_samples_split )
            forest2=train.crossvalidation(traininginput, trainingoutput, forest, slidwindow)
            print('')
            print('')

################################################################################
### Saving the trained model
################################################################################
            filename=open('../trained_models/Model' + str(slidwindow) +'_Estimators'+str(n_estimators)+'_MinSamples'+str(min_samples_split)+'_RandomForest.pkl','wb')
            pickle.dump(forest2, filename)

end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
