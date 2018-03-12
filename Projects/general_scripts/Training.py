import parser_module as prs
import SVM_training_module as train
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from datetime import datetime
import pickle
#from sklearn.externals import joblib

################################################################################
### GET INPUT FOR TRAINING THE SVM
################################################################################
start_time = datetime.now()
print('Model Training Program is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/membrane-beta_2state.3line.txt') #('../../datasets/example.txt')
# ('../../datasets/membrane-beta_2state.3line.txt')
print('FULL DATASET')


#listcvalues=[0.5,1,10,100]
for m in range(9,50,2):#listcvalues:
	c=1
	print('SLIDWINDOW VARIABLE EQUAL TO: ',m)
	slidwindow=m
#for slidwindow in range(5,50,2):
	traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)
	
	if m>1: #value in range(-10,0):
	    #gammavalue=10**value
	    #print('GAMMA VARIABLE EQUAL TO: ',gammavalue)
################################################################################
### TRAINING THE SVM (NO CROSS VAL) // not used anymore
################################################################################
        #clf = svm.SVC(kernel='linear', C=1)
        #trial=train.test_classifier(traininginput, trainingoutput, clf, 0.2, 0.80, slidwindow) 

################################################################################
### TRAINING THE SVM WITH 5 CROSS-VALIDATION
################################################################################
	    clf0 = svm.SVC(kernel='linear', C=c, cache_size=7000)
	    print('LINEAR KERNEL TYPE')
	    clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)
	    print('')
	    print('')
	    #clf6 = svm.SVC(kernel='rbf', C=c, cache_size=4000, gamma=gammavalue)
	    #print('RBF KERNEL TYPE')
	    #clf1=train.crossvalidation(traininginput, trainingoutput, clf6, slidwindow)
	    #print('')
	    #print('')
	    #clf2 = svm.SVC(kernel='poly', C=c, cache_size=4000, gamma=gammavalue)
	    #print('POLYNOMIAL KERNEL TYPE')
	    #clf3=train.crossvalidation(traininginput, trainingoutput, clf2, slidwindow)
	    #print('')
	    #print('')
	    #clf4 = svm.SVC(kernel='sigmoid', C=c, cache_size=4000, gamma=gammavalue)
	    #print('SIGMOID KERNEL TYPE')
	    #clf5=train.crossvalidation(traininginput, trainingoutput, clf4, slidwindow)
	    #print('')
	    #print('')

################################################################################
### SAVE THE TRAINED MODEL
################################################################################
	filename=open('./trained_models/finalized_model_' + str(slidwindow) + '.pkl','wb') 
	#filename = 'finalized_model1.pkl'
	#pickle.dump(clf, open('finalized_model_' + str(slidwindow) + '_C'+str(c)+'.pkl', 'wb'))
	#or use joblib.dump(clf, filename)

end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
print ('Training done! Bye!')
