import parser_module as prs
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics
import pickle
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools

################################################################################
### Training the SVM (no cross val)
################################################################################
def test_classifier(X, y, trial, test_size, train_size,slidwindow):
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=test_size, train_size=train_size)   
    trial.fit(X_train, y_train)
    y_predicted = trial.predict(X_test)
    target_names = ['Class 0 == globular', 'Class 1 == beta barrel']
    print('Trial with sliding window: ',slidwindow)
    print(sklearn.metrics.classification_report(y_test, y_predicted, target_names=target_names))
    # here the explanation of the results given:
    # http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_fscore_support.html#sklearn.metrics.precision_recall_fscore_support
    print ('Score: ', trial.score(X_test, y_test))
    #CONFUSION MATRIX
    cnf_matrix = confusion_matrix(y_test, y_predicted)
    fig=plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=target_names,
                      title='Confusion matrix, without normalization')
    #plt.show()
    plt.close(fig)
    # NORMALIZED CONFUSION MATRIX
    fignorm=plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
    plt.close(fignorm)
    return (trial)

################################################################################
### Training the SVM with 5 cross-validation datasets
################################################################################
def crossvalidation(X,y, clf,slidwindow):   
    print('RESULTS FOR SLIDING WINDOW ',slidwindow)
    clf.fit(X, y)
    predictions=cross_val_predict(clf, X, y, cv=5, n_jobs=-1)
    target_names = ['Class 0 == globular', 'Class 1 == beta barrel']
    #CONFUSION MATRIX
    cnf_matrix = confusion_matrix(y, predictions)
    #fig=plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=target_names,
                      title='Confusion matrix, without normalization')
    #plt.show()
    #plt.close(fig)
    # NORMALIZED CONFUSION MATRIX
    #fignorm=plt.figure()
    plot_confusion_matrix(cnf_matrix, classes=target_names, normalize=True,
                      title='Normalized confusion matrix')
    #plt.close(fignorm)
    main_metrics=sklearn.metrics.classification_report(y, predictions, target_names=target_names)
    print (main_metrics)
    scores = cross_val_score(clf, X, y, cv=5, n_jobs=-1)
    print(scores)
    print("The accuracy for a sliding window of %s: %0.4f (+/- %0.4f)" % (slidwindow, scores.mean(), scores.std() * 2))
    #R2 score https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6
    accuracy = metrics.r2_score(y, predictions)
    print ('Cross-Predicted Accuracy:', accuracy)
    print ('')
    return (clf)

################################################################################
### Function for plotting the confusion matrix
################################################################################
#From sklearn:
#http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

if __name__ == '__main__':
    print("Training model...")
