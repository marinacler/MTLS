################################################################################
### Get filtered dataset with the corresponding topologies
################################################################################
filehandle=open('Filtered_BetaBarrelDataset_fasta.txt', 'r')
filehandle2=open('BetaBarrelDataset.txt', 'r')
text=filehandle.read().splitlines()
text2=filehandle2.read().splitlines()
filehandle.close()
filehandle2.close()
new_dataset=open('Filtered_BetaBarrelDataset.txt', 'w+')
x=0
y=0
for line in text:
    if line.startswith('>'):
        new_dataset.write(line+'\n'+text[x+1]+'\n')
        for i in range(0,len(text2)):
                if line == text2[i]:
                    new_dataset.write(text2[i+2])
                    new_dataset.write('\n')
        x=x+1 
    else:
        x=x+1
new_dataset.close()