import parsl
from parsl.app.app import bash_app
from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor
import os

config = Config(
    executors=[ThreadPoolExecutor()],
    lazy_errors=True
)

parsl.load(config)

from Bio import SeqIO

@bash_app
def create_db(sequence_name):
    import os
    if not os.path.isdir(f"databases/{sequence_name}"):
        return "Fail"
    return f"cd databases/{sequence_name}; makeblastdb -in sufficient_length.fasta -out {sequence_name} -parse_seqids -dbtype nucl; cd ../.."

def make_sequence_db_input_fasta(sequence, sequence_name):
    import os
    from glob import glob
    from Bio import SeqIO
    min_length = 0.8 * len(sequence)
    if not os.path.isdir(f"databases/{sequence_name}"):
        os.makedirs(f"databases/{sequence_name}")
    with open(f"databases/{sequence_name}/sufficient_length.fasta", "w") as fh:
        for file in glob("/home/labs/binford/Assembled_Untranslated_Transcriptomes/s*"):
            with open(file) as read_fh:
                for record in SeqIO.parse(read_fh, "fasta"):
                    if len(record.seq) >= min_length:
                        print(f"Writing {record.id}")
                        fh.write(f">{record.id}\n")
                        fh.write(f"{record.seq}\n")
                    else:
                        print(f"Not writing {record.id}")


def make_database_input_files():
    with open("input_sequences.fasta") as fh:
        for record in SeqIO.parse(fh, "fasta"):
            make_sequence_db_input_fasta(record.seq, record.id)

if __name__ == '__main__':
    make_database_input_files()
    databases = os.listdir("databases")
    for database in databases:
        create_db(database)