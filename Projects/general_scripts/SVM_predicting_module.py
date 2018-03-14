import parser_module as prs
import pickle

################################################################################
### Loading the (best found) model
################################################################################
def Loading():
    loaded_model = pickle.load(open('./trained_models/Last_model_35_C1.pkl','rb'))
    #result = loaded_model.score(X_test, y_test) #result = loaded_model.score(X_test, Y_test)
    #print(result)  #result = loaded_model.score(X_test, Y_test)
    return loaded_model

################################################################################
### Loading the (best found) model with evolutionary information
################################################################################
def Loading_PSSM():
    loaded_model = pickle.load(open('./trained_models/Last_model_35_C0.6_PSSM.pkl','rb'))
    #result = loaded_model.score(X_test, y_test) #result = loaded_model.score(X_test, Y_test)
    #print(result)  #result = loaded_model.score(X_test, Y_test)
    return loaded_model

################################################################################
### Parsing the file to predict 
################################################################################
def PredictionParser(filetopredict,loaded_model):
    slidwindow=35 #Because the best saved model has this sliding window
    parsed_dictionary_prediction,  dictionary_prediction=prs.parse_fasta('../../datasets/'+filetopredict)
    predictioninput = prs.input_for_testing(parsed_dictionary_prediction,slidwindow)
    print('\nPredicting your topology...')
    prediction=loaded_model.predict(predictioninput)
    return dictionary_prediction, prediction

################################################################################
### Parsing the file to predict on a PSSM-trained model
################################################################################
def PredictionParser_PSSM(filetopredict,loaded_model):
    slidwindow=35 #Because the best saved model has this sliding window
    parsed_dictionary_prediction,  dictionary_prediction=prs.parse_fasta('../../datasets/'+filetopredict)
    predictioninput = prs.input_for_testing_PSSM(dictionary_prediction,slidwindow)
    print('\nPredicting your topology...')
    prediction=loaded_model.predict(predictioninput)
    return dictionary_prediction, prediction

################################################################################
### Saving the prediction
################################################################################
def Saveprediction(dictionary,prediction,file_name): 
    filename=open(file_name+'_prediction.txt','w') 
    counter=0
    for proteins in dictionary.keys():
        filename.write('>'+proteins)
        filename.write('\n')
        seq=dictionary.get(proteins)
        filename.write(seq)
        filename.write('\n')
        pred=prediction[counter:(counter+len(seq))]
        counter=counter+len(seq)
        decoded_prediction=prs.decode_topology(pred)
        filename.write(''.join(decoded_prediction))
        filename.write('\n')     
    filename.close
    return()

if __name__ == '__main__':
    print("Training model...")
