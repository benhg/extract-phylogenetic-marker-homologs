import parsl
from Bio import seqio

@bash_app
def create_db(sequence, sequence_name):
	import os
	os.makedirs(sequence_name)
	make_sequence_db_input_fasta(sequence, sequence_name)
	return ""

def make_sequence_db_input_fasta(sequence, sequence_name):
	import os
	from glob import glob
	min_length = 0.8 * len(sequence)
	with open(f"{sequence_name}/sufficient_length.fasta", "w") as fh:
		for file in glob("/home/labs/binford/raw_reads/lane*"):
			with open(file) as read_fh:
				


with open("input_sequences.fasta") as fh:
