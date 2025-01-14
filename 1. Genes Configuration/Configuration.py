import os
from pathlib import Path
from Bio import Entrez, SeqIO


def get_project_root():
    """Get absolute path to project root directory."""
    # Start with current working directory
    current = Path.cwd()
    
    # Check if we're already in the project root
    if (current / 'data' / 'raw' / 'genes').exists():
        return str(current)
        
    # Look for project root by checking for key directories
    while current != current.parent:
        if (current / 'data' / 'raw' / 'genes').exists():
            return str(current)
        current = current.parent
        
    # If we can't find it, return current directory as fallback
    return str(Path.cwd())

def setup_directories():
    """Create necessary project directories."""
    dirs = [
        os.path.join("data", "raw", "genes"),
        os.path.join("data", "processed"),
        os.path.join("data", "processed", "phylogenetic"),
        os.path.join("results", "figures")
    ]
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        
    # Create figures subdirectories for each gene type
    figure_types = ['protein', 'blast', 'phylogenetic']
    for fig_type in figure_types:
        os.makedirs(os.path.join("results", "figures", fig_type), exist_ok=True)

# Configure Entrez
Entrez.email = 'your.email@example.com'

def download_gene(id_gene: str, name_gene: str, start=None, end=None, complement=False):
    """
    Downloads a GenBank sequence from NCBI, with option to specify a region and calculate reverse complement.

    Args:
        id_gene (str): NCBI database accession ID
        name_gene (str): Name for saving the sequence
        start (int, optional): Start position of region of interest
        end (int, optional): End position of region of interest
        complement (bool, optional): If True, calculates reverse complement
    """
    try:
        # Create genes directory if it doesn't exist
        genes_dir = os.path.join(get_project_root(), "data", "raw", "genes")
        if not os.path.exists(genes_dir):
            os.makedirs(genes_dir)
        
        # Fetch sequence data from NCBI
        if start and end:
            handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", 
                                 id=id_gene, seq_start=start, seq_stop=end)
        else:
            handle = Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", 
                                 id=id_gene)
        
        # Process GenBank record
        seq_record = SeqIO.read(handle, "gb")
        handle.close()
        
        # Calculate reverse complement if needed
        if complement:
            seq_record.seq = seq_record.seq.reverse_complement()
        
        # Save sequence
        output_path = os.path.join("data", "raw", "genes", f"{name_gene}.gb")
        SeqIO.write(seq_record, output_path, "gb")
        
        print(f"GenBank file download for gene '{name_gene}' completed successfully.")
        print(f"Saved to: {os.path.abspath(output_path)}")
    
    except Exception as e:
        print(f"Error downloading gene {id_gene}: {e}")

def download_fasta(gene_id, filename):
    """
    Downloads FASTA file with gene sequences and saves to genes directory.

    Args:
        gene_id (str): NCBI gene ID
        filename (str): Name for saving the sequence
    """
    try:
        # Create genes directory if it doesn't exist
        genes_dir = os.path.join("data", "raw", "genes")
        if not os.path.exists(genes_dir):
            os.makedirs(genes_dir)
        
        # Full path for saving file
        file_path = os.path.join(genes_dir, filename)
        
        # Fetch and save FASTA sequence
        handle = Entrez.efetch(db="protein", id=gene_id, rettype="fasta", retmode="text")
        with open(file_path, "w") as out_file:
            out_file.write(handle.read())
        handle.close()
        
        print(f"FASTA download for gene {gene_id} completed.")
        print(f"Saved to: {os.path.abspath(file_path)}")
    except Exception as e:
        print(f"Error downloading gene {gene_id}: {e}")