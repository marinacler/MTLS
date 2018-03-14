import SVM_training_module as train
import sklearn
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from matplotlib import pyplot as plt

################################################################################
### Getting the real and predicted values for testing performance
################################################################################
filehandle=open('50Prot_dataset_prediction.txt','r')
pred50=filehandle.read().splitlines()
filehandle.close()

filehandle=open('3Protein_PSSM_prediction.txt','r')
pred3_PSSM=filehandle.read().splitlines()
filehandle.close()

filehandle=open('../../datasets/50_extra_proteins/Filtered_BetaBarrelDataset.txt','r')
real50=filehandle.read().splitlines()
filehandle.close()

filehandle=open('../../datasets/50_extra_proteins/examplefortesting_PSSM_realtopologies.txt','r')
real3_PSSM=filehandle.read().splitlines()
filehandle.close()

counter=0
predtopology50=[]
realtopology50=[]
for line in pred50:
    if line.startswith('>'):
        for feature in (pred50[counter+2]):  
            if feature == 'g':   #globular = g = 0 
                predtopology50.append(0)
            elif feature == 'B':   #beta = B = 1
                predtopology50.append(1)
        
        for feature in (real50[counter+2]):  
            if feature == 'g':   #globular = g = 0 
                realtopology50.append(0)
            elif feature == 'B':   #beta = B = 1
                realtopology50.append(1)
        counter=counter+1
    else:
        counter=counter+1

counter2=0
predtopology3=[]
realtopology3=[]    
for line in pred3_PSSM:
    if line.startswith('>'):
        for feature in (pred3_PSSM[counter2+2]):
            if feature == 'g':   #globular = g = 0 
                predtopology3.append(0)
            elif feature == 'B':   #beta = B = 1
                predtopology3.append(1)
        for feature in (real3_PSSM[counter2+2]):  
            if feature == 'g':   #globular = g = 0 
                realtopology3.append(0)
            elif feature == 'B':   #beta = B = 1
                realtopology3.append(1)
        counter2=counter2+1
    else:
        counter2=counter2+1

print(len(realtopology3))
print(len(predtopology3))

################################################################################
### Testing the performance of residue-trained model (Evaluation of predictions)
################################################################################
print('')
print('Performance of prediction using the residue-trained model:')
print('')
cnf_matrix = confusion_matrix(realtopology50, predtopology50)

# CONFUSION MATRIX
target_names = ['Class 0 == globular', 'Class 1 == beta barrel']
fig=plt.figure()
train.plot_confusion_matrix(cnf_matrix, classes=target_names,
                      title='Confusion matrix, without normalization')
plt.show()
plt.close(fig)

# NORMALIZED CONFUSION MATRIX
fignorm=plt.figure()
train.plot_confusion_matrix(cnf_matrix, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
plt.show()
plt.close(fignorm)
main_metrics=sklearn.metrics.classification_report(realtopology50, predtopology50, target_names=target_names)
print (main_metrics)
scores=sklearn.metrics.accuracy_score(realtopology50, predtopology50)
print("The accuracy is: %0.4f" % (scores))

################################################################################
### Testing the performance of PSSM-trained model (Evaluation of predictions)
################################################################################
print('')
print('Performance of prediction using the PSSM-trained model:')
print('')
cnf_matrix = confusion_matrix(realtopology3, predtopology3)

# CONFUSION MATRIX
fig=plt.figure()
train.plot_confusion_matrix(cnf_matrix, classes=target_names,
                      title='Confusion matrix, without normalization')
plt.show()
plt.close(fig)

# NORMALIZED CONFUSION MATRIX
fignorm=plt.figure()
train.plot_confusion_matrix(cnf_matrix, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
plt.show()
plt.close(fignorm)
main_metrics=sklearn.metrics.classification_report(realtopology3, predtopology3, target_names=target_names)
print (main_metrics)
scores=sklearn.metrics.accuracy_score(realtopology3, predtopology3)
print("The accuracy is: %0.4f" % (scores))
