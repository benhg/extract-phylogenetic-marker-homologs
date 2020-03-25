# extract-phylogenetic-marker-homologs



1. search the transcriptome subsets that are >= to 80% the length of the query for each of the phylogenetic markers then

2. search those hits against the transcriptomes using the programs you and Ellen developed for mapping against the reads and building confidence in the taxon source. then


For step 1,  am I essentially creating a new blast database, which is made up of only transcripts longer than 80% of the length of each phylogenetic marker
11:31
then running BLAST with that marker against that modified database

Then taking those hts and plugging them into STAR (step 2)