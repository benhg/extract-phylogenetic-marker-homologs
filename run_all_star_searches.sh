#!/bin/bash

python3 run_star_queries.py STAR_input_fastas/16S_input.fasta /home/users/glick/extract-phylogenetic-marker-homologs/16S_star_out
python3 run_star_queries.py STAR_input_fastas/18S_input.fasta /home/users/glick/extract-phylogenetic-marker-homologs/18S_star_out
python3 run_star_queries.py STAR_input_fastas/28S_input.fasta /home/users/glick/extract-phylogenetic-marker-homologs/28S_star_out
python3 run_star_queries.py STAR_input_fastas/COI_input.fasta /home/users/glick/extract-phylogenetic-marker-homologs/COI_star_out
python3 run_star_queries.py STAR_input_fastas/H3S_input.fasta /home/users/glick/extract-phylogenetic-marker-homologs/H3S_star_out

