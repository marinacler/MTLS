import parser_module as prs
import SVM_training_module as train
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from datetime import datetime
import pickle
from sklearn.ensemble import RandomForestRegressor
#Tools for visualizing single decision tree
from sklearn.tree import export_graphviz
import pydot

################################################################################
### Get input for training the SVM
################################################################################
start_time = datetime.now()
print('Model Training Program is running...')
parsed_dictionary_training=prs.parse_fasta_topology('../../datasets/membrane-beta_2state.3line.txt')
slidwindow=35
c=0.8
traininginput, trainingoutput = prs.input_for_training(parsed_dictionary_training,slidwindow)

################################################################################
### Training the SVM with 5 cross-validation
################################################################################
clf0 = svm.SVC(kernel='linear', C=c, cache_size=7000)
print('LINEAR KERNEL TYPE')
clf=train.crossvalidation(traininginput, trainingoutput, clf0, slidwindow)
print('')
print('')

rf0=RandomForestRegressor(n_estimators=1000, random_state=42)
print('RANDOM FOREST')
rf=train.crossvalidation(traininginput, trainingoutput, rf0, slidwindow)
print('')
print('')

################################################################################
### Saving the trained model
################################################################################
filename=open('./trained_models/finalized_model_' + str(slidwindow) + '_RandomForest.pkl','wb')
pickle.dump(rf, filename)

################################################################################
### Single decision tree visualization
################################################################################
foresttree=rf.estimators_[5]
target_names = ['Class 0 == globular', 'Class 1 == beta barrel']
export_graphviz(foresttree, out_file='ForestTree.dot', feature_names=target_names, rounded= True, precision=1)
(graph, )=pydot.graph_from_dot_file('ForestTree.dot')
graph.write_png('ForestTree.png')
