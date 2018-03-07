import parser_module as prs
from datetime import datetime
import pickle
################################################################################
### LOAD THE MODEL 
################################################################################
start_time = datetime.now()
print('Model Predicting Program is running...')
loaded_model = pickle.load(open('finalized_model1.pkl', 'rb')) 
# or use loaded_model = joblib.load(filename)

################################################################################
### PREDICT TOPOLOGY FROM ANOTHER FASTA FILE
################################################################################
parsed_dictionary_prediction,  dictionary_prediction=prs.parse_fasta('../../datasets/examplefortesting.txt')
# ('./../datasets/membrane-beta_3state.3line.FASTA.txt')
predictioninput = prs.input_for_testing(parsed_dictionary_prediction,35)
print('Predicting your topology...')
prediction=loaded_model.predict(predictioninput)
counter=0
for proteins in dictionary_prediction.keys():
    print('\n')
    print ('>'+proteins)
    seq=dictionary_prediction.get(proteins)
    print (seq)
    pred=prediction[counter:(counter+len(seq))]
    counter=counter+len(seq)
    #print(pred)
    decoded_prediction=prs.decode_topology(pred)
    #''.join(decoded_prediction)
    print(''.join(decoded_prediction))
print('\n')
end_time = datetime.now()
print('Total Running Time: {}'.format(end_time - start_time))
print ('Bye!!!')
