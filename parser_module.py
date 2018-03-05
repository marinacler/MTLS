from collections import OrderedDict
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
    for line in text:
	    if line.startswith('>'):
		    line=line[1:] #also line=line.replace('>','')
		    sequence=[]
		    for character in text[x+1]:   #text[x+1] is the protein sequence
			    sequence.append(seqbinary.get(character))
		    data[line]=  [sequence] #the ID is the key, the sequence is the value fot that ID, already converted to a binary code (aa residues).
		    x=x+1  #counter to store the values in the corresponding key
	    else:
        	x=x+1  #counter to store the values in the corresponding key

    return(data)

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

    return(data)
    
################################################################################
### Creating input vectors for the SVM using a predefined sliding window.
### The input dictionary should have been parsed first
################################################################################
def input_for_training(dictionary,slidwindow):
	protsfortraining=dictionary.keys()  #these are all the proteins in my dataset
	traininginput=[]   #list of seqs in binary that will be used as an input for SVM
	trainingoutput=[]  #list of topologies in numbers (0,1) that will be used as input for SVM, although they should be the outputs (but we are working with a supervised learning machine method)
	flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for proteins in protsfortraining:
		flankinglist=[]
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the beggining for flanking. 
			flankinglist=[flankingseq]+flankinglist
		flankinglist=flankinglist+(dictionary.get(proteins)[0]) # data.get(proteins)[0] is the seq in binary
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the end for flanking. 
			flankinglist=flankinglist+[flankingseq]
 
		features=dictionary.get(proteins)[1] #data.get(proteins)[1] is the topology for each residue in the protein

		for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
			slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
			flat_list = [item for sublist in slidingsequence for item in sublist]
			traininginput.append(flat_list)
			trainingoutput.append(features[j-int(slidwindow/2)]) 

	return traininginput, trainingoutput

################################################################################
### Creating input vectors for the testing the predictor.
### The input dictionary should have been parsed first
################################################################################
def input_for_testing(dictionary,slidwindow):
	protsfortesting=dictionary.keys() #data.keys() from parse_fasta(filename)
	testinginput=[]
	flankingseq= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	#I HAVE TO SORT THE DICTIONARY IN A WAY THAT THE ORDER IS THE SAME AS THE PROTS IN THE TXT FILE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	for proteins in protsfortesting:
		flankinglist=[]
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the beggining for flanking. 
			flankinglist=[flankingseq]+flankinglist
		flankinglist=flankinglist+(dictionary.get(proteins)[0])
		for i in range(int(slidwindow/2)):   #add int(sliding window size / 2) at the end for flanking. 
			flankinglist=flankinglist+[flankingseq]

		for j in range(int(slidwindow/2),(len(flankinglist)-int(slidwindow/2))):
			slidingsequence=flankinglist[(j-int(slidwindow/2)):(j+int(slidwindow/2)+1)]
			flat_list = [item for sublist in slidingsequence for item in sublist]
			testinginput.append(flat_list)
					
	return (testinginput)

################################################################################
### Translator of prediction into topology
################################################################################
def translate_topology(inputlist):
	output=[]
	for element in inputlist:
		if element == 0:   #globular = g = 0 
			output.append('g')
		elif element == 1:   #beta = B = 1
			output.append('B')
	return (output)

if __name__ == '__main__':
    print("Parsing")
    #data = parse_fasta_topology('example.txt')
    #print (data.keys())

