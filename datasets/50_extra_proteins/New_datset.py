################################################################################
### Modifying the downloaded dataset to fit with the 
### required dataset format of my predictor
################################################################################
filehandle=open('top_bp.txt','r')
text=filehandle.read().splitlines()
filehandle.close()
new_dataset=open('BetaBarrelDataset.txt', 'w+')
new_dataset_fasta=open('BetaBarrelDataset_fasta.txt', 'w+')
x=0
for line in text:
    if line.startswith('>'):
        new_dataset.write(line+'\n'+text[x+1]+'\n')
        new_dataset_fasta.write(line+'\n'+text[x+1]+'\n')
        for character in text[x+2]:
            if character == 'M' or character == 'm':
                character=character.replace(character,'B')
                new_dataset.write(character)
            else:
                character=character.replace(character,'g')
                new_dataset.write(character)
        #print(text[x+2])
        new_dataset.write('\n')
        x=x+1 
    else:
        x=x+1
new_dataset.close()
new_dataset_fasta.close()