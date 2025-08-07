def to_rna(dna_strand: str) -> str:
    rna_strand: str = ""
    for dna in dna_strand:
        match dna:
            case 'G':
                rna_strand = rna_strand + 'C'
            case 'C':
                rna_strand = rna_strand + 'G'
            case 'T':
                rna_strand = rna_strand + 'A'
            case 'A':
                rna_strand = rna_strand + 'U'
            case _:
                rna_strand = rna_strand + ''
    return rna_strand
    
