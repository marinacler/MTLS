from collections import OrderedDict
import os

################################################################################
### Defining the binary code for the aa residues
################################################################################
def residues_in_binary():
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
    return (seqbinary)

################################################################################
### Parsing a file in FASTA format
################################################################################
def parse_fasta(filename):
    filehandle=open(filename,'r') #('membrane-beta_3state.3line.FASTA.txt', 'r') 
    text=filehandle.read().splitlines()
    filehandle.close()
    x=0
    seqbinary=residues_in_binary()
    data=OrderedDict()
    datauntranslated=OrderedDict()
    for line in text:
        if line.startswith('>'):
            line=line[1:] #also line=line.replace('>','')
            sequence=[]
            for character in text[x+1]:
                sequence.append(seqbinary.get(character))
            data[line]=  [sequence] #ID=key, sequence=value (binary).
            datauntranslated[line]=text[x+1]
            x=x+1 
        else:
            x=x+1 
    return(data,datauntranslated)

################################################################################
### Parsing a file in FASTA format + topology 
################################################################################
def parse_fasta_topology(filename):
    filehandle=open(filename,'r') #('membrane-beta_2state.3line.txt', 'r') 
    text=filehandle.read().splitlines()
    filehandle.close()
    x=0
    seqbinary=residues_in_binary()
    data=OrderedDict()
    for line in text:
        if line.startswith('>'):
            line=line[1:] #also line=line.replace('>','')
            sequence=[]
            topology=[]
            for character in text[x+1]:  
                sequence.append(seqbinary.get(character))
            for feature in (text[x+2]):  
                if feature == 'g':   #globular = g = 0 
                    topology.append(0)
                elif feature == 'B':   #beta = B = 1
                    topology.append(1)
         
            data[line]=  [sequence,topology] #ID=key, [sequence,topology]=values
            x=x+1
        else:
            x=x+1
    return(data)
    
################################################################################
### Creating input vectors for the SVM using a predefined sliding window.
### The input dictionary should have been parsed first
################################################################################
def input_for_training(dictionary,slidwindow):
    protsfortraining=dictionary.keys()
    traininginput=[]
    trainingoutput=[]
    flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for proteins in protsfortraining:
        flankinglist=[]
        for i in range(int(slidwindow/2)):
            flankinglist=[flankingseq]+flankinglist
        flankinglist=flankinglist+(dictionary.get(proteins)[0])
        for i in range(int(slidwindow/2)):
            flankinglist=flankinglist+[flankingseq]
        features=dictionary.get(proteins)[1]
        
        for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
            slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
            flat_list = [item for sublist in slidingsequence for item in sublist]
            traininginput.append(flat_list)
            trainingoutput.append(features[j-int(slidwindow/2)]) 
    return traininginput, trainingoutput

################################################################################
### Creating input vectors for the SVM using a predefined sliding window.
### The input vectors will contain evol. info (from PSSM, from PSI-BLAST)
### The input dictionary should have been parsed first
################################################################################
def input_for_training_pssm(dictionary,slidwindow):
    traininginput=[]
    trainingoutput=[]
    for proteins in dictionary.keys():
        if os.path.isfile('../../datasets/fasta_psi/pssm/'+proteins+'.fasta.pssm'):
            #print('Running: ', proteins,'.fasta.pssm')
            filehandle= open('../../datasets/fasta_psi/pssm/'+proteins+'.fasta.pssm', 'r')
            text=filehandle.read().splitlines()
            filehandle.close()
            flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            flankinglist=[]
            for i in range(int(slidwindow/2)):
                flankinglist=[flankingseq]+flankinglist
            for lineindex in range(3,(len(text)-6)):
                elements=text[lineindex].split()
                flankinglist=flankinglist+[(list(elements[22:-2]))]
            for i in range(int(slidwindow/2)):
                flankinglist=flankinglist+[flankingseq]
            #Normalization
            for position in flankinglist:
                for number in range (0, len(position)):
                    position[number] = int(position[number])/100
            #Extract topology
            features=dictionary.get(proteins)[1]
            for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
                slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
                flat_list = [item for sublist in slidingsequence for item in sublist]
                traininginput.append(flat_list)
                trainingoutput.append(features[j-int(slidwindow/2)])
    return traininginput, trainingoutput

################################################################################
### Creating input vectors for the using the predictor.
### The input dictionary should have been parsed first
################################################################################
def input_for_testing(dictionary,slidwindow): # parsed dictionary
    testinginput=[]
    flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for proteins in dictionary.keys():
        flankinglist=[]
        for i in range(int(slidwindow/2)):
            flankinglist=[flankingseq]+flankinglist
        flankinglist=flankinglist+(dictionary.get(proteins)[0])
        for i in range(int(slidwindow/2)): 
            flankinglist=flankinglist+[flankingseq]
        #Sliding windows
        for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
            slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
            flat_list = [item for sublist in slidingsequence for item in sublist]
            testinginput.append(flat_list)                
    return (testinginput)
    
################################################################################
### Creating input vectors for the using the predictor trained with PSSM data.
### The input dictionary should not have been parsed first
################################################################################
def input_for_testing_PSSM(dictionary,slidwindow): # no parsed dictionary
    testinginput=[]
    for proteins in dictionary.keys():
        if os.path.isfile('../../datasets/fasta_psi/pssm/'+proteins+'.fasta.pssm'):
            #print('Running: ', proteins,'.fasta.pssm')
            filehandle= open('../../datasets/fasta_psi/pssm/'+proteins+'.fasta.pssm', 'r')
            text=filehandle.read().splitlines()
            filehandle.close()
            flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            flankinglist=[]
            for i in range(int(slidwindow/2)):
                flankinglist=[flankingseq]+flankinglist
            for lineindex in range(3,(len(text)-6)):
                elements=text[lineindex].split()
                flankinglist=flankinglist+[(list(elements[22:-2]))]
            for i in range(int(slidwindow/2)):
                flankinglist=flankinglist+[flankingseq]
            #Normalization
            for position in flankinglist:
                for number in range (0, len(position)):
                    position[number] = int(position[number])/100
            #Sliding windows
            for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
                slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
                flat_list = [item for sublist in slidingsequence for item in sublist]
                testinginput.append(flat_list)                          
    return (testinginput)

################################################################################
### Translator of prediction into topology
################################################################################
def decode_topology(inputlist):
    output=[]
    for element in inputlist:
        if element == 0:   #globular = g = 0 
            output.append('g')
        elif element == 1:   #beta = B = 1
            output.append('B')
    return (output)

if __name__ == '__main__':
    print("Parsing...")
