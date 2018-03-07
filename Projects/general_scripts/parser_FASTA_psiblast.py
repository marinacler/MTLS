################################################################################
### Transforming the dataset in fasta format (individual files)
################################################################################

from collections import OrderedDict

filehandle=open('../../datasets/membrane-beta_2state.3line.txt','r') # ('../datasets/example.txt')
text=filehandle.read().splitlines()
filehandle.close()
x=0
data=OrderedDict()
for line in text:
    if line.startswith('>'):
	    data[line]= text[x+1] #ID=key, [sequence]=value
	    x=x+1
    else:
        x=x+1
for proteins in data.keys():
	name=proteins[1:]# proteins.replace('>','')
	with open('../../datasets/fasta_psi/%r.fasta' %name, 'w+') as fasta:
		sequence=str(data.get(proteins))
		fasta.write(proteins+'\n' + sequence +'\n')
print('Transformation in fasta format completed. Document safed in datasets/fasta_psi folder')
