import parser_module as prs
import SVM_training_module as train
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from datetime import datetime
import pickle

################################################################################
### Getting the input for training the SVM
################################################################################
start_time = datetime.now()
print('Model Training Program is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/membrane-beta_2state.3line.txt') #('../../datasets/example.txt')
# ('../../datasets/membrane-beta_2state.3line.txt')
print('FULL DATASET')


listcvalues=[0.6,0.8,0.9,1]
for m in listcvalues:
	c=m
	slidwindow=35
	print('C value equal to: ',m)
	
#for slidwindow in range(5,50,2):
	traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)
	if m>0: #for value in range(-10,0):
	    #gammavalue=10**value
	    #print('GAMMA VARIABLE EQUAL TO: ',gammavalue)
################################################################################
### Training the SVM (no cross-val) // not used anymore
################################################################################
        #clf = svm.SVC(kernel='linear', C=1)
        #trial=train.test_classifier(traininginput, trainingoutput, clf, 0.2, 0.80, slidwindow) 

################################################################################
### Training the SVM with 5 cross-validation
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
### Saving the trained model
################################################################################
	    filename=open('./trained_models/Last_model_' + str(slidwindow) +'_C'+str(c)+'.pkl','wb')
	    pickle.dump(clf,filename)

end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
print ('Training done! Bye!')
