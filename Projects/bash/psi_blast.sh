################################################################################
### Running psi-blast
################################################################################
cd ../../datasets/fasta_psi
echo "Program is running"
echo "Starting time: $(date)"

for prot in *.fasta ; do
	echo "Running PSI-BLAST on $prot at $(date)..."
	time psiblast -db /scratch/swissport/uniprot.fasta -query $prot -num_iterations 3 -evalue 0.001 -num_threads 8 -out ./align/$prot.psiblast -out_ascii_pssm ./pssm/$prot.pssm 
	echo "Finished running psiblast on $prot at $(date)."
done

echo "PSI-BLAST run is complete"
echo "Ending time: $(date)"

#All the files have been created in the folder datasets so with the following steps I move them to output/psiblast_output
#cd ~/project_course/projects/datasets/fasta_seqs/
#mv *.psiblast ../../output/psiblast_out_50
#mv *.pssm ../../output/psiblast_out_50 
