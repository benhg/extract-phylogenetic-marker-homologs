from Bio import SeqIO
all_transcripts_fasta = "~/all.fasta"

# The FASTA ids have other stuff in them so we need to repeatedly iterate through.
# This sucks.
# I was gonna use some hashtag dynamic programming but now life is terrible


def create_single_input_fasta(input_prefix):
	sequences_list = [f.split(" ")[0] for f in open(f"STAR_input_fastas/{input_prefix}_seq_list.txt").readlines()]
	with open(f"STAR_input_fastas/{input_prefix}_input.fasta", "w") as fh:
		for sequence_name in sequences_list:
			fh.write(f">{sequence_name}\n")
			sequence = get_sequence(sequence_name)
			fh.write(f"{sequence}\n")

def get_sequence(sequence_name):
	with open(all_transcripts_fasta, "rU") as handle:
	    for record in SeqIO.parse(handle, "fasta"):
	        if sequence_name in record.id:
	        	print(f"Found {sequence_name}")
	        	return record.seq
	    return "Couldnae Find"
	    print(f"Couldn't find {sequence_name}")


if __name__ == '__main__':
	input_prefixes = ["12S", "16S", "18S", "28S", "COI", "H3"]
	for prefix in input_prefixes:
		create_single_input_fasta(prefix)
