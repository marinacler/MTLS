import parser_module as prs
import SVM_training_module as train
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from datetime import datetime
import pickle

################################################################################
### Get input for training the SVM
################################################################################
start_time = datetime.now()
print('Model Training Program (with evolutionary information) is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/membrane-beta_2state.3line.txt')
slidwindow=35
c=1
print('Slid window: ', slidwindow)
print('C value: ', c)
traininginput, trainingoutput = prs.input_for_training_pssm(parsed_dictionary_training,slidwindow)

################################################################################
### Training the SVM with 5 cross-validation datasets
################################################################################
clf0 = svm.SVC(kernel='linear', C=c, cache_size=4000)
clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)

################################################################################
### Save the trained model
################################################################################
pickle.dump(clf, open('./trained_models/last_model_' + str(slidwindow) + '_C'+str(c)+'_PSSM.pkl', 'wb'))

end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
print ('Training done! Bye!')

parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/membrane-beta_2state.3line.txt')
slidwindow=35
c=0.8
print('Slid window: ', slidwindow)
print('C value: ', c)
traininginput, trainingoutput = prs.input_for_training_pssm(parsed_dictionary_training,slidwindow)

################################################################################
### Training the SVM with 5 cross-validation datasets
################################################################################
clf0 = svm.SVC(kernel='linear', C=c, cache_size=4000)
clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)

################################################################################
### Save the trained model
################################################################################
pickle.dump(clf, open('./trained_models/last_model_' + str(slidwindow) + '_C'+str(c)+'_PSSM.pkl', 'wb'))

parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/membrane-beta_2state.3line.txt')
slidwindow=35
c=0.6
print('Slid window: ', slidwindow)
print('C value: ', c)
traininginput, trainingoutput = prs.input_for_training_pssm(parsed_dictionary_training,slidwindow)

################################################################################
### Training the SVM with 5 cross-validation datasets
################################################################################
clf0 = svm.SVC(kernel='linear', C=c, cache_size=4000)
clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)

################################################################################
### Save the trained model
################################################################################
pickle.dump(clf, open('./trained_models/last_model_' + str(slidwindow) + '_C'+str(c)+'_PSSM.pkl', 'wb'))
