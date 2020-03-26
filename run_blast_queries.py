import sys
import os
import parsl
from parsl.app.app import bash_app
from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor
import os
import glob

databases_translate_table = {
                                "18S": "databases/18S_Periegops_suterii_QMBS/",
                                "12S": "databases/12S_Drymusa_rengan_AToL/",
                                "COI": "databases/COI_Periegops_suterii_QMBS/",
                                "28S": "databases/28S_Periegops_suterii_LUNZ00012725/",
                                "H3": "databases/H3_Periegops_suterii_QMBS/",
                                "16S": "databases/16S_Periegops_suterii_QMBS/",
                            }


config = Config(
    executors=[ThreadPoolExecutor()],
    lazy_errors=True
)

parsl.load(config)

#@bash_app
def run_blast_query(input_prefix):
    database_dir = databases_translate_table[input_prefix]
    database_name = glob.glob(f"{database_dir}/*.fasta")[0].split("/")[-1]
    #print(database_name)
    input_file = f"../../input_files/{input_prefix}_in.fasta"
    output_file = f"{input_prefix}_out.txt"
    blast_cmd = f"blastn -db {database_name} -query {input_file} -out ../../output_files/{output_file}"
    print(blast_cmd)
    return f"cd {database_dir}; {blast_cmd}; cd ../../;"



if __name__ == '__main__':
    all_to_search = glob.glob("input_files/*_in.fasta")
    fus = []
    for seq in all_to_search:
        seq_prefix = seq.split("/")[1].split('_')[0]
        fus.append(run_blast_query(seq_prefix))
    fus[-1].result()