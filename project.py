#import parser_module
import numpy as np
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
import pickle
from sklearn.externals import joblib

################################################################################
### Defining the binary code for the aa residues
################################################################################
seqbinary= {}
seqbinary['A']=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['R']=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['N']=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['D']=[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['C']=[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['Q']=[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['E']=[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['G']=[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['H']=[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['I']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['L']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['K']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
seqbinary['M']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
seqbinary['F']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
seqbinary['P']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
seqbinary['S']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
seqbinary['T']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
seqbinary['W']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
seqbinary['Y']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
seqbinary['V']=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

################################################################################
### Opens the file and store each feature of the txt file into
### the appropriate elements within a dictionary.
################################################################################
filehandle=open('example.txt','r') #('membrane-beta_2state.3line.txt', 'r') 
text=filehandle.read().splitlines()
filehandle.close()
x=0
data={}
for line in text:
	if line.startswith('>'):
		line=line[1:] #also line=line.replace('>','')
		sequence=[]
		topology=[]
		for character in text[x+1]:   #text[x+1] is the protein sequence
			sequence.append(seqbinary.get(character))
		for feature in (text[x+2]):  #text[x+2] is the topology
			if feature == 'g':   #globular = g = 0 
				topology.append(0)
			elif feature == 'B':   #beta = B = 1
				topology.append(1)
         
		data[line]=  [sequence,topology] #the ID is the key, the sequence and topology are the values fot that ID, already converted to a binary code (aa residues) and to letters (topology:0 or 1). 
		x=x+1  #counter to store the values in the corresponding key
	else:
        	x=x+1  #counter to store the values in the corresponding key


################################################################################
### Opens the FASTA file and store each feature of the txt file into
### the appropriate elements within a dictionary.
################################################################################
filehandle=open('examplefortesting.txt','r') 
text=filehandle.read().splitlines()
filehandle.close()
x=0
dataFASTA={}
for line in text:
	if line.startswith('>'):
		line=line[1:] #also line=line.replace('>','')
		sequence=[]  #text[x+1] is the protein sequence
		for character in text[x+1]:  
			sequence.append(seqbinary.get(character))
         
		dataFASTA[line]=  [sequence] #the ID is the key, the sequence is the value fot that ID, already converted to a binary code (aa residues)
		x=x+1  #counter to store the values in the corresponding key
	else:
        	x=x+1  #counter to store the values in the corresponding key

################################################################################
### Creating input vectors for the SVM using a predefined sliding window
################################################################################
for k in list(range(7,8)):  #1,32,2
	slidwindow=k   #add int(sliding window size / 2) at both endings for flanking.
	protsfortesting=dataFASTA.keys()
	protsfortraining=data.keys()  #these are all the proteins in my dataset
	traininginput=[]   #list of seqs in binary that will be used as an input for SVM
	trainingoutput=[]  #list of topologies in numbers (0,1) that will be used as input for SVM, although they should be the outputs (but we are working with a supervised learning machine method)
	testinginput=[]
	for proteins in protsfortraining:
		# data.get(proteins)[0] is the seq in binary and data.get(proteins)[1] is the topology
		flankinglist=[]
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the beggining for flanking. 
			flankinglist=[flankingseq]+flankinglist
		flankinglist=flankinglist+(data.get(proteins)[0])
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the end for flanking. 
			flankinglist=flankinglist+[flankingseq]
 
		features=data.get(proteins)[1] #data.get(proteins)[1] is the topology for each residue in the protein

		for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
			slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
			flat_list = [item for sublist in slidingsequence for item in sublist]
			traininginput.append(flat_list)
			trainingoutput.append(features[j-int(slidwindow/2)]) 

	for proteins in protsfortesting:
		flankinglist=[]
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the beggining for flanking. 
			flankinglist=[flankingseq]+flankinglist
		flankinglist=flankinglist+(dataFASTA.get(proteins)[0])
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the end for flanking. 
			flankinglist=flankinglist+[flankingseq]

		for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
			slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
			flat_list = [item for sublist in slidingsequence for item in sublist]
			testinginput.append(flat_list)
			
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
	print('Trial with sliding window:')
	print(slidwindow)
	print(sklearn.metrics.classification_report(y_test, y_predicted, target_names=target_names))
	# here the explanation of the results given: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support


	clf = svm.SVC(kernel='linear', C=1).fit(traininginput, trainingoutput)
	#clf = svm.SVC(kernel='linear', C=1)
	scores = cross_val_score(clf, traininginput, trainingoutput, cv=5, n_jobs=-1)
	#prediction=cross_val_predict(estimator, X=array-like The data to fit. Can be, for example a list, or an array at least 2d.)

	print(scores)
	print("The accuracy for a sliding window of %s: %0.4f (+/- %0.4f)" % (slidwindow, scores.mean(), scores.std() * 2))


################################################################################
### Save the model using pickle
################################################################################
	filename = 'finalized_model1.pkl'
	pickle.dump(clf, open(filename, 'wb')) #or use joblib.dump(clf, filename)


################################################################################
### Load the model some time after
################################################################################
	loaded_model = pickle.load(open(filename, 'rb'))   #loaded_model = joblib.load(filename)
	result = loaded_model.score(X_test, y_test)    #result = loaded_model.score(X_test, Y_test)
	#print(result)  #result = loaded_model.score(X_test, Y_test)

################################################################################
### Predicting features from another set
################################################################################
	print('Predicting your topology...')
	prediction=clf.predict(testinginput)
	print(prediction)
	#x_for_predict = open("myexample.txt") #loadScoringData("example.txt") Assuming same data format without target variable  (which is not the case, but I will parse the data to enter later)
	#y_predict = loaded_model.predict(testinginput)#(x_for_predict)
	#plotResults(loaded_model, y_predict)# just a signature. 

