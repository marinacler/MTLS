import parser_module as prs
import SVM_training_module as train
import sklearn
from datetime import datetime
import pickle
from sklearn.tree import DecisionTreeClassifier

################################################################################
### Get input for doing the Decision Tree Classifier (DTC)
################################################################################
start_time = datetime.now()
print('Decision Tree: Model Training Program is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../../datasets/membrane-beta_2state.3line.txt')
for slidwindow in range(3,36,2):
    traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)
    
################################################################################
### Evaluating the DTC
################################################################################
    for min_samples_split in range(2,11):
        tree =  DecisionTreeClassifier(min_samples_split = min_samples_split)
        print('Decision Tree: Sliding window: ', slidwindow, '\nMin_samples_split: ', min_samples_split )
        tree2=train.crossvalidation(traininginput, trainingoutput, tree, slidwindow)
        print('')
        print('')
        
################################################################################
### Saving the trained model
################################################################################
        filename=open('../trained_models/Model' + str(slidwindow) +'_MinSamples'+str(min_samples_split)+'_DecisionTree.pkl','wb')
        pickle.dump(tree2, filename)
        
end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
