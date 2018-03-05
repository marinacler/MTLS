#THIS IS THE PROJECT WITH MODULES
import parser_module
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
import pickle
#from sklearn.externals import joblib

################################################################################
### TRAIN THE SVM
################################################################################
trainingdict=parser_module.parse_fasta_topology('example.txt')#('membrane-beta_2state.3line.txt')
slidwindow=7
traininginput, trainingoutput = parser_module.input_for_training(trainingdict,slidwindow)

################################################################################
### Training a SVM with 5 cross-validation datasets
################################################################################
#clf = svm.SVC(kernel='linear', C=1)
#test_classifier(traininginput, trainingoutput, clf, test_size=0.2, train_size=0.80, confusion=False) #y_names=files.target_names, confusion=False)
#train-test split FUNCTION
#def test_classifier(X, y, clf, test_size=0.20, train_size=0.80, y_names=None, confusion=False):
#	X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=test_size, train_size=train_size)
#	clf.fit(X_train, y_train)
#	y_predicted = clf.predict(X_test)
#	print (sklearn.metrics.classification_report(y_test, y_predicted, target_names=y_names))

X_train, X_test, y_train, y_test = model_selection.train_test_split(traininginput, trainingoutput, test_size=0.20, train_size=0.8)
trial = svm.SVC(kernel='linear', C=1)	
trial.fit(X_train, y_train)
	
y_predicted = trial.predict(X_test)
target_names = ['Class 0 == globular', 'Class 1 == beta barrel']
print('Trial with sliding window: ',slidwindow)
print(sklearn.metrics.classification_report(y_test, y_predicted, target_names=target_names))
# here the explanation of the results given: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support


clf = svm.SVC(kernel='linear', C=1).fit(traininginput, trainingoutput)
#clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, traininginput, trainingoutput, cv=5, n_jobs=-1)
#prediction=cross_val_predict(estimator, X=array-like The data to fit. Can be, for example a list, or an array at least 2d.)

print(scores)
print("The accuracy for a sliding window of %s: %0.4f (+/- %0.4f)" % (slidwindow, scores.mean(), scores.std() * 2))

################################################################################
### SAVE THE BEST TRAINED MODEL
################################################################################
filename = 'finalized_model1.pkl'
pickle.dump(clf, open(filename, 'wb')) #or use joblib.dump(clf, filename)

################################################################################
### LOAD THE MODEL 
################################################################################
loaded_model = pickle.load(open(filename, 'rb'))   #loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, y_test)    #result = loaded_model.score(X_test, Y_test)
#print(result)  #result = loaded_model.score(X_test, Y_test)

################################################################################
### PREDICT TOPOLOGY FROM ANOTHER FASTA FILE
################################################################################
parsed_dictionary_prediction=parser_module.parse_fasta('examplefortesting.txt')   #('membrane-beta_3state.3line.FASTA.txt')
predictioninput = parser_module.input_for_testing(parsed_dictionary_prediction,slidwindow)


print('Predicting your topology...')
prediction=loaded_model.predict(predictioninput)
print(prediction)
#x_for_predict = open("myexample.txt") #loadScoringData("example.txt") Assuming same data format without target variable  (which is not the case, but I will parse the data to enter later)
#y_predict = loaded_model.predict(testinginput)#(x_for_predict)
#plotResults(loaded_model, y_predict)# just a signature. 

output=[]
for element in prediction:
	if element == 0:   #globular = g = 0 
		output.append('g')
	elif element == 1:   #beta = B = 1
		output.append('B')
print(output)
