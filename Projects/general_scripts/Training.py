import parser_module as prs
import SVM_training_module as train
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from datetime import datetime
import pickle
#from sklearn.externals import joblib

################################################################################
### Get input for training the SVM
################################################################################
start_time = datetime.now()
print('Model Training Program is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/example.txt')
# ('../../datasets/membrane-beta_2state.3line.txt')# 
#for slidwindow in range(35,36):# ,2):
for m in range(-6,-4):
	c=1*10**m
	print('C VARIABLE EQUAL TO: ',c)
	slidwindow=35
	traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)

################################################################################
### Train the SVM (no cross val)
################################################################################
	#clf = svm.SVC(kernel='linear', C=1)
	#trial=train.test_classifier(traininginput, trainingoutput, clf, 0.2, 0.80, slidwindow) 

################################################################################
### Training the SVM with 5 cross-validation datasets
################################################################################
	clf0 = svm.SVC(kernel='linear', C=c, cache_size=3000)
	print('LINEAR KERNEL TYPE')
	clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)
	print('')
	print('')
	#clf6 = svm.SVC(kernel='rbf', C=1, cache_size=3000)
	#print('RBF KERNEL TYPE')
	#clf2=train.crossvalidation(traininginput, trainingoutput, clf6, slidwindow)
	#print('')
	#print('')
	#clf2 = svm.SVC(kernel='poly', C=1, cache_size=3000)
	#print('POLYNOMIAL KERNEL TYPE')
	#clf3=train.crossvalidation(traininginput, trainingoutput, clf2, slidwindow)
	#print('')
	#print('')
	#clf4 = svm.SVC(kernel='sigmoid', C=1, cache_size=3000)
	#print('SIGMOID KERNEL TYPE')
	#clf5=train.crossvalidation(traininginput, trainingoutput, clf4, slidwindow)
	#print('')
	#print('')

for m in range(5,7):
	c=1*10**m
	print('C VARIABLE EQUAL TO: ',c)
	slidwindow=35
	traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)

################################################################################
### Train the SVM (no cross val)
################################################################################
	#clf = svm.SVC(kernel='linear', C=1)
	#trial=train.test_classifier(traininginput, trainingoutput, clf, 0.2, 0.80, slidwindow) 

################################################################################
### Training the SVM with 5 cross-validation datasets
################################################################################
	clf0 = svm.SVC(kernel='linear', C=c, cache_size=3000)
	print('LINEAR KERNEL TYPE')
	clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)
	print('')
	print('')
################################################################################
### SAVE THE BEST TRAINED MODEL
################################################################################
#filename = 'finalized_model1.pkl'
#pickle.dump(clf, open(filename, 'wb'))
#or use joblib.dump(clf, filename)

################################################################################
### LOAD THE MODEL 
################################################################################
#loaded_model = pickle.load(open(filename, 'rb')) #loaded_model = joblib.load(filename)
#result = loaded_model.score(X_test, y_test) #result = loaded_model.score(X_test, Y_test)
#print(result)  #result = loaded_model.score(X_test, Y_test)

################################################################################
### PREDICT TOPOLOGY FROM ANOTHER FASTA FILE
################################################################################
#parsed_dictionary_prediction=prs.parse_fasta('./../datasets/examplefortesting.txt')
# ('./../datasets/membrane-beta_3state.3line.FASTA.txt')
#predictioninput = prs.input_for_testing(parsed_dictionary_prediction,slidwindow)

#print('Predicting your topology...')
#prediction=loaded_model.predict(predictioninput)
#print(prediction)
#decoded_prediction=prs.decode_topology(prediction)
#print(decoded_prediction)
end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
print ('Training done! Bye!')
