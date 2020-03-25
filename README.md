# extract-phylogenetic-marker-homologs



1. search the transcriptome subsets that are >= to 80% the length of the query for each of the phylogenetic markers then

2. search those hits against the transcriptomes using the programs you and Ellen developed for mapping against the reads and building confidence in the taxon source. then


For step 1,  am I essentially creating a new blast database, which is made up of only transcripts longer than 80% of the length of each phylogenetic marker
11:31
then running BLAST with that marker against that modified database

Then taking those hts and plugging them into STAR (step 2)

NB: `awk 'BEGIN{RS=">"}NR>1{sub("\n","\t"); gsub("\n",""); print RS$0}' sufficient_length.fasta | awk '!seen[$1]++' | awk -v OFS="\n" '{print $1,$2}' > deduped.fasta` to deduplicate fasta

NB: `makeblastdb -in deduped.fasta -out 16S_Periegops -parse_seqids -dbtype nucl` to make blast db